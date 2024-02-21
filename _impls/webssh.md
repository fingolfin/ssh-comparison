---
title: WebSSH
homepage: https://www.webssh.net
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 13.1
    date: 2015-11-30
#changelog: TODO
client: yes
server: no
platforms:
    - iphone
    - ipad
protocols:
    cipher:
        - aes256-ctr
        - aes128-ctr
        - aes256-cbc
        - aes128-cbc
        - twofish256-cbc
        - twofish128-cbc
        - blowfish-cbc
        - 3des-cbc
        - arcfour128
        - arcfour256
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-dss
        - ssh-rsa
    kex:
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha1
        - hmac-sha2-512
        - hmac-md5
        - hmac-ripemd160
    userauth:
        - keyboard-interactive
        - publickey
        - password
    extension:
        - kex-strict-c-v00@openssh.com  # since 24.8
        - kex-strict-s-v00@openssh.com  # since 24.8

first_kex_packet_follows: 0
ident: "SSH-2.0-PuTTY_Release_0.63"
based-on: "[PuTTY](/impls/putty.html)"
---
* Client for Apple iOS (iPhone, iPod, iPad).
* Available on the Apple App Store in two versions:
   [WebSSH Essential](https://itunes.apple.com/us/app/id958955657),
   [WebSSH Pro](https://itunes.apple.com/us/app/id497714887)
* 2015-07-10: Version 8.3.2 identifies itself on the wire as `SSH-2.0-PuTTY_Release_0.63`.
* 2015-12-05: Version 13.1 identifies itself on the wire as `SSH-2.0-PuTTY_Release_0.63`.
