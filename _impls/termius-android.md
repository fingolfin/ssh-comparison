---
title: Termius (Android)
redirect_from: /impls/serverauditor-android.html
homepage: https://termius.com/
license: Proprietary
first-release:
    no-later-than: 2012-11-21    # serverauditor.com links to the Play listing, web.archive.org/web/20121121190830/http://www.serverauditor.com/
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

help-wanted: The protocol data is from version 2.2.15 (2016). Current
    builds use libssh2, not JSch, and have never been measured.

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
    userauth:   # per docs.termius.com/keychain/identities
        - password
        - publickey

first_kex_packet_follows: 0
---
* Mobile client for Android.
* There is also an [iOS version](/impls/termius-ios.html).
* Available on
  [Google Play](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client).
* Formerly named Serverauditor.
* 2015-12-05: Version 2.1 for Android identifies itself on the wire
  as `SSH-2.0-JSCH-0.1.52`
* 2016-05-11: Version 2.2.15 for Android identifies itself on the wire
  as `SSH-2.0-JSCH-0.1.53`. The protocol data is from that version.
* The [changelog](https://docs.termius.com/changelog/android) of 7.7.0
  patches libssh2, so current builds no longer use JSch; they have not
  been measured. Termius documents
  [ML-KEM and ML-DSA](https://docs.termius.com/security/post-quantum-cryptography).
