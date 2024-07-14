---
title: libassh
homepage: https://www.nongnu.org/libassh/
source-repository: https://hg.savannah.nongnu.org/hgweb/libassh/
license: "[LGPL 2.1](https://www.nongnu.org/libassh/manual/Copyright_and_license.html)"
first-release:
    date: 2020-09-28
latest-release:
    version: 1.1
    date: 2023-02-05
#changelog: TODO available in the next release :)
client: yes
server: yes
library: both
protocols:
    cipher:
        - 3des-cbc
        - 3des-ctr
        - aes128-cbc
        - aes128-ctr
        - aes128-gcm@openssh.com
        - aes128-ocb@libassh.org
        - aes192-cbc
        - aes192-ctr
        - aes256-cbc
        - aes256-ctr
        - aes256-gcm@openssh.com
        - aes256-ocb@libassh.org
        - arcfour
        - arcfour128
        - arcfour256
        - blowfish-cbc
        - blowfish-ctr
        - camellia128-cbc
        - camellia128-ctr
        - camellia192-cbc
        - camellia192-ctr
        - camellia256-cbc
        - camellia256-ctr
        - cast128-cbc
        - cast128-ctr
        - chacha20-poly1305@openssh.com
        - idea-cbc
        - idea-ctr
        - rijndael-cbc@lysator.liu.se
        - serpent128-cbc
        - serpent128-ctr
        - serpent128-gcm@libassh.org
        - serpent192-cbc
        - serpent192-ctr
        - serpent256-cbc
        - serpent256-ctr
        - serpent256-gcm@libassh.org
        - twofish128-cbc
        - twofish128-ctr
        - twofish128-gcm@libassh.org
        - twofish256-cbc
        - twofish256-ctr
        - twofish256-gcm@libassh.org
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - dsa2048-sha224@libassh.org
        - dsa2048-sha256@libassh.org
        - dsa3072-sha256@libassh.org
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - eddsa-e382-shake256@libassh.org
        - eddsa-e521-shake256@libassh.org
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-dss
        - ssh-ed25519
        - ssh-rsa
    kex:
        - curve25519-sha256@libssh.org
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - m383-sha384@libassh.org
        - m511-sha512@libassh.org
        - rsa1024-sha1
        - rsa2048-sha256
    mac:
        - hmac-md5
        - hmac-md5-96
        - hmac-md5-96-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-ripemd160
        - hmac-ripemd160-etm@openssh.com
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha1-96-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - hostbased
    extension:

first_kex_packet_follows: 0
---
* Portable C library with an asynchronous API.
