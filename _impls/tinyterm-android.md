---
title: TinyTERM for Android
homepage: http://www.censoft.com/products/mobile/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 1.2.9
    date: 2015-09-16
#changelog: TODO
client: yes
server: no
platforms:
    - android

protocols:
    cipher:
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-libssh-0.7.0"
based-on: "[libssh](/impls/libssh.html)"
---
* There is also an [iOS version](/impls/tinyterm-ios.html),
  and also versions for Windows, Linux, Mac OS X, ...
* There are two versions available on Google Play:
    * [TinyTERM Lite](https://play.google.com/store/apps/details?id=com.censoft.TinyTERM.Lite)
    * [TinyTERM Plus](https://play.google.com/store/apps/details?id=com.censoft.TinyTERM.Plus)
* This report is based on `TinyTERM Lite`

* 2015-12-05: Version 1.2.9 identifies itself on the wire as `SSH-2.0-libssh-0.7.0`
