---
title: Termix
homepage: https://apps.apple.com/us/app/id6739386670
license: Proprietary
first-release:
    date: 2025-03-06
latest-release:
    version: 1.1.7
    date: 2026-07-30
client: yes
server: no
standalone: client
library: no
platforms:
    - ios

protocols:
    cipher:
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
        - aes128-ctr
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp521
        - ssh-rsa
        - rsa-sha2-256
        - rsa-sha2-512
    kex:
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
    mac:
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
    userauth:   # per the App Store description
        - password
        - publickey
first_kex_packet_follows: 0
ident: "SSH-2.0-SwiftNIOSSH_1.0"
based-on: "[SwiftNIO SSH](/impls/swift-nio-ssh.html)"
---
* Client for Apple iOS (iPhone, iPad).
* Available on the Apple App Store in two versions: [Termix](https://apps.apple.com/us/app/id6739386670), [Termix Pro](https://apps.apple.com/us/app/id6743685377).
* 2026-11-21: Version 1.1.7 identifies itself on the wire as `SSH-2.0-SwiftNIOSSH_1.0`.
