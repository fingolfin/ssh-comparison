---
title: JSch
homepage: https://github.com/mwiede/jsch
source-repository: https://github.com/mwiede/jsch
license: "[BSD style](https://github.com/mwiede/jsch/blob/master/LICENSE.txt)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 0.2.18
    date: 2024-06-07
changelog: https://github.com/mwiede/jsch/blob/master/ChangeLog.md
client: yes
server: no
library: client

protocols:
    cipher:
        - 3des-cbc
        - 3des-ctr
        - aes128-cbc
        - aes128-ctr
        - aes128-gcm@openssh.com
        - aes192-cbc
        - aes192-ctr
        - aes256-cbc
        - aes256-ctr
        - aes256-gcm@openssh.com
        - arcfour
        - arcfour128
        - arcfour256
        - blowfish-cbc
        - blowfish-ctr
        - cast128-cbc
        - cast128-ctr
        - chacha20-poly1305@openssh.com
        - rijndael-cbc@lysator.liu.se
        - seed-cbc@ssh.com
        - twofish-cbc
        - twofish128-cbc
        - twofish128-ctr
        - twofish192-cbc
        - twofish192-ctr
        - twofish256-cbc
        - twofish256-ctr
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-dss
        - ssh-ed25519
        - ssh-ed448
        - ssh-rsa
        - ssh-rsa-sha224@ssh.com
        - ssh-rsa-sha256@ssh.com
        - ssh-rsa-sha384@ssh.com
        - ssh-rsa-sha512@ssh.com
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - curve448-sha512
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha224@ssh.com
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha384@ssh.com
        - diffie-hellman-group-exchange-sha512@ssh.com
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha224@ssh.com
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha256@ssh.com
        - diffie-hellman-group15-sha256@ssh.com
        - diffie-hellman-group15-sha384@ssh.com
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha384@ssh.com
        - diffie-hellman-group16-sha512
        - diffie-hellman-group16-sha512@ssh.com
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group18-sha512@ssh.com
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - ext-info-c
        - ext-info-s
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
        - sntrup761x25519-sha512@openssh.com
    mac:
        - hmac-md5
        - hmac-md5-96
        - hmac-md5-96-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-ripemd160
        - hmac-ripemd160-etm@openssh.com
        - hmac-ripemd160@openssh.com
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha1-96-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha224@ssh.com
        - hmac-sha256-2@ssh.com
        - hmac-sha256@ssh.com
        - hmac-sha384@ssh.com
        - hmac-sha512@ssh.com
    userauth:
        - gssapi-with-mic           # only OID 1.2.840.113554.1.2.2 / Kerberos
        - keyboard-interactive
        - password
        - publickey
    extension:
        - ext-info-in-auth@openssh.com
        - server-sig-algs
---
* Pure Java implementation.
* This is a fork of the original [JSch project](https://sourceforge.net/projects/jsch/)
