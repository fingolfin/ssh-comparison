---
title: iTerminal
homepage: http://www.comcsoft.com/Portfolio/our_apps/iTerminal/iTerminal_overview.php
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 3.02
    date: 2015-12-01
#changelog: TODO
client: yes
server: no
platforms:
    - iphone
    - ipad

protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - arcfour128
        - arcfour
        - cast128-cbc
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-libssh2_1.4.3"
based-on: "[libssh2](/impls/libssh2.html)"
---
* Client for Apple iOS (iPhone, iPod, iPad).
* Available on the Apple App Store in three versions:
   [iTerminal](https://itunes.apple.com/us/app/id581455211),
   [iTerminal Pro for iPhone](https://itunes.apple.com/us/app/id787053466),
   [iTerminal Pro for Universal](https://itunes.apple.com/us/app/id586842129)
* 2015-10-30: Version 2.02 for iOS identifies itself on the wire as `SSH-2.0-libssh2_1.4.3`
