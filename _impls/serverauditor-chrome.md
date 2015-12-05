---
title: Serverauditor for Chrome
homepage: https://serverauditor.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 0.200.4
    date: 2015-10-26
#changelog: TODO
client: yes
server: no
#platforms:
#    - chrome
# has cloud service for account sync
protocols:
    cipher:
        - blowfish-cbc
        - aes128-ctr
        - aes256-ctr
        - aes128-cbc
        - aes256-cbc
        - 3des-cbc
        - arcfour128
        - arcfour256
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
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-ParamikoJS_0.0.1"
based-on: paramikojs
---
### Remarks

* Client for Google Chrome.
* There is also an [Android version](/impls/serverauditor-android.html)
  and an [iOS version](/impls/serverauditor-ios.html).
* Available at the
  [Google Chrome web store](https://chrome.google.com/webstore/detail/serverauditor-ssh-client/fjcdjmmkgnkgihjnlbgcdamkadlkbmam?utm_source=chrome-ntp-icon).
* 2015-12-05: Version 2.1 for Chrome identifies itself on the wire
  as `SSH-2.0-ParamikoJS_0.0.1`, so likely based on
  [paramikojs](https://github.com/mimecuvalo/paramikojs),
  a JavaScript port of Paramiko.
