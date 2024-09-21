---
title: SwiftNIO SSH
homepage: https://github.com/apple/swift-nio-ssh/
source-repository: https://github.com/apple/swift-nio-ssh
license: "[Apache-2.0](https://github.com/apple/swift-nio-ssh/blob/main/LICENSE.txt)"
first-release:
    date: 2020-04-14
latest-release:
    version: 0.9.0
    date: 2024-03-26
changelog: https://github.com/apple/swift-nio-ssh/releases
client: yes
server: yes
library: both

protocols:
    cipher:
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
    compression:
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - curve25519-sha256@libssh.org
    mac:
        # no MACs actually supported since only AEAD ciphers are implemented
    userauth:
        - password
        - publickey
        - hostbased
---
* SwiftNIO SSH library
