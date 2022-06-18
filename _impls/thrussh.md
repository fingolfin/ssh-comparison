---
title: Thrussh
homepage: http://pijul.org/thrussh
source-repository: https://nest.pijul.com/pijul_org/thrussh
license: "[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)"
first-release:
    date: 2016-07-01
latest-release:
    version: 0.33.5
    date: 2021-07-06
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
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-ed25519
    kex:
        - curve25519-sha256@libssh.org
        #- ecdh-sha2-nistp256
    mac:
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - hostbased

---
* Multiplatform Rust library for clients and servers.
