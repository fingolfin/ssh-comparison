---
title: SSH2
homepage: https://github.com/mscdex/ssh2
source-repository: https://github.com/mscdex/ssh2
license: "[MIT style](https://github.com/mscdex/ssh2/blob/master/LICENSE)"
first-release:
    date: 2012-11-11
latest-release:
    version: 1.16.0
    date: 2024-09-16
#changelog: ?
client: yes
server: yes
library: both
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes128-gcm
        - aes128-gcm@openssh.com
        - aes256-gcm
        - aes256-gcm@openssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - 3des-cbc
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - arcfour256
        - arcfour128
        - arcfour
        - blowfish-cbc
        - cast128-cbc
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5
        - hmac-sha2-256-96
        - hmac-sha2-512-96
        - hmac-ripemd160
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - password
        - publickey
        - hostbased
        - keyboard-interactive
    extension:
        - server-sig-algs
---
* SSH2 client and server modules written in pure JavaScript for [node.js](https://nodejs.org/).
