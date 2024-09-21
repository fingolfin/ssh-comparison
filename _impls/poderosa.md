---
title: Poderosa
homepage: https://poderosa.sourceforge.net/
source-repository: https://github.com/poderosaproject/poderosa
license: "[Apache-2.0](https://github.com/poderosaproject/poderosa/blob/master/LICENSE.txt)"
#first-release:
#    date: YYYY-MM-DD
#   version 3.0.0 on SourceForge.net ist dated 2005-04-28
latest-release:
    version: 4.7.0
    date: 2024-08-20
changelog: https://github.com/poderosaproject/poderosa/blob/master/ChangeLog.txt
client: yes
server: no
library: no
platforms:
    - windows

protocols:
    cipher:
        - aes256-gcm@openssh.coom
        - AEAD_AES_256_GCM
        - aes128-gcm@openssh.coom
        - AEAD_AES_128_GCM
        - aes256-ctr
        - aes256-cbc
        - aes192-ctr
        - aes192-cbc
        - aes128-ctr
        - aes128-cbc
        - blowfish-cbc
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-dss
        - ssh-rsa
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - rsa-sha2-256
        - rsa-sha2-512
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256@libssh.org
        - curve25519-sha256
        - curve448-sha512
        - ext-info-c
    mac:
        - AEAD_AES_256_GCM
        - AEAD_AES_128_GCM
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
    userauth:
        - password
        - publickey
        - keyboard-interactive
    extension:
        - server-sig-algs

first_kex_packet_follows: 0
ident: "SSH-2.0-Granados-2.0"
---
