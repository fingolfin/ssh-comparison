---
title: ConnectBot
homepage: https://connectbot.org/
source-repository: https://github.com/connectbot/connectbot
developer: Kenny Root
license: "[Apache-2.0](https://github.com/connectbot/connectbot/blob/main/LICENSE)"
first-release:
    date: 2007-11   # according to Wikipedia
latest-release:
    version: 1.12.0-alpha-3279
    date: 2026-11-02
changelog: https://github.com/connectbot/connectbot/blob/main/CHANGELOG.md
client: yes
server: no
library: client
platforms:
    - android
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
        - aes256-ctr
        - aes128-ctr
        - aes256-cbc
        - aes128-cbc
        - 3des-cbc
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - sk-ssh-ed25519@openssh.com
        - sk-ecdsa-sha2-nistp256@openssh.com
        - sk-ssh-ed25519-cert-v01@openssh.com
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ssh-mldsa44-ed25519
        - ssh-mldsa87-p384
        - ssh-mldsa-44
        - ssh-mldsa-65
        - ssh-mldsa-87
        - ssh-ed448
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-ed25519
        - ssh-rsa
    kex:
        - mlkem768x25519-sha256
        - mlkem768nistp256-sha256
        - mlkem1024nistp384-sha384
        - mlkem768-sha256
        - mlkem1024-sha384
        - sntrup761x25519-sha512
        - sntrup761x25519-sha512@openssh.com
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group18-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - ext-info-c
        - kex-strict-c-v00@openssh.com
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
    userauth:
        - keyboard-interactive
        - password
        - publickey
        - publickey-hostbound-v00@openssh.com
    extension:
        - ext-info-in-auth@openssh.com
        - ping@openssh.com
        - publickey-hostbound@openssh.com
        - server-sig-algs

first_kex_packet_follows: 0
ident: "SSH-2.0-CBSSH_1.0"
---
* Android client
* Available on [Google Play](https://play.google.com/store/apps/details?id=org.connectbot)
* The SSH client library is developed and released separately as [cbssh](https://github.com/connectbot/cbssh).
* Algorithm support listed here is based on [cbssh v0.6.7](https://github.com/connectbot/cbssh/tree/v0.6.7), released 2026-10-27. The ConnectBot app has its own release version shown above.
