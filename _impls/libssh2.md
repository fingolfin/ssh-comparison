---
title: libssh2
homepage: https://libssh2.org/
source-repository: https://github.com/libssh2/libssh2
license: "[BSD style](https://libssh2.org/license.html)"
first-release:
    date: 2004-12-08    # version 0.1, initial release, date from repository
latest-release:
    version: 1.11.0
    date: 2023-05-30
changelog: https://libssh2.org/changes.html
client: yes
server: no
library: client

protocols:
    cipher:
        - aes128-ctr    # not documented; enabled if using OpenSSL >= 0.9.7, or libgcrypt, but not with Windows CNG
        - aes192-ctr    # not documented; enabled if using OpenSSL >= 0.9.7, or libgcrypt, but not with Windows CNG
        - aes256-ctr    # not documented; enabled if using OpenSSL >= 0.9.7, or libgcrypt, but not with Windows CNG
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - arcfour128
        - arcfour
        - cast128-cbc
        - 3des-cbc
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
    compression:
        - zlib
        - zlib@openssh.com  # added in 1.4.3
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - rsa-sha2-256
        - rsa-sha2-512
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - sk-ecdsa-sha2-nistp256@openssh.com
        - sk-ssh-ed25519@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com
        - sk-ssh-ed25519-cert-v01@openssh.com
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ext-info-c
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
    userauth:
        - password
        - publickey
        - hostbased
        - keyboard-interactive
    extension:
        - server-sig-algs
---
* C library for clients.
* Not to be confused with the unrelated [libssh](/impls/libssh.html)
