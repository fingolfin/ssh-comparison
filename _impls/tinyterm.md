---
title: TinyTERM for iOS
homepage: http://www.censoft.com/products/mobile/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 3.1.0
    date: 2015-09-23
#changelog: TODO
client: yes
server: no
#platforms:
#    - iphone
#    - ipad
# They also have clients for OS X, Windows, Android, Web, Linux, UNIX, ...
# supports many terminal types, and protocols beyond SSH
# The android clients have a different version, so I am not linking them here
remarks: |
    * There are multiple versions of this, for different platform: Windows, Android, Linux, iOS, Mac OS X, ...
    * This report is currently based on `TinyTERM Lite for iOS`
    * There are three versions for iOS available via the Apple app store:
        * [TinyTERM Lite](https://itunes.apple.com/us/app/id893250564)
        * [TinyTERM Enterprise AS](https://itunes.apple.com/us/app/id893366373)
        * [TinyTERM Plus](https://itunes.apple.com/us/app/id912491717)
    * Google Play has at least two versions (but their version numbers differ
       from the iOS versions; the Android version has not yet been tested by me)
        * [TinyTERM Lite](https://play.google.com/store/apps/details?id=com.censoft.TinyTERM.Lite)
        * [TinyTERM Plus](https://play.google.com/store/apps/details?id=com.censoft.TinyTERM.Plus)

    * 2015-07-10: Version 2.1.5 for iOS identifies itself on the wire as `SSH-2.0-libssh-0.5.5`, so likely based on [libssh](/impls/libssh.html).
    * 2015-10-30: Version 3.1.0 for iOS identifies itself on the wire as `SSH-2.0-libssh-0.7.0`, so likely based on [libssh](/impls/libssh.html).

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
---
