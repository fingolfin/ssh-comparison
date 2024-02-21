---
title: Tera Term
homepage: https://ttssh2.osdn.jp/
source-repository: https://en.osdn.jp/projects/ttssh2/scm/svn/
license: "[BSD style](http://ttssh2.osdn.jp/manual/en/about/copyright.html)"
first-release:
    date: 2004    # according to Wikipedia
latest-release:
    version: 4.89
    date: 2015-12-01
#changelog: TODO
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
    mac:
        - hmac-sha1
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
        - hmac-ripemd160@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
    userauth:
        - password
        - publickey
        - keyboard-interactive
    extension:
        - kex-strict-c-v00@openssh.com  # since 5.1 / 4.108
        - kex-strict-s-v00@openssh.com  # since 5.1 / 4.108

ident: "SSH-2.0-TTSSH/2.75 Win32"
---
* [Wikipedia page](https://en.wikipedia.org/wiki/Tera_Term)
