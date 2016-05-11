---
title: Serverauditor (Chrome)
homepage: https://serverauditor.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 0.300.2
    date: 2016-04-05
#changelog: TODO
client: yes
server: no
platforms:
    - chrome
# has cloud service for account sync
protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-gcm
        - aes128-gcm@openssh.com
        - aes256-gcm
        - aes256-gcm@openssh.com
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - 3des-cbc
        - arcfour256
        - arcfour128
        - cast128-cbc
        - arcfour
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - ssh-rsa
        - ssh-dss
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5
        - hmac-sha2-256-96
        - hmac-sha2-512-96
        - hmac-ripemd160
        - hmac-sha1-96
        - hmac-md5-96
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-ssh2js0.1.1"
#based-on: ssh2js
---
* Client for Google Chrome.
* There is also an [Android version](/impls/serverauditor-android.html)
  and an [iOS version](/impls/serverauditor-ios.html).
* Available on the
  [Google Chrome web store](https://chrome.google.com/webstore/detail/serverauditor-ssh-client/fjcdjmmkgnkgihjnlbgcdamkadlkbmam?utm_source=chrome-ntp-icon).
* 2015-12-05: Version 0.200.4 for Chrome identifies itself on the wire
  as `SSH-2.0-ParamikoJS_0.0.1`, so likely based on
  [paramikojs](https://github.com/mimecuvalo/paramikojs),
  a JavaScript port of Paramiko.
* 2016-05-03: Version 0.300.2 for Chrome identifies itself on the wire
  as `SSH-2.0-ssh2js0.1.1`.
