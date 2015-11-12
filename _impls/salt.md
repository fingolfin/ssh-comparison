---
layout: impl

title: salt
homepage: http://www.hekkelman.com/salt.html
#source-repository: URL
developer: Hekkelman Programmatuur
license: Proprietary
first-release:
    date: 2011-11   # according to Wikipedia
latest-release:
    version: 3.4.10
    date: 2015-05-12
#changelog: URL
client: yes
server: no
library: no
remarks: |
    * Windows client
protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - blowfish-cbc
        - 3des-cbc
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
    kex:
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha1
        - hmac-md5
    userauth:
        - keyboard-interactive
        - publickey
---
