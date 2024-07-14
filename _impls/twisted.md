---
title: Twisted Conch
homepage: https://twisted.org/
source-repository: https://github.com/twisted/twisted
license: "[MIT](https://github.com/twisted/twisted/blob/trunk/LICENSE)"
first-release:
    date: 2002-07-07    # Conch renamed from twisted.secsh
latest-release:
    version: 2024.3.0
    date: 2024-03-01
changelog: https://github.com/twisted/twisted/blob/trunk/NEWS.rst
client: yes
server: yes
library: both
platforms:
    - linux
    - windows
    - macos
protocols:
    # https://github.com/twisted/twisted/blob/2a33824557ed65d2241a51d6bba07ac76521b50f/src/twisted/conch/ssh/transport.py#L95
    cipher:
        - 3des-cbc
        - 3des-ctr
        - blowfish-cbc
        - blowfish-ctr
        - cast128-cbc
        - cast128-ctr
        - aes128-cbc
        - aes192-ctr
        - aes256-cbc
        - aes128-ctr
        - aes192-cbc
        - aes256-ctr
        - none
    compression:
        - zlib
        - none
    # https://github.com/twisted/twisted/blob/2a33824557ed65d2241a51d6bba07ac76521b50f/src/twisted/conch/ssh/transport.py#L458
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256            # since 16.6.0
        - ecdsa-sha2-nistp384            # since 16.6.0
        - ecdsa-sha2-nistp521            # since 16.6.0
        - ssh-ed25519                    # since 21.2.0
        - rsa-sha2-256                   # since 22.4.0
        - rsa-sha2-512                   # since 22.4.0

    # See: https://github.com/twisted/twisted/blob/2a33824557ed65d2241a51d6bba07ac76521b50f/src/twisted/conch/ssh/_kex.py#L178
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - ext-info-c
        - ext-info-s
    # https://github.com/twisted/twisted/blob/2a33824557ed65d2241a51d6bba07ac76521b50f/src/twisted/conch/ssh/transport.py#L110
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-384
        - hmac-sha2-512
        - none
    userauth:
        - publickey
        - password
        - keyboard-interactive              # client-side only
    extension:
        - server-sig-algs                   # since 22.4.0

first_kex_packet_follows: 1
ident: "SSH-2.0-Twisted_2024.3.0"
---
* Designed as a [Python](https://www.python.org/) library.
* Cryptograpy provided by [cryptography](https://cryptography.io/) library, that provides bindings for [OpenSSL](https://www.openssl.org/) or [LibreSSL](https://www.libressl.org/)
* SFTP client and server.
* Source code and documentation contains example for creating a client and a server.
* [Wikipedia](https://en.wikipedia.org/wiki/Twisted_(software))
