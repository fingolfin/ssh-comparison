---
title: Russh
homepage: https://github.com/Eugeny/russh
source-repository: https://github.com/Eugeny/russh
license: "[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)"
first-release:
    date: 2022-03-13
latest-release:
    version: 0.57.0
    date: 2026-01-24
changelog: https://github.com/Eugeny/russh/releases
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - 3des-cbc
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-ed25519
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-rsa
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-dss
        - ssh-ed25519-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - mlkem768x25519-sha256
        - ext-info-c
        - ext-info-s
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
    extension:
        - server-sig-algs

based-on: "[Thrussh](/impls/thrussh.html)"
---
* Low-level Tokio SSH2 client and server implementation.
