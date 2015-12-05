---
title: vSSH for Android
homepage: http://www.velestar.com/
license: Proprietary
first-release:
    date: 2012
latest-release:
    version: 1.4
    date: 2015-10-01
#changelog: TODO
client: yes
server: no
platforms:
    - android

protocols:
    cipher:
        - aes256-ctr
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes192-ctr
        - aes192-cbc
        - aes128-ctr
        - aes128-cbc
        - blowfish-ctr
        - blowfish-cbc
        - 3des-ctr
        - 3des-cbc
        - arcfour256
        - arcfour128
    compression:
        - none
        - zlib
    hostkey:
        - ssh-rsa
        - ssh-dss
    kex:
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - rsa2048-sha256
        - rsa1024-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-vSSH_1.9"
based-on: "[PuTTY](/impls/putty.html)"
---
* Mobile client for Android.
* There is also an [iOS version](/impls/vssh-ios.html).
* Available on
    [Google Play](https://play.google.com/store/apps/details?id=com.velestar.vssh)
* 2015-12-05: Version 1.4 for Android identifies itself on the wire as `SSH-2.0-vSSH_1.9`.
* Version 1.4 for iOS is based on [PuTTY](/impls/putty.html) 0.65 according to the
  "What's New" information on Google Play.
* Homepage is oddly outdated: last news item is from Nov 2014; yet they do make
  regular releases
