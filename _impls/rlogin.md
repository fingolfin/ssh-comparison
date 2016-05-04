---
title: RLogin
homepage: http://nanno.dip.jp/softlib/man/rlogin/
source-repository: TODO
# http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/
license: "TODO"
first-release:
    date: 2005-05-16    # first release with SSH 2 support was 1.0.7
latest-release:
    version: 2.20.3
    date: 2016-04-05
changelog: http://nanno.dip.jp/softlib/man/rlogin/history.html
client: yes
server: no
library: no
platforms:
    - windows
remarks: |
    * Only available in Japanes.
    * The list of supported protocols is based on what the website reports.

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
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
        - AEAD_AES_256_GCM
        - AEAD_AES_128_GCM
        #- AEAD_AES_256_CCM     # ignore
        #- AEAD_AES_128_CCM     # ignore
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
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
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - ssh-rsa-sha2-512
        - ssh-rsa-sha2-256
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha256
        - diffie-hellman-group16-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
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
        - hostbased
        - password
        - keyboard-interactive

---
* Seems to implement many non-standardized protocol variations, such as umac-32 and umac-96,
  or AEAD_AES_256_CCM; and also things that once were discussed, but then dropped from
  the specs, like hmac-sha2-256-96
* Release notes of version 2.20.1 refer to openssl-1.0.2g, so presumably based on that.
