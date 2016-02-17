---
title: Poderosa
homepage: http://poderosa.sourceforge.net/
source-repository: https://github.com/poderosaproject/poderosa
license: "[Apache-2.0](https://github.com/poderosaproject/poderosa/blob/master/LICENSE.txt)"
#first-release:
#    date: YYYY-MM-DD
#   version 3.0.0 on SourceForge.net ist dated 2005-04-28
latest-release:
    version: 4.3.16
    date: 2015-08-03
#changelog: URL
client: yes
server: no
library: no
platforms:
    - windows

protocols:
    cipher:
        - aes256-ctr
        - aes256-cbc
        - aes192-ctr
        - aes192-cbc
        - aes128-ctr
        - aes128-cbc
        - blowfish-cbc
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-dss
        - ssh-rsa
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha1
    userauth:
        - password
        - publickey
        - keyboard-interactive

first_kex_packet_follows: 0
ident: "SSH-2.0-Granados-2.0"
---
