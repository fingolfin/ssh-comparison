---
title: Georgia SoftWorks SSH
homepage: https://www.georgiasoftworks.com/ssh-server-windows
developer: Georgia SoftWorks
license: Proprietary
first-release:
    date: 2004-07   # according to Wikipedia
latest-release:
    version: 8.16.0031
    date: 2026-04-30
changelog: https://www.georgiasoftworks.com/product/ssh-server-windows#downloads

client: yes   # for multiple devices; but do they all support the same?
server: yes
#library: unknown

# TODO: http://www.georgiasoftworks.com/products/ssh/ssh_authentication_x509v3.php
# TODO: what about http://www.georgiasoftworks.com/security/fips.php ?
# cipher, kex and mac: all algorithms available with FIPS 140-2 disabled, per
# the vendor FAQs (2022) https://www.georgiasoftworks.com/ssh-server-windows/faq
# (specify-ciphers, specify-macs, specify-key-exchange-algorithms).
# 8.16.0031 added ML-KEM key exchange; the method names are not documented.
protocols:
    cipher:
        - aes128-cbc
        - chacha20-poly1305@openssh.com
        - aes128-ctr
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - 3des-cbc
        - blowfish-cbc
        - aes192-cbc
        - aes192-ctr
        - aes256-cbc
        - aes256-ctr
        - rijndael128-cbc
        - rijndael192-cbc
        - rijndael256-cbc
        - rijndael-cbc@lysator.liu.se
        - cast128-cbc
    compression:
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp521
        - x509v3-sign-dss
        - x509v3-sign-rsa
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group18-sha512
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
    mac:
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
#    userauth:
---
* data based on [user's manual](http://www.georgiasoftworks.com/docs/ssh2/SSH2_usersguide.php)
