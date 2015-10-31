#!/usr/bin/env python2
#
# A minimalistic "server" which fakes an SSH connection exchange
# and logs the data sent by the client.
#
# TODO: also add a client version
# TODO: improve logging
#
# Hints on testing specific implementations:
#
# libssh2: edit example/ssh2.c to change the port from 22 to 10000; also insert
#    the following line right after the call to libssh2_session_init():
#       libssh2_session_flag(session, LIBSSH2_FLAG_COMPRESS, 1);
#    Then "make" and run example/ssh2

import socket
import sys
import struct


SSH_MSG_DISCONNECT            = 1
SSH_MSG_IGNORE                = 2
SSH_MSG_UNIMPLEMENTED         = 3
SSH_MSG_DEBUG                 = 4
SSH_MSG_SERVICE_REQUEST       = 5
SSH_MSG_SERVICE_ACCEPT        = 6
SSH_MSG_KEXINIT               = 20
SSH_MSG_NEWKEYS               = 21
SSH_MSG_KEXDH_INIT            = 30
SSH_MSG_KEXDH_REPLY           = 31

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


def read_uint32(f):
    data = f.read(4)
    return struct.unpack("!i", data)[0]

def read_byte(f):
    data = f.read(1)
    return struct.unpack("B", data)[0]

def write_uint32(f, val):
    f.write(struct.pack("!i", val))

def write_byte(f, val):
    f.write(struct.pack("B", val))


def hex_str(str):
    return ':'.join(x.encode('hex') for x in str)

def recv_namelist(f, title, vals):
    #print >>sys.stderr, 'Receiving name list: '
    len = read_uint32(f)
    #print >>sys.stderr, 'len = ', len
    data = f.read(len)
    #print >>sys.stderr, '%s: ' % title
    #print >>sys.stderr, '   %s' % data
    vals[title] = data.split(",")

def append_namelist(payload, str):
    payload.extend(struct.pack("!i", len(str)))
    payload.extend(str)

def print_list(title, vals):
    print "    %s:" % title
    for v in vals:
        print '        - %s' % v

try:
    while True:
        # Wait for a connection
        print >>sys.stderr, '=' * 60
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'connection from', client_address

            f = connection.makefile('r+')

            # Identify as an SSH 2.0 server
            print >>sys.stderr, 'sending SSH 2.0 identification'
            f.write("SSH-2.0-SSH_detector_0.1 comment\r\n")
            f.flush()

            # Read SSH client identification, plus extra fluff
            while not f.closed:
                line = f.readline()
                print >>sys.stderr, 'received "%s"' % line.strip()
                if line.startswith("SSH-"):
                    break


            #
            # Send a fake SSH_MSG_KEXINIT
            #
            print >>sys.stderr, ''
            print >>sys.stderr, 'sending fake SSH_MSG_KEXINIT'

            payload = bytearray([SSH_MSG_KEXINIT])
            payload.extend(bytearray(range(16)))   # cookie

            kex = "diffie-hellman-group14-sha1,curve25519-sha256@libssh.org,ecdh-sha2-nistp521"
            append_namelist(payload, kex)       # kex_algorithms

            hostkey = "ecdsa-sha2-nistp256,ssh-rsa"
            append_namelist(payload, hostkey)   # server_host_key_algorithms

            cipher = "aes128-cbc,aes128-ctr"
            append_namelist(payload, cipher)    # encryption_algorithms_client_to_server
            append_namelist(payload, cipher)    # encryption_algorithms_server_to_client

            mac = "hmac-sha2-512"
            append_namelist(payload, mac)       # mac_algorithms_client_to_server
            append_namelist(payload, mac)       # mac_algorithms_server_to_client

            append_namelist(payload, "zlib,zlib@openssh.com,none")    # compression_algorithms_client_to_server
            append_namelist(payload, "zlib,zlib@openssh.com,none")    # compression_algorithms_server_to_client
            append_namelist(payload, "")        # languages_client_to_server
            append_namelist(payload, "")        # languages_server_to_client
            payload.append(0)                   # boolean: first_kex_packet_follows
            payload.extend(bytearray([0,0,0,0]))  # uint32: reserved for future extension

            total_len = 4 + 1 + len(payload)
            padding_length = 16 - (total_len & 7)
            packet_length = len(payload) + padding_length + 1

            print >>sys.stderr, 'sending packet with len ', packet_length, ' and padding ', padding_length

            write_uint32(f, packet_length)
            write_byte(f, padding_length)
            f.write(payload)
            f.write(bytearray(range(padding_length)))   # padding
            # no MAC
            f.flush()


            print >>sys.stderr, 'waiting for SSH packet'
            packet_length = read_uint32(f)
            padding_length = read_byte(f)
            print >>sys.stderr, 'received packet with len ', packet_length, ' and padding ', padding_length

            #
            # Receive a SSH_MSG_KEXINIT message
            #
            msg = read_byte(f)

            if msg != SSH_MSG_KEXINIT:
                print >>sys.stderr, 'Error, expected SSH_MSG_KEXINIT but got ', msg
                continue

            print >>sys.stderr, 'received SSH_MSG_KEXINIT'
            cookie = f.read(16)
            print >>sys.stderr, 'cookie "%s"' % hex_str(cookie)
            # TODO

            vals = dict()
            recv_namelist(f, "kex_algorithms", vals)
            recv_namelist(f, "server_host_key_algorithms", vals)

            recv_namelist(f, "encryption_algorithms_client_to_server", vals)
            recv_namelist(f, "encryption_algorithms_server_to_client", vals)
            if vals["encryption_algorithms_client_to_server"] != vals["encryption_algorithms_server_to_client"]:
                print >>sys.stderr, 'WARNING: languages sets for c/s and s/c differ'

            recv_namelist(f, "mac_algorithms_client_to_server", vals)
            recv_namelist(f, "mac_algorithms_server_to_client", vals)
            if vals["mac_algorithms_client_to_server"] != vals["mac_algorithms_server_to_client"]:
                print >>sys.stderr, 'WARNING: languages sets for c/s and s/c differ'

            recv_namelist(f, "compression_algorithms_client_to_server", vals)
            recv_namelist(f, "compression_algorithms_server_to_client", vals)
            if vals["compression_algorithms_client_to_server"] != vals["compression_algorithms_server_to_client"]:
                print >>sys.stderr, 'WARNING: languages sets for c/s and s/c differ'

            recv_namelist(f, "languages_client_to_server", vals)
            recv_namelist(f, "languages_server_to_client", vals)
            if vals["languages_client_to_server"] != vals["languages_server_to_client"]:
                print >>sys.stderr, 'WARNING: languages sets for c/s and s/c differ'

            # TODO: validate the payload length so far

            # receive padding
            print >>sys.stderr, 'reading %d padding bytes' % padding_length
            if padding_length > 0:
                f.read(padding_length)

            #
            # Output everything
            #

            print "protocols:"
            print_list("cipher", vals["encryption_algorithms_client_to_server"])
            print_list("compression", vals["compression_algorithms_client_to_server"])
            print_list("hostkey", vals["server_host_key_algorithms"])
            print_list("kex", vals["kex_algorithms"])
            print_list("mac", vals["mac_algorithms_client_to_server"])

            # TODO: continue with fake useauth, to test support for different methods?
            print "#    userauth:"
            print "#        - unknown"

            # TODO: send a disconnect message

            print ""

        finally:
            f.close()
            connection.close()

finally:
    sock.close()
