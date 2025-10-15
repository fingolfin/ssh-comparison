---
title: Maverick Synergy
homepage: https://jadaptive.com/java-ssh-library/
source-repository: https://github.com/sshtools/maverick-synergy
license: "[LGPL 3](https://github.com/sshtools/maverick-synergy/blob/master/LICENSE)"
first-release:
    date: 2004-02-12
latest-release:
    version: 3.1.2
    date: 2024-10-15
changelog: "https://github.com/sshtools/maverick-synergy/blob/master/maverick-synergy-assembly/notes/CHANGES"
client: yes
server: yes
library: both
protocols:
    cipher:
        - 3des-cbc
        - 3des-ctr
        - blowfish-cbc
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - arcfour
        - arcfour128
        - arcfour256
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - ssh-dss
        - ssh-ed25519
        - ssh-ed448
        - ssh-rsa
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-ed25519-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - x509v3-sign-dss
        - x509v3-ssh-dss
        - x509v3-ecdsa-sha2-nistp256
        - x509v3-ecdsa-sha2-nistp384
        - x509v3-ecdsa-sha2-nistp521
        - x509v3-rsa2048-sha256
        - x509v3-sign-rsa
        - x509v3-ssh-rsa
        - x509v3-sign-rsa-sha1
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - rsa1024-sha1
        - rsa2048-sha256
        - ext-info-c
        - ext-info-s
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha1
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-etm@openssh.com
        - hmac-md5-96
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-256-96
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-512-96
        - hmac-ripemd160
        - hmac-ripemd160-etm@openssh.com
    userauth:
        - password
        - publickey
        - keyboard-interactive
    extension:
        - server-sig-algs
---
* A pure Java implementation of the SSH2 protocol.
