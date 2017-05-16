---
title: Thrussh
homepage: http://pijul.org/thrussh
source-repository: https://nest.pijul.com/pijul_org/thrussh
license: "[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)"
first-release:
    date: 2016-07-01
latest-release:
    version: 0.10.3
    date: 2017-05-07
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
    compression:
        - none
    hostkey:
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-ed25519                       # since 6.5
    kex:
        - curve25519-sha256@libssh.org      # since 6.5
        - ecdh-sha2-nistp256                # since 5.7
    mac:
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - hostbased

---
* Multiplatform Rust library for clients and servers.
