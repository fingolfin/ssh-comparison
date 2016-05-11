---
title: Serverauditor (Android)
homepage: https://serverauditor.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 2.2.15
    date: 2016-05-03
#changelog: TODO
client: yes
server: no
platforms:
    - android
# has cloud service for account sync

protocols:
    cipher:
        - aes128-ctr
        - aes128-cbc
        - 3des-ctr
        - 3des-cbc
        - blowfish-cbc
        - aes192-ctr
        - aes192-cbc
        - aes256-ctr
        - aes256-cbc
    compression:
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha1-96
        - hmac-md5-96
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-JSCH-0.1.53"
based-on: "[JSch](/impls/jsch.html)"
---
* Mobile client for Android.
* There is also an [iOS version](/impls/serverauditor-ios.html)
  and a [Google Chrome plugin](/impls/serverauditor-chrome.html).
* Available on
  [Google Play](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client).
* 2015-12-05: Version 2.1 for Android identifies itself on the wire
  as `SSH-2.0-JSCH-0.1.52`
