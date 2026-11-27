---
title: iTerminal
homepage: http://www.comcsoft.com/Portfolio/our_apps/iTerminal/iTerminal_overview.php
license: Proprietary
first-release:
    date: 2013-01-07    # App Store releaseDate, itunes.apple.com/lookup?id=581455211
latest-release:
    version: 10.0
    date: 2025-10-22
#changelog: TODO
client: yes
server: no
standalone: client
library: no
platforms:
    - ios

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
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
    userauth:   # per the App Store description
        - password
        - publickey

first_kex_packet_follows: 0
ident: "SSH-2.0-libssh2_1.10.0"
based-on: "[libssh2](/impls/libssh2.html)"
---
* Client for Apple iOS (iPhone, iPod, iPad).
* Available on the Apple App Store in two versions:
   [iTerminal](https://apps.apple.com/us/app/id581455211),
   [iTerminal Pro](https://apps.apple.com/us/app/id586842129)
* 2015-10-30: Version 2.02 identifies itself on the wire as `SSH-2.0-libssh2_1.4.3`
* 2016-02-19: Version 4.0 identifies itself on the wire as `SSH-2.0-libssh2_1.4.3`
* 2026-11-21: Version 10.0 identifies itself on the wire as `SSH-2.0-libssh2_1.10.0`
