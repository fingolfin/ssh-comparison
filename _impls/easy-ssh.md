---
title: Easy SSH
homepage: https://apps.apple.com/us/app/id6742807404
developer: Argsment Limited
license: Proprietary
first-release:
    date: 2025-03-10
latest-release:
    version: 1.16
    date: 2026-07-19
client: yes
server: no
standalone: client
library: no
platforms:
    - ios

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes192-cbc
        - aes128-cbc
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
        - rsa-sha2-512
        - rsa-sha2-256
        - rsa-sha2-512-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - ssh-rsa
        - ssh-rsa-cert-v01@openssh.com
    kex:
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
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
    extension:
        - server-sig-algs   # as in libssh2
    userauth:   # per the app's host settings
        - password
        - publickey
first_kex_packet_follows: 0
ident: "SSH-2.0-libssh2_1.11.1"
based-on: "[libssh2](/impls/libssh2.html)"
---
* Client for Apple iOS (iPhone, iPad).
* Available on the [Apple App Store](https://apps.apple.com/us/app/id6742807404);
  called Locker SSH in the German store.
* 2026-11-21: Version 1.16 identifies itself on the wire as `SSH-2.0-libssh2_1.11.1`.
