---
title: ConnectBot
homepage: https://connectbot.org/
source-repository: https://github.com/connectbot/connectbot/
#developer: NAME
license: "[Apache-2.0](https://github.com/connectbot/connectbot/blob/master/LICENSE)"
first-release:
    date: 2007-11   # according to Wikipedia
latest-release:
    version: 1.8.6
    date: 2015-08-28
#changelog: URL
client: yes
server: no
library: no
platforms:
    - android
protocols:
    cipher:
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - blowfish-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - 3des-ctr
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-rsa
        - ssh-dss
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1-96
        - hmac-sha1
        - hmac-md5-96
        - hmac-md5
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: " SSH-2.0-TrileadSSH2Java_213"
based-on: "Trilead SSH-2"
---
* Android client
* Available on [Google Play](https://play.google.com/store/apps/details?id=org.connectbot)
