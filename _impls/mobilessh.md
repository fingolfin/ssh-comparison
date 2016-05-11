---
title: Mobile SSH
homepage: https://play.google.com/store/apps/details?id=mobileSSH.feng.gao
license: Proprietary
#first-release:
#    date: TODO
latest-release:
    version: 2.17
    date: 2016-04-23
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
ident: "SSH-2.0-Mobile_SSH_2.10:_Mar_22_2015_13:27:33"

based-on: "[OpenSSH](/impls/openssh.html)"
---
* Mobile client for Android.
* Available on
    [Google Play](https://play.google.com/store/apps/details?id=mobileSSH.feng.gao).
* Claims to be based on OpenSSH.
* The report given here is for the base version; a paid version exists
  which supposedly offers support for "RSA key authenticaation feature".
