---
title: lsh
homepage: http://www.lysator.liu.se/~nisse/lsh/
source-repository: http://git.lysator.liu.se/lsh
license: "[GPL 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0)"
first-release:
    date: 1999-05-23    # according to git tag lsh_0.1_release_19990523
latest-release:
    version: 2.1
    date: 2013-06-26
client: yes
server: yes
remarks: |
    * [Wikipedia](https://en.wikipedia.org/wiki/Lsh)
    * 2015-07-10: The version history mentions an experimental 2.9, but does NOT mention the
      actual release 2.1, which seems to be newer than the experimental 2.9 release.

protocols:
    cipher:
        - aes256-cbc
        - 3des-cbc
        - blowfish-cbc
        - arcfour
        - aes256-ctr                    # disabled by default
        - twofish-cbc                   # disabled by default
        - cast128-cbc                   # disabled by default
        - serpent256-cbc                # disabled by default
        #- serpent-cbc@lysator.liu.se    # disabled by default; non-standard
    compression:
        - none
        - zlib
    hostkey:
        - ssh-rsa
        - ssh-dss
        - spki-sign-rsa
        - spki-sign-dss
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
    mac:
        - hmac-sha1
        - hmac-md5
    userauth:
        - publickey
        - password
        - hostbased
        - keyboard-interactive

first_kex_packet_follows: 0
---
