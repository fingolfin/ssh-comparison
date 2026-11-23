---
title: Wardterm
homepage: https://wardterm.com
license: Proprietary
first-release:
    date: 2026-11-13
latest-release:
    version: 1.0.16
    date: 2026-11-22
client: yes
server: no
platforms:
    - macos
    - linux
    - android
    - iphone
    - ipad

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-gcm@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
    kex:
        - mlkem768x25519-sha256
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group18-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group15-sha512
        - diffie-hellman-group14-sha256
        - ext-info-c
        - kex-strict-c-v00@openssh.com
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-256
    userauth:
        - publickey
        - password
        - keyboard-interactive
first_kex_packet_follows: 0
ident: "SSH-2.0-russh_0.65.0"
based-on: "[Russh](/impls/russh.html)"
---
* Client for macOS, Linux, Android, iOS and iPadOS.
* Lists are in the order the client offers them by default. A per-server setting can require `mlkem768x25519-sha256` alone, or leave it out for servers that misbehave when it is offered.
* Host key algorithms the client already knows for a server move to the front of the list.
