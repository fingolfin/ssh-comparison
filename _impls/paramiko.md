---
title: Paramiko
homepage: https://www.paramiko.org/
source-repository: https://github.com/paramiko/paramiko
license: "[LGPL 2.1](https://github.com/paramiko/paramiko/blob/master/LICENSE)"
first-release:
    date: 2003-09-13    # v0.1, according to NEWS file
latest-release:
    version: 3.5.0
    date: 2024-09-15
changelog: https://www.paramiko.org/changelog.html
client: yes
server: yes
library: both

protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr            # since 1.16.0 (2015-11-04)
        - aes256-ctr
        - aes128-cbc
        #- blowfish-cbc         # removed in 2.11.0
        - aes192-cbc            # since 1.16.0 (2015-11-04)
        - aes256-cbc
        - aes128-gcm@openssh.com # since 3.5.0
        - aes256-gcm@openssh.com # since 3.5.0
        - 3des-cbc
        #- arcfour128           # removed in 2.1.3
        #- arcfour256           # removed in 2.1.3
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256   # since 1.12.0 (2013-09-27)
        - ecdsa-sha2-nistp384   # since 2.0.0 (2016-04-28)
        - ecdsa-sha2-nistp521   # since 2.0.0 (2016-04-28)
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-ed25519
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1   # since 1.15.0 (2014-09-18)
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256  # since 1.16.0 (2015-11-04)
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256@libssh.org
        - gss-group1-sha1-*     # since 1.15.0 (2014-09-18)
        - gss-group14-sha1-*    # since 1.15.0 (2014-09-18)
        - gss-gex-sha1-*        # since 1.15.0 (2014-09-18)
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256         # since 1.16.0 (2015-11-04)
        - hmac-sha2-512         # since 1.16.0 (2015-11-04)
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
        - hmac-sha1
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic       # since 1.15.0 (2014-09-18) # only OID 1.2.840.113554.1.2.2 / Kerberos
        - gssapi-keyex          # since 1.15.0 (2014-09-18)
    extension:
        - server-sig-algs
---
* [Python](https://www.python.org/) library.
* Built on [pyca/cryptography](https://cryptography.io/).
