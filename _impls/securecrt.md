---
title: SecureCRT
homepage: https://www.vandyke.com/products/securecrt/index.html
# TODO: also check out VShell
#    https://www.vandyke.com/products/vshell/features.html
developer: VanDyke Software
license: Proprietary
first-release:
    date: 1998-06   # according to Wikipedia
latest-release:
     version: 8.0.1
     date: 2016-04-26
changelog: https://www.vandyke.com/products/securecrt/history.txt
client: yes
server: no
library: no
protocols:
    cipher:
        - aes128-cbc
        - aes192-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - 3des-cbc
        - twofish-cbc
        - blowfish-cbc
        - arcfour
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - ssh-rsa
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - x509v3-ssh-rsa    # since 8.0 (windows only??)
        - x509v3-ssh-dss    # since 8.0 (windows only??)
    kex:
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - gss-gex-sha1-*
    mac:
        - hmac-sha1
        - hmac-sha2-512
        - hmac-sha2-384
        - hmac-sha2-256
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - umac-64@openssh.com
    userauth:
        - password
        - publickey
        - keyboard-interactive
        - gssapi-with-mic
        - gssapi-keyex
    extension:
        - kex-strict-c-v00@openssh.com  # since 9.4.3
        - kex-strict-s-v00@openssh.com  # since 9.4.3

#sftp-su@vandyke.com
#read-directory-changes@vandyke.com
#get-volume-information@vandyke.com
#statvfs@openssh.com
#space-available
#check-file-name
#check-file-handle
#receipt@vandyke.com
#receipt-request@vandyke.com

# iOS version 1.1.1 Jul 20, 2015
# https://itunes.apple.com/en/app/id911124130
---
* Windows, Linux, Mac OS X, iOS (iPad) client
