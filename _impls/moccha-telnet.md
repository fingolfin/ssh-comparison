---
# SSH-2.0-1.0.00
# waits for server to send KEX packet
title: Mocca Telnet (iOS)
# I tested "Mocca Telnet Lite"
homepage: http://www.mochasoft.dk/iphone_telnet.htm
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 3.1
    date: 2016-02-19
#changelog: TODO
client: true
server: false
platforms:
    - iphone
    - ipad

# TODO: add more versions 
protocols:
    cipher:
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-dss
    kex:
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha1
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-1.0.00"
---
* Multi-platform client, with versions for Android, iOS, and more.
* The tests here were done with "Mocca Telnet Lite" on an iPhone
* Available on Apple app store:
  * [Mocha Telnet](https://itunes.apple.com/us/app/id286892932)
  * [Telnet Lite](https://itunes.apple.com/us/app/id286893976)

* 2015-07-10: Version 2.7 for iOS identifies itself on the wire as `SSH-2.0-1.0.00`.
