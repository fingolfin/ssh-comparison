---
layout: impl

title: Serverauditor for iOS
homepage: https://serverauditor.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 2.2.1
    date: 2015-09-16
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
based-on: libssh2
---
### Remarks

* Mobile client for iOS (iPhone, iPad).
* There is also an [Android version](/impls/serverauditor-android.html)
  and a [Google Chrome plugin](/impls/serverauditor-chrome.html).
* Available at the
  [Apple App Store](https://itunes.apple.com/us/app/id549039908).
* 2015-12-05: Version 2.2.1 for iOS identifies itself on the wire as `SSH-2.0-libssh2_1.4.3`, so likely based on [libssh2](/impls/libssh2.html).
