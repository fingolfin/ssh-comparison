---
title: RLogin
homepage: http://nanno.bf1.jp/softlib/man/rlogin/
source-repository: https://github.com/kmiya-culti/RLogin
license: "[MIT](https://github.com/kmiya-culti/RLogin/blob/master/LICENSE)"
first-release:
    date: 2005-05-16    # first release with SSH 2 support was 1.0.7
latest-release:
    version: 2.31.9
    date: 2026-09-25
changelog: http://nanno.bf1.jp/softlib/man/rlogin/history.html
client: yes
server: no
library: no
platforms:
    - windows
remarks: |
    * Only available in Japanese.
    * The list of supported protocols is the default proposal of 2.31.9
      (RLogin/Data.cpp, RLogin/ssh.cpp), built with Nettle and without CLEFIA.

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - chacha20-poly1305
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - camellia256-ctr
        - camellia192-ctr
        - camellia128-ctr
        - blowfish-ctr
        - cast128-ctr
        - twofish-ctr
        - idea-ctr
        - seed-ctr@ssh.com
        - 3des-ctr
        - AEAD_AES_256_GCM      # supported, not in the default proposal
        - AEAD_AES_128_GCM      # supported, not in the default proposal
        #- AEAD_AES_256_CCM     # ignore
        #- AEAD_AES_128_CCM     # ignore
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - aes128-gcm
        - aes256-gcm
        - arcfour256
        - arcfour128
        - arcfour
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - camellia256-cbc
        - camellia192-cbc
        - camellia128-cbc
        - blowfish-cbc
        - cast128-cbc
        - idea-cbc
        - twofish-cbc
        - seed-cbc@ssh.com
        - 3des-cbc
        - twofish256-ctr
        - twofish192-ctr
        - twofish128-ctr
        - serpent256-ctr
        - serpent192-ctr
        - serpent128-ctr
        - twofish256-cbc
        - twofish192-cbc
        - twofish128-cbc
        - serpent256-cbc
        - serpent192-cbc
        - serpent128-cbc
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        #- ssh-rsa-cert-v01@openssh.com     # not in 2.31.9
        #- ssh-dss-cert-v01@openssh.com     # not in 2.31.9
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - ssh-ed448
        - rsa-sha2-512
        - rsa-sha2-256
        #- ssh-rsa-sha2-512                 # not in 2.31.9
        #- ssh-rsa-sha2-256                 # not in 2.31.9
        - ssh-mldsa-44
        - ssh-mldsa-65
        - ssh-mldsa-87
        - ssh-mldsa44-ed25519
        - ssh-mldsa65-ed25519
        - ssh-mldsa87-ed448
        - ssh-rsa
        - ssh-dss
    kex:
        - mlkem768x25519-sha256
        - mlkem768nistp256-sha256
        - mlkem1024nistp384-sha384
        - mlkem512-sha256
        - mlkem768-sha256
        - mlkem1024-sha384
        - sntrup761x25519-sha512
        - sntrup761x25519-sha512@openssh.com
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - curve448-sha512
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha256
        #- diffie-hellman-group15-sha256    # not in 2.31.9
        #- diffie-hellman-group16-sha256    # not in 2.31.9
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - rsa2048-sha256
        - rsa1024-sha1
        - ext-info-c
        - kex-strict-c
        - kex-strict-s
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - umac-64-etm@openssh.com
        - umac-128-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-256-96
        - hmac-sha2-512
        - hmac-sha2-512-96
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-whirlpool
        - umac-64@openssh.com
        - umac-128@openssh.com
        - umac-128
        - umac-96
        - umac-64
        - umac-32
    userauth:
        - publickey
        - publickey-hostbound-v00@openssh.com
        - hostbased
        - gssapi-with-mic
        - password
        - keyboard-interactive
    extension:
        - server-sig-algs
        - publickey-hostbound@openssh.com
        - ext-info-in-auth@openssh.com
        - agent-forward
        - hostkeys

---
* Seems to implement many non-standardized protocol variations, such as umac-32 and umac-96,
  or AEAD_AES_256_CCM; and also things that once were discussed, but then dropped from
  the specs, like hmac-sha2-256-96
* Built on OpenSSL (2.31.9: openssl-3.5.8).
