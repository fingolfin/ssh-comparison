---
title: Go Cryptography
homepage: https://pkg.go.dev/golang.org/x/crypto/ssh
source-repository: https://cs.opensource.google/go/x/crypto
license: "[BSD style](https://cs.opensource.google/go/x/crypto/+/master:LICENSE)"
first-release:
    date: 2022-10-19
latest-release:
    version: 0.42.0
    date: 2025-09-08
#changelog: ?
client: yes
server: yes
library: both
protocols:
    cipher:
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-cbc
        - 3des-cbc
        - arcfour
        - arcfour128
        - arcfour256
    compression:
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - sk-ecdsa-sha2-nistp256@openssh.com
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - sk-ssh-ed25519@openssh.com
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - sk-ssh-ed25519-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - mlkem768x25519-sha256
        - curve25519-sha256@libssh.org
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha1-96
    userauth:
        - password
        - publickey
        - keyboard-interactive
        - gssapi-with-mic
    extension:
        - server-sig-algs
        - ping@openssh.com
---
* Go based implementation.
