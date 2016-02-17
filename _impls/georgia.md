---
title: Georgia SoftWorks SSH
homepage: http://www.georgiasoftworks.com/products/ssh/ssh2_server.php
developer: Georgia SoftWorks
license: Proprietary
first-release:
    date: 2004-07   # according to Wikipedia
latest-release:
    version: 8.05.0031
    date: 2014-10-24
#changelog: URL
client: yes   # for multiple devices; but do they all support the same?
server: yes
#library: unknown

# TODO: http://www.georgiasoftworks.com/products/ssh/ssh_authentication_x509v3.php
# TODO: what about http://www.georgiasoftworks.com/security/fips.php ?
protocols:
    cipher:
        - aes128-cbc
        - aes128-ctr
        - 3des-cbc
        - aes192-cbc
        - aes192-ctr
        - aes256-cbc
        - aes256-ctr
        - rijndael192-cbc
        - rijndael256-cbc
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
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha1-96
#    userauth:
---
* data based on [user's manual](http://www.georgiasoftworks.com/docs/ssh2/SSH2_usersguide.php)
