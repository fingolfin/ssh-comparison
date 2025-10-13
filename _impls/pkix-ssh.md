---
title: PKIX-SSH
homepage: https://roumenpetrov.info/secsh/
source-repository: https://gitlab.com/secsh/pkixssh
license: "[BSD](https://gitlab.com/secsh/pkixssh/-/blob/master/LICENCE)"
first-release:
    date: 2002-04-04
latest-release:
    version: 17.1.2
    date: 2025-10-11
changelog: https://roumenpetrov.info/secsh/#news
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - aes128-cbc
        - 3des-cbc
        - aes192-cbc
        - aes256-cbc
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - x509v3-ecdsa-sha2-nistp256
        - x509v3-ecdsa-sha2-nistp384
        - x509v3-ecdsa-sha2-nistp521
        - x509v3-rsa2048-sha256
        - x509v3-ssh-rsa
        - x509v3-sign-rsa
        - x509v3-ssh-ed25519
        - x509v3-ssh-dss                    # disabled by ddefault
        - x509v3-sign-dss                   # disabled by ddefault
        - rsa-sha2-256
        - rsa-sha2-512
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com      # disabled by default
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - ssh-rsa
        - ssh-dss                           # disabled by default
    kex:
        - curve448-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group15-sha512
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
        - sntrup761x25519-sha512@openssh.com
        - sntrup761x25519-sha512
        - mlkem768x25519-sha256
        - mlkem768nistp256-sha256
        - mlkem1024nistp384-sha384
    mac:
        - umac-64-etm@openssh.com
        - umac-128-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - umac-64@openssh.com
        - umac-128@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - hostbased
    extension:
        - server-sig-algs

first_kex_packet_follows: 0
based-on: "[OpenSSH](/impls/openssh.html)"
---
* Fork of OpenSSH that adds X.509v3 certificate support.
