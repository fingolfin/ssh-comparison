---
title: libssh
homepage: https://www.libssh.org/
source-repository: https://git.libssh.org/projects/libssh.git
references:
    - https://api.libssh.org/stable/
license: "[LGPL 2.1](https://git.libssh.org/projects/libssh.git/tree/COPYING)"
first-release:
    date: 2003-09-03
# Looking at the initial commit in the git repository, it contains
# a CHANGELOG which contains the date of the initial release.
latest-release:
    version: 0.11.1
    date: 2024-08-30
changelog: https://git.libssh.org/projects/libssh.git/tree/CHANGELOG
client: yes
server: yes
library: both

# Note: internally, there are also ciphers des-cbc-ssh1 and 3des-cbc-ssh1.
# But according to the authors, these are only there for SSH v1 support.
# And indeed, a test program does not offer them during KEXINIT for v2
# connections.
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - 3des-cbc
    compression:
        - zlib             # disabled by default since 0.11.0
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-ed25519
        - ssh-ed25519-cert-v01@openssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - rsa-sha2-256
        - rsa-sha2-512
        - rsa-sha2-512-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - ssh-rsa
        - ssh-rsa-cert-v01@openssh.com
        #- ssh-dss                                    # removed in 0.11.0
        #- ssh-dss-cert-v01@openssh.com               # removed in 0.11.0
        - sk-ssh-ed25519@openssh.com                  # since 0.10.0, server side only
        - sk-ssh-ed25519-cert-v01@openssh.com         # since 0.10.0, server side only
        - sk-ecdsa-sha2-nistp256@openssh.com          # since 0.10.0, server side only
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com # since 0.10.0, server side only
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group18-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-256
        - hmac-sha1
    userauth:
        - password
        - publickey
        - hostbased
        - keyboard-interactive
        - gssapi-with-mic
    extension:
        - server-sig-algs
---
* Mulitplatform C library for clients and servers.
* Not to be confused with the unrelated [libssh2](/impls/libssh2.html)
