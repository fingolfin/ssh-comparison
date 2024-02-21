---
title: phpseclib
homepage: http://phpseclib.sourceforge.net/
source-repository: https://github.com/phpseclib/phpseclib
license: "[MIT style](https://github.com/phpseclib/phpseclib/blob/master/LICENSE)"
first-release:
    date: 2007-09-23
latest-release:
    version: 3.0.2
    date: 2020-12-24
changelog: https://github.com/phpseclib/phpseclib/blob/master/CHANGELOG.md
client: unknown
server: unknown
library: client

protocols:
    cipher:
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - arcfour256
        - arcfour128
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - chacha20-poly1305@openssh.com
        - twofish128-ctr
        - twofish192-ctr
        - twofish256-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - twofish128-cbc
        - twofish192-cbc
        - twofish256-cbc
        - twofish-cbc
        - blowfish-ctr
        - blowfish-cbc
        - 3des-ctr
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman_group17-sha512
        - diffie-hellman-group18-sha512
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - umac-64-etm@openssh.com
        - umac-128-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - umac-64@openssh.com
        - umac-128@openssh.com
        - hmac-sha1-96
        - hmac-sha1
        - hmac-md5-96
        - hmac-md5
    userauth:
        - keyboard-interactive
        - publickey
        - password
    extension:
        - kex-strict-c-v00@openssh.com  # since 3.0.35 / 2.0.46 / 1.0.22
        - kex-strict-s-v00@openssh.com  # since 3.0.35 / 2.0.46 / 1.0.22
---
* Pure PHP implementation.
