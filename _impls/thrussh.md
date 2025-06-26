---
title: Thrussh
homepage: http://pijul.org/thrussh
source-repository: https://nest.pijul.com/pijul/thrussh
license: "[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)"
first-release:
    date: 2016-07-01
latest-release:
    version: 0.35.6
    date: 2024-07-22
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-rsa
        - rsa-sha2-256
        - rsa-sha2-512
        - ecdsa-sha2-nistp256
        - ssh-ed25519
    kex:
        - curve25519-sha256@libssh.org
        - ext-info-c
        - ext-info-s
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - hostbased
    extension:
        - server-sig-algs

---
* Multiplatform Rust library for clients and servers.
