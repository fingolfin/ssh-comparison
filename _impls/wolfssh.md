---
title: wolfSSH
homepage: https://www.wolfssl.com/products/wolfssh/
source-repository: https://github.com/wolfSSL/wolfssh
license: "Dual license: [GPLv3](https://github.com/wolfSSL/wolfssh/blob/master/LICENSING) or [commercial](https://www.wolfssl.com/license/)"
first-release:
    date: 2016-10-24
latest-release:
    version: 1.4.17
    date: 2024-03-25
changelog: https://github.com/wolfSSL/wolfssh/blob/master/ChangeLog.md
client: yes
server: yes
library: both

protocols:
    cipher:
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-gcm@openssh.com
        - aes192-gcm@openssh.com
        - aes256-gcm@openssh.com
    compression:
        - none
    hostkey:
        - ssh-rsa
        - rsa-sha2-256
        - rsa-sha2-512
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - x509v3-ssh-rsa
        - x509v3-ecdsa-sha2-nistp256
        - x509v3-ecdsa-sha2-nistp384
        - x509v3-ecdsa-sha2-nistp521
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha256
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - ecdh-nistp256-kyber-512r3-sha256-d00@openquantumsafe.org
        - ext-info-c
    mac:
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha2-256
    userauth:
        - password
        - publickey
    extension:
        - server-sig-algs
---
* Lightweight ANSI C library using [wolfCrypt](https://www.wolfssl.com/products/wolfcrypt/).
