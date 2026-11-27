---
title: Blink Shell
homepage: https://blink.sh/
developer: Blink Shell, Inc
source-repository: https://github.com/blinksh/blink
license: "[GPL-3.0](https://github.com/blinksh/blink/blob/raw/LICENSE)"
first-release:
    no-later-than: 2016-09-27    # README of commit d79dcea: "available on the AppStore"
latest-release:
    version: 18.7.3
    date: 2026-11-16
client: yes
server: no
standalone: client
library: no
platforms:
    - ios
languages:
    - Swift
    - Objective-C

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
        - sk-ssh-ed25519@openssh.com
        - sk-ecdsa-sha2-nistp256@openssh.com
        - rsa-sha2-512
        - rsa-sha2-256
    kex:
        - mlkem768x25519-sha256
        - mlkem768nistp256-sha256
        - mlkem1024nistp384-sha384
        - sntrup761x25519-sha512
        - sntrup761x25519-sha512@openssh.com
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group18-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha256
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
    userauth:   # per the app's host settings
        - password
        - publickey
first_kex_packet_follows: 0
ident: "SSH-2.0-libssh_0.12.0"
based-on: "[libssh](/impls/libssh.html)"
---
* Client for Apple iOS (iPhone, iPad).
* Available on the [Apple App Store](https://apps.apple.com/us/app/id1594898306).
* 2026-11-21: Version 18.7.3 identifies itself on the wire as `SSH-2.0-libssh_0.12.0`.
