---
title: cryptlib
homepage: http://www.cryptlib.com
#source-repository: TODO
license: "[Dual license: Sleepycat or commercial](http://www.cryptlib.com/security-software/licensing)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 3.4.2
    date: 2012-12-17
#changelog: TODO
client: yes
server: yes
library: both
protocols:
    cipher:
        - aes128-cbc
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ssh-rsa
        - ssh-dss
    kex:
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha1
    userauth:
        - publickey
        - password
        - keyboard-interactive
---
* Client and server library written in C.
