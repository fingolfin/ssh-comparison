#!/usr/bin/env python3
"""
ssh-detect: a fake SSH server that records what a client offers.

It exchanges identification strings, sends a KEXINIT, reads the client's
KEXINIT and disconnects before any key exchange. What the client offered
is printed as the YAML fragment used in _impls/*.md.

    python3 ssh-detect.py [--port 2222] [--bind ADDRESS] [--out DIR] [--once]

Then point the client under test at this machine and port; it will fail
to connect, which is expected. Needs only the Python 3 standard library.

    client                          ssh-detect
      |  <-- identification ---------  |
      |  --- identification -------->  |  record ident
      |  <-- SSH_MSG_KEXINIT --------  |  broad offer, see SERVER_OFFER
      |  --- SSH_MSG_KEXINIT ------->  |  record name-lists
      |  <-- SSH_MSG_DISCONNECT -----  |
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import socket
import socketserver
import struct
import sys
import threading
from dataclasses import dataclass

VERSION = "2.0"
SERVER_IDENT = f"SSH-2.0-ssh_detect_{VERSION}"
DEFAULT_PORT = 2222
SOCKET_TIMEOUT = 30  # seconds

# RFC 4253 message numbers, disconnect reason and limits
SSH_MSG_DISCONNECT = 1
SSH_MSG_IGNORE = 2
SSH_MSG_DEBUG = 4
SSH_MSG_KEXINIT = 20
SSH_DISCONNECT_BY_APPLICATION = 11

MAX_IDENT_LINE = 255  # including CR LF, section 4.2
MAX_PREAMBLE_LINES = 50
MAX_PACKET_LENGTH = 35000  # section 6.1
BLOCK_SIZE = 8  # cipher "none"
MIN_PADDING = 4
COOKIE_LENGTH = 16

# The ten name-lists of SSH_MSG_KEXINIT, in wire order (RFC 4253 section 7.1).
NAME_LISTS = (
    "kex_algorithms",
    "server_host_key_algorithms",
    "encryption_algorithms_client_to_server",
    "encryption_algorithms_server_to_client",
    "mac_algorithms_client_to_server",
    "mac_algorithms_server_to_client",
    "compression_algorithms_client_to_server",
    "compression_algorithms_server_to_client",
    "languages_client_to_server",
    "languages_server_to_client",
)

# What this server claims to support. A client sends its KEXINIT whatever
# we offer, but a broad offer keeps one that checks for overlap first from
# hanging up early.
_CIPHERS = [
    "chacha20-poly1305@openssh.com",
    "aes128-gcm@openssh.com", "aes256-gcm@openssh.com",
    "aes128-ctr", "aes192-ctr", "aes256-ctr",
    "aes128-cbc", "aes192-cbc", "aes256-cbc", "3des-cbc",
]
_MACS = [
    "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512-etm@openssh.com",
    "umac-128-etm@openssh.com", "hmac-sha1-etm@openssh.com",
    "hmac-sha2-256", "hmac-sha2-512", "umac-64@openssh.com",
    "hmac-sha1", "hmac-md5",
]
_COMPRESSION = ["none", "zlib@openssh.com", "zlib"]
SERVER_OFFER = {
    "kex_algorithms": [
        "mlkem768x25519-sha256",
        "sntrup761x25519-sha512", "sntrup761x25519-sha512@openssh.com",
        "curve25519-sha256", "curve25519-sha256@libssh.org",
        "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521",
        "diffie-hellman-group-exchange-sha256",
        "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512",
        "diffie-hellman-group14-sha256", "diffie-hellman-group14-sha1",
        "diffie-hellman-group-exchange-sha1", "diffie-hellman-group1-sha1",
        "ext-info-s", "kex-strict-s-v00@openssh.com",
    ],
    "server_host_key_algorithms": [
        "ssh-ed25519",
        "ecdsa-sha2-nistp256", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp521",
        "rsa-sha2-512", "rsa-sha2-256", "ssh-rsa", "ssh-dss",
    ],
    "encryption_algorithms_client_to_server": _CIPHERS,
    "encryption_algorithms_server_to_client": _CIPHERS,
    "mac_algorithms_client_to_server": _MACS,
    "mac_algorithms_server_to_client": _MACS,
    "compression_algorithms_client_to_server": _COMPRESSION,
    "compression_algorithms_server_to_client": _COMPRESSION,
    "languages_client_to_server": [],
    "languages_server_to_client": [],
}

# Protocol classes of _impls/*.md and the name-lists they come from. For
# the directional lists the client-to-server one is reported.
REPORTED = (
    ("cipher", "encryption_algorithms_client_to_server", "encryption_algorithms_server_to_client"),
    ("compression", "compression_algorithms_client_to_server", "compression_algorithms_server_to_client"),
    ("hostkey", "server_host_key_algorithms", None),
    ("kex", "kex_algorithms", None),
    ("mac", "mac_algorithms_client_to_server", "mac_algorithms_server_to_client"),
)

# _impls/*.md lists the server's strict-kex marker next to the client's: a
# client that sends one has to recognise the other.
STRICT_KEX_MARKERS = {
    "kex-strict-c-v00@openssh.com": "kex-strict-s-v00@openssh.com",
    "kex-strict-c": "kex-strict-s",
}


class ProtocolError(Exception):
    """The client sent something this server cannot use."""


# --- Wire format: SSH data types (RFC 4251 section 5) ------------------------

def encode_string(data: bytes) -> bytes:
    return struct.pack("!I", len(data)) + data


def encode_name_list(names: list[str]) -> bytes:
    return encode_string(",".join(names).encode("ascii"))


class Reader:
    """Reads SSH data types from a message payload."""

    def __init__(self, data: bytes):
        self._data = data
        self._pos = 0

    def take(self, n: int) -> bytes:
        if self._pos + n > len(self._data):
            raise ProtocolError("message truncated")
        chunk = self._data[self._pos:self._pos + n]
        self._pos += n
        return chunk

    def byte(self) -> int:
        return self.take(1)[0]

    def uint32(self) -> int:
        return struct.unpack("!I", self.take(4))[0]

    def string(self) -> bytes:
        return self.take(self.uint32())

    def name_list(self) -> list[str]:
        text = self.string().decode("ascii", errors="replace")
        return text.split(",") if text else []


# --- Transport: identification lines and unencrypted packets -----------------

class Transport:
    """RFC 4253 sections 4.2 and 6 over a socket, before any key exchange."""

    def __init__(self, sock: socket.socket):
        self._sock = sock
        self._file = sock.makefile("rb")

    def send_line(self, text: str) -> None:
        self._sock.sendall(text.encode("ascii") + b"\r\n")

    def read_line(self) -> bytes:
        line = self._file.readline(MAX_IDENT_LINE)
        if not line:
            raise ProtocolError("connection closed")
        return line.rstrip(b"\r\n")

    def send_packet(self, payload: bytes) -> None:
        # packet_length, padding_length, payload and padding together must
        # fill whole blocks, with at least MIN_PADDING bytes of padding
        padding = BLOCK_SIZE - (5 + len(payload)) % BLOCK_SIZE
        if padding < MIN_PADDING:
            padding += BLOCK_SIZE
        header = struct.pack("!IB", 1 + len(payload) + padding, padding)
        self._sock.sendall(header + payload + os.urandom(padding))

    def read_packet(self) -> bytes:
        packet_length, padding = struct.unpack("!IB", self._read_exact(5))
        if packet_length > MAX_PACKET_LENGTH or padding >= packet_length:
            raise ProtocolError(f"implausible packet length {packet_length}")
        body = self._read_exact(packet_length - 1)
        return body[:len(body) - padding]

    def _read_exact(self, n: int) -> bytes:
        data = self._file.read(n)
        if len(data) != n:
            raise ProtocolError("connection closed")
        return data


# --- Messages ----------------------------------------------------------------

@dataclass
class KexInit:
    name_lists: dict[str, list[str]]
    first_kex_packet_follows: bool = False
    reserved: int = 0

    @classmethod
    def parse(cls, payload: bytes) -> KexInit:
        r = Reader(payload)
        if r.byte() != SSH_MSG_KEXINIT:
            raise ProtocolError("not a KEXINIT")
        r.take(COOKIE_LENGTH)
        lists = {name: r.name_list() for name in NAME_LISTS}
        return cls(lists, bool(r.byte()), r.uint32())

    def encode(self) -> bytes:
        parts = [bytes([SSH_MSG_KEXINIT]), os.urandom(COOKIE_LENGTH)]
        parts += [encode_name_list(self.name_lists[name]) for name in NAME_LISTS]
        parts += [bytes([self.first_kex_packet_follows]), struct.pack("!I", self.reserved)]
        return b"".join(parts)


def encode_disconnect(reason: int, description: str) -> bytes:
    return (bytes([SSH_MSG_DISCONNECT]) + struct.pack("!I", reason)
            + encode_string(description.encode("utf-8")) + encode_string(b""))


# --- Probe: one client connection --------------------------------------------

@dataclass
class Record:
    peer: str
    time: datetime.datetime
    ident: str
    kexinit: KexInit


def read_client_ident(transport: Transport) -> str:
    # a peer may send other lines before its identification
    for _ in range(MAX_PREAMBLE_LINES):
        line = transport.read_line()
        if line.startswith(b"SSH-"):
            return line.decode("utf-8", errors="replace")
    raise ProtocolError("no SSH identification line")


def read_kexinit(transport: Transport) -> KexInit:
    while True:
        payload = transport.read_packet()
        if not payload:
            raise ProtocolError("empty packet")
        if payload[0] in (SSH_MSG_IGNORE, SSH_MSG_DEBUG):
            continue
        if payload[0] != SSH_MSG_KEXINIT:
            raise ProtocolError(f"expected KEXINIT, got message {payload[0]}")
        return KexInit.parse(payload)


def probe(sock: socket.socket, peer: str) -> Record:
    transport = Transport(sock)
    transport.send_line(SERVER_IDENT)
    ident = read_client_ident(transport)

    transport.send_packet(KexInit(SERVER_OFFER).encode())
    kexinit = read_kexinit(transport)

    transport.send_packet(encode_disconnect(
        SSH_DISCONNECT_BY_APPLICATION, "ssh-detect has recorded what this client offers"))
    return Record(peer, datetime.datetime.now(), ident, kexinit)


# --- Report ------------------------------------------------------------------

def format_record(rec: Record) -> str:
    lists = rec.kexinit.name_lists
    lines = [f"# ssh-detect {rec.time:%Y-%m-%d %H:%M:%S} from {rec.peer}", "protocols:"]

    for cls, c2s, s2c in REPORTED:
        lines.append(f"    {cls}:")
        # work around buggy clients that end a name-list with a comma,
        # against RFC 4251: drop the empty name, but say it was there
        for name in filter(None, lists[c2s]):
            lines.append(f"        - {name}")
            marker = STRICT_KEX_MARKERS.get(name)
            if marker and marker not in lists[c2s]:
                lines.append(f"        - {marker}  # implied by {name}")
        if "" in lists[c2s]:
            lines.append("        # the client sent an empty name, e.g. a trailing comma")
        if s2c and lists[s2c] != lists[c2s]:
            lines.append(f"        # server to client differs: {','.join(lists[s2c])}")

    for name in ("languages_client_to_server", "languages_server_to_client"):
        if lists[name]:
            lines.append(f"# {name}: {','.join(lists[name])}")
    if rec.kexinit.reserved:
        lines.append(f"# reserved field is {rec.kexinit.reserved}, should be 0")

    lines.append(f"first_kex_packet_follows: {int(rec.kexinit.first_kex_packet_follows)}")
    lines.append(f"ident: {json.dumps(rec.ident)}")  # a JSON string is a YAML string
    lines.append(f"# * {rec.time:%Y-%m-%d}: Version ? identifies itself on the wire as `{rec.ident}`")
    return "\n".join(lines) + "\n"


def record_filename(rec: Record) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", rec.ident)
    return f"{rec.time:%Y%m%d-%H%M%S}-{slug}.yml"


# --- Server ------------------------------------------------------------------

def log(message: str) -> None:
    print(f"{datetime.datetime.now():%H:%M:%S} {message}", file=sys.stderr, flush=True)


class ProbeHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        peer = "%s:%d" % self.client_address[:2]
        self.request.settimeout(SOCKET_TIMEOUT)
        log(f"{peer}: connected")
        try:
            rec = probe(self.request, peer)
        except (ProtocolError, OSError) as e:
            log(f"{peer}: {e or type(e).__name__}")
            return
        log(f"{peer}: recorded {rec.ident}")
        self.server.report(rec)


class ProbeServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, address, out_dir: str | None, once: bool):
        super().__init__(address, ProbeHandler)
        self.out_dir = out_dir
        self.once = once
        self._lock = threading.Lock()

    def report(self, rec: Record) -> None:
        text = format_record(rec)
        with self._lock:
            print(text, flush=True)
            if self.out_dir:
                path = os.path.join(self.out_dir, record_filename(rec))
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
                log(f"wrote {path}")
        if self.once:
            threading.Thread(target=self.shutdown).start()


def primary_address() -> str:
    # connecting a UDP socket sends nothing; it only picks the route
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("192.0.2.1", 9))
            return s.getsockname()[0]
        except OSError:
            return "127.0.0.1"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0].strip())
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--bind", default="0.0.0.0", help="address to listen on (default: all)")
    parser.add_argument("--out", metavar="DIR", help="also write each record to a file in DIR")
    parser.add_argument("--once", action="store_true", help="exit after the first record")
    args = parser.parse_args()

    if args.out:
        os.makedirs(args.out, exist_ok=True)

    with ProbeServer((args.bind, args.port), args.out, args.once) as server:
        port = server.server_address[1]
        host = primary_address() if args.bind == "0.0.0.0" else args.bind
        log(f"listening on {args.bind}:{port}; point clients at {host} port {port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
