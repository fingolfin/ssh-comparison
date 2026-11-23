---
title: ServerCat
homepage: https://servercat.app/
developer: Early Moon, LLC
license: Proprietary
first-release:
    date: 2020-04-27
latest-release:
    version: 26.11.2
    date: 2026-11-11
client: yes
server: no
platforms:
    - iphone
    - ipad

protocols:
    cipher:
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
        - aes128-ctr
        - aes128-ctr
        - aes128-ctr
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp521
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
    kex:
        - mlkem768x25519-sha256
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha256
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
    userauth:   # per the app's host settings
        - password
        - publickey
first_kex_packet_follows: 0
ident: "SSH-2.0-SwiftNIOSSH_1.0"
based-on: "[SwiftNIO SSH](/impls/swift-nio-ssh.html)"
---
* Client for Apple iOS (iPhone, iPad).
* Available on the [Apple App Store](https://apps.apple.com/us/app/id1501532023).
* 2026-11-21: Version 26.11.2 identifies itself on the wire as `SSH-2.0-SwiftNIOSSH_1.0`.
