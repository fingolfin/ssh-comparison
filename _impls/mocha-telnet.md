---
# SSH-2.0-1.0.00
# waits for server to send KEX packet
title: Mocha Telnet (iOS)
redirect_from: /impls/moccha-telnet.html
# I tested "Mocca Telnet Lite"
homepage: http://www.mochasoft.dk/iphone_telnet.htm
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 5.8
    date: 2026-10-20
changelog: https://www.mochasoft.dk/iphone_telnet_release.htm
client: true
server: false
standalone: client
library: no
platforms:
    - ios

# TODO: add more versions 
protocols:
    cipher:
        - aes128-ctr
        #- 3des-cbc     # not offered by 5.8
    compression:
        - none
    hostkey:
        - rsa-sha2-256
        #- ssh-dss      # replaced by ssh-rsa in 3.3
        #- ssh-rsa      # since 3.3, not offered by 5.8
    kex:
        - mlkem768x25519-sha256         # since 5.7
        #- diffie-hellman-group14-sha256 # since 4.3, not offered by 5.8
        #- diffie-hellman-group1-sha1   # not offered by 5.8
    mac:
        - hmac-sha2-256 # since 5.1
        #- hmac-sha1    # not offered by 5.8
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
* 2026-11-21: Version 5.8 of Telnet Lite identifies itself on the wire as
  `SSH-2.0-1.0.00` and offers one algorithm of each kind.
