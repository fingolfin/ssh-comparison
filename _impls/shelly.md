---
title: Shelly
homepage: https://apps.apple.com/us/app/id989642999
license: Proprietary
first-release:
    date: 2016-06-11
latest-release:
    version: 1.4.6
    date: 2026-03-31
client: yes
server: no
platforms:
    - iphone
    - ipad

protocols:
    cipher:
        - aes256-ctr
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes192-ctr
        - aes192-cbc
        - aes128-ctr
        - aes128-cbc
        - chacha20-poly1305@openssh.com
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - 3des-ctr
        - 3des-cbc
        - blowfish-ctr
        - blowfish-cbc
        - arcfour256
        - arcfour128
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - ssh-ed25519
        - ssh-ed448
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
        - ssh-dss
    kex:
        - sntrup761x25519-sha512@openssh.com
        - curve448-sha512
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - rsa2048-sha256
        - rsa1024-sha1
        - diffie-hellman-group1-sha1
        - ext-info-c
    mac:
        - hmac-sha2-256
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-etm@openssh.com
first_kex_packet_follows: 0
ident: "SSH-2.0-PuTTY_Release_0.78"
based-on: "[PuTTY](/impls/putty.html)"
---
* Client for Apple iOS (iPhone, iPad).
* Available on the [Apple App Store](https://apps.apple.com/us/app/id989642999).
* 2026-11-21: Version 1.4.6 identifies itself on the wire as `SSH-2.0-PuTTY_Release_0.78`.
