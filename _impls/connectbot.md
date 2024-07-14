---
title: ConnectBot
homepage: https://connectbot.org/
source-repository: https://github.com/connectbot/connectbot
developer: Kenny Root
license: "[Apache-2.0](https://github.com/connectbot/connectbot/blob/main/LICENSE)"
first-release:
    date: 2007-11   # according to Wikipedia
latest-release:
    version: 1.9.10
    date: 2023-12-20
changelog: https://github.com/connectbot/connectbot/blob/main/CHANGELOG.md
client: yes
server: no
library: client
platforms:
    - android
protocols:
    cipher:
        - aes256-ctr
        - aes128-ctr
        - blowfish-ctr
        - aes256-cbc
        - aes128-cbc
        - blowfish-cbc
        - 3des-ctr
        - 3des-cbc
    compression:
        - none
        - zlib@openssh.com
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-ed25519
        - ssh-rsa
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group18-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
    userauth:
        - keyboard-interactive
        - password
        - publickey
    extension:
        - server-sig-algs

first_kex_packet_follows: 0
ident: " SSH-2.0-TrileadSSH2Java_213"
based-on: "Trilead SSH-2"
---
* Android client
* Available on [Google Play](https://play.google.com/store/apps/details?id=org.connectbot)
* Java library used is available separately on [GitHub](https://github.com/connectbot/sshlib)
