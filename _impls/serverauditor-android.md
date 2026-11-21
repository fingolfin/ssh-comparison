---
title: Termius (Android)
homepage: https://termius.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 8.0.2
    date: 2026-11-19
changelog: https://docs.termius.com/changelog/android
client: yes
server: no
standalone: client
library: no
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
        - ssh-mldsa-44  # since 7.5.0, names per
        - ssh-mldsa-65  #  https://docs.termius.com/security/post-quantum-cryptography
        - ssh-mldsa-87
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
    kex:
        - mlkem768x25519-sha256 # since 7.2.2
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
* There is also an [iOS version](/impls/serverauditor-ios.html).
* Available on
  [Google Play](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client).
* Formerly named Serverauditor.
* 2015-12-05: Version 2.1 for Android identifies itself on the wire
  as `SSH-2.0-JSCH-0.1.52`
