---
title: vSSH
homepage: http://www.velestar.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 1.11
    date: 2015-10-22
#changelog: TODO
client: yes
server: no
#platforms:
#    - iphone
#    - ipad
# seems they also have versions for Android and Windows Phone, and also Mac OS X?
# Homepage is oddly outdated: last news item is from Nov 2014, 
#
# TODO: add app store links?!
remarks: |
    * Mobile client for Apple iOS (iPhone and iPad).
    * There are four versions for iOS available via the Apple app store:
        [vSSH Lite](https://itunes.apple.com/us/app/id535055496),
        [vSSH](https://itunes.apple.com/us/app/id527244258),
        [vSSH HD Lite](https://itunes.apple.com/us/app/id535056241),
        [vSSH HD](https://itunes.apple.com/us/app/id530136764).

    * Android:
        [Google Play](https://play.google.com/store/apps/details?id=com.velestar.vssh)

    * 2015-07-10: Version 1.9 for iOS identifies itself on the wire as `SSH-2.0-vSSH_2.0`.
    * 2015-10-30: Version 1.11 for iOS identifies itself on the wire as `SSH-2.0-vSSH_1.9`.
    * Version 1.11 is based on [PuTTY](/impls/putty.html) 0.65
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
---
