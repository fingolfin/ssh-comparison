---
title: Termphin
homepage: https://termphin.dev/
source-repository: https://github.com/Termphin/Termphin
license: "[GPL-3.0](https://github.com/Termphin/Termphin/blob/main/LICENSE)"
first-release:
    date: 2026-10-31
latest-release:
    version: 1.16.1
    date: 2026-11-21
changelog: https://github.com/Termphin/Termphin/releases
client: yes
server: no
platforms:
    - iphone
    - ipad

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-ctr
        - aes128-ctr
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - rsa-sha2-512
        - rsa-sha2-256
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha256
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
        - ext-info-c
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
first_kex_packet_follows: 0
ident: "SSH-2.0-DartSSH_2.0"
based-on: "[dartssh2](/impls/dartssh2.html)"
---
* Client for Apple iOS (iPhone, iPad).
* Available on the [Apple App Store](https://apps.apple.com/us/app/id6813191168).
* 2026-11-21: Version 1.15.1 identifies itself on the wire as `SSH-2.0-DartSSH_2.0`.
