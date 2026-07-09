---
title: cryptlib
homepage: https://cryptlib.com/
source-repository: https://github.com/cryptlib/cryptlib
license: "[Dual license: Sleepycat or commercial](https://github.com/cryptlib/cryptlib/blob/main/COPYING)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 3.4.9.3
    date: 2026-07-08
changelog: https://github.com/cryptlib/cryptlib/releases
client: yes
server: yes
library: both
protocols:
    cipher:
        - aes128-cbc
        - aes256-cbc
        - aes128-ctr
        - aes256-ctr
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ssh-rsa
        - rsa-sha2-256
        - ssh-dss
    kex:
        - curve25519-sha256
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - ext-info-c
    mac:
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha1
        - hmac-sha1-etm@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
    extension:
        - server-sig-algs
---
* Client and server library written in C.
