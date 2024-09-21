---
title: SSHJ
homepage: https://github.com/hierynomus/sshj
source-repository: https://github.com/hierynomus/sshj
changelog: https://github.com/hierynomus/sshj
license: "[Apache-2.0](https://github.com/hierynomus/sshj/blob/master/LICENSE)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 0.39.0
    date: 2024-09-13
#changelog: URL
client: yes
server: no
library: client
protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - 3des-ctr
        - 3des-cbc
        - blowfish-ctr
        - blowfish-cbc
        - chacha20-poly1305@openssh.com
        - twofish128-ctr
        - twofish192-ctr
        - twofish256-ctr
        - twofish128-cbc
        - twofish192-cbc
        - twofish256-cbc
        - twofish-cbc
        - serpent128-ctr
        - serpent192-ctr
        - serpent256-ctr
        - serpent128-cbc
        - serpent192-cbc
        - serpent256-cbc
        - idea-ctr
        - idea-cbc
        - cast128-ctr
        - cast128-cbc
        - arcfour
        - arcfour128
        - arcfour256
        - camellia128-ctr
        - camellia192-ctr
        - camellia256-ctr
        - camellia128-cbc
        - camellia192-cbc
        - camellia256-cbc
        - camellia128-ctr@openssh.org
        - camellia192-ctr@openssh.org
        - camellia256-ctr@openssh.org
        - camellia128-cbc@openssh.org
        - camellia192-cbc@openssh.org
        - camellia256-cbc@openssh.org
    compression:
        - zlib              # disabled by default
        - zlib@openssh.com  # disabled by default
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
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - diffie-hellman-group-exchange-sha256
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha256@ssh.com
        - diffie-hellman-group15-sha256
        - diffie-hellman-group15-sha256@ssh.com
        - diffie-hellman-group15-sha384@ssh.com
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha256
        - diffie-hellman-group16-sha384@ssh.com
        - diffie-hellman-group16-sha512
        - diffie-hellman-group16-sha512@ssh.com
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group18-sha512@ssh.com
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-ripemd160-etm@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - hostbased
---
* Pure Java implementation.
