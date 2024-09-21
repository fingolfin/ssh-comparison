---
title: Tera Term
homepage: https://teratermproject.github.io/index-en.html
source-repository: https://github.com/TeraTermProject/teraterm
license: "[BSD style](https://teratermproject.github.io/manual/5/en/about/copyright.html)"
first-release:
    date: 2004    # according to Wikipedia
latest-release:
    version: 5.3
    date: 2024-09-08
changelog: https://teratermproject.github.io/manual/5/en/about/history.html
client: yes
server: no
library: no
platforms:
    - windows

protocols:
    cipher:
        - 3des-cbc
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - blowfish-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - arcfour
        - arcfour128
        - arcfour256
        - cast128-cbc
        - 3des-ctr
        - blowfish-ctr
        - cast128-ctr
        - camellia128-cbc
        - camellia192-cbc
        - camellia256-cbc
        - camellia128-ctr
        - camellia192-ctr
        - camellia256-ctr
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - rsa-sha2-256
        - rsa-sha2-512
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha256
        - diffie-hellman-group16-sha256
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha1
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
        - hmac-ripemd160@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - hmac-ripemd160-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
    userauth:
        - password
        - publickey
        - keyboard-interactive
    extension:
        - server-sig-algs

ident: "SSH-2.0-TTSSH/3.2 Win32"
---
* [Wikipedia page](https://en.wikipedia.org/wiki/Tera_Term)
