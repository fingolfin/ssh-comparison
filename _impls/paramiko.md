---
title: Paramiko
homepage: http://www.paramiko.org/
source-repository: https://github.com/paramiko/paramiko
license: "[LGPL 2.1](https://github.com/paramiko/paramiko/blob/master/LICENSE)"
first-release:
    date: 2003-09-13    # v0.1, according to NEWS file
latest-release:
    version: 2.0.0
    date: 2016-04-28
changelog: http://www.paramiko.org/changelog.html
client: yes
server: yes
library: both

protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr            # since 1.16.0 (2015-11-04)
        - aes256-ctr
        - aes128-cbc
        - blowfish-cbc
        - aes192-cbc            # since 1.16.0 (2015-11-04)
        - aes256-cbc
        - 3des-cbc
        - arcfour128
        - arcfour256
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
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1   # since 1.15.0 (2014-09-18)
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256  # since 1.16.0 (2015-11-04)
        - gss-group1-sha1-*     # since 1.15.0 (2014-09-18)
        - gss-group14-sha1-*    # since 1.15.0 (2014-09-18)
        - gss-gex-sha1-*        # since 1.15.0 (2014-09-18)
    mac:
        - hmac-sha2-256         # since 1.16.0 (2015-11-04)
        - hmac-sha2-512         # since 1.16.0 (2015-11-04)
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
        - hmac-sha1
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic       # since 1.15.0 (2014-09-18) # only OID 1.2.840.113554.1.2.2 / Kerberos
        - gssapi-keyex          # since 1.15.0 (2014-09-18)
    extension:
        - kex-strict-c-v00@openssh.com  # since 3.4.0
        - kex-strict-s-v00@openssh.com  # since 3.4.0
---
* [Python](https://www.python.org/) library.
* Built on [PyCrypto](http://pycrypto.org/), a Python C extension for low level cryptography.
