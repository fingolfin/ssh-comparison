---
title: Reflection for UNIX, Android Edition
homepage: https://www.attachmate.com/products/reflection/unix/
license: Proprietary
first-release:
    date: 2005  # according to Wikipedia
latest-release:
    version: 1.5.0.62
    date: 2015-09-25
#changelog: TODO
client: yes
server: no
platforms:
    - android
#
# TODO: They also have a client / server for Unix and Windows, called
#  Reflection for Secure IT (formerly F-Secure SSH), see
#   https://www.attachmate.com/products/reflection-security-it/
#
# https://www.attachmate.com/library/docs/reflection-for-secure-it-client-for-unix.html
# https://www.attachmate.com/library/docs/reflection-for-secure-it-client-for-windows-tech-specs.html
# https://www.attachmate.com/library/docs/reflection-for-secure-it-server-for-unix-tech-specs.html
# https://www.attachmate.com/library/docs/reflection-for-secure-it-server-for-windows-tech-specs.html
#
#
# Beyond that, they even have a "web client"?

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
based-on: "[libssh2](/impls/libssh2.html)"
---
* Mobile client for Android.
* There is also an [iOS version](/impls/reflection-ios.html).
* Available on
    [Google Play](https://play.google.com/store/apps/details?id=rTablet.Android&hl=en).
* They also offer clients and servers for Unix and Windows, under the name Reflection for Secure IT
  (formerly known as F-Secure SSH). These should be covered by a separate entry.
* 2015-12-05: Version 1.5.0.62 identifies itself on the wire as `SSH-2.0-libssh2_1.4.3`
