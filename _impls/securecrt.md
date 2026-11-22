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
     version: 9.7.4
     date: 2026-11-03
changelog: https://www.vandyke.com/products/securecrt/history.txt
client: yes
server: no
library: no
# Changes since 8.0.1 from the per-release histories
# https://www.vandyke.com/download/securecrt/<8.0 ... 9.6>/history.txt and the changelog above
protocols:
    cipher:
        - chacha20-poly1305@openssh.com # since 8.3
        - aes256-gcm@openssh.com        # since 8.3; default since 9.7
        - aes128-gcm@openssh.com        # since 8.3
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - 3des-cbc
        - twofish-cbc
        #- blowfish-cbc     # removed in 9.0
        #- arcfour          # removed in 9.0
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - ssh-ed25519       # since 8.0
        - rsa-sha2-256      # since 9.0
        - rsa-sha2-512      # since 9.0
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256-cert-v01@openssh.com # since 9.3
        - rsa-sha2-512-cert-v01@openssh.com # since 9.3
        - x509v3-ssh-rsa    # since 8.0, Windows only
        - x509v3-ssh-dss    # since 8.0, Windows only
        - x509v3-ecdsa-sha2-nistp256    # since 8.7
        - x509v3-ecdsa-sha2-nistp384    # since 8.7
        - x509v3-ecdsa-sha2-nistp521    # since 8.7
        - x509v3-rsa2048-sha256         # since 9.3
    kex:
        - curve25519-sha256             # since 8.5.2
        - curve25519-sha256@libssh.org  # since 8.5.3
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group18-sha512 # since 8.7
        - diffie-hellman-group17-sha512 # since 9.7
        - diffie-hellman-group16-sha512 # since 8.7
        - diffie-hellman-group15-sha512 # since 9.7
        - diffie-hellman-group14-sha256 # since 8.7
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1    # disabled by default since 8.0
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - gss-gex-sha1-*
        - ext-info-c
        - kex-strict-c-v00@openssh.com  # since 9.4.3
        - kex-strict-s-v00@openssh.com  # since 9.4.3
    mac:
        - hmac-sha2-512-etm@openssh.com # since 8.5
        - hmac-sha2-256-etm@openssh.com # since 8.5
        - hmac-sha1
        - hmac-sha2-512
        - hmac-sha2-384
        - hmac-sha2-256
        - hmac-sha1-96      # removed in 9.0, restored in 9.0.1
        #- hmac-md5         # removed in 9.0
        - hmac-md5-96       # removed in 9.0, restored in 9.0.1
        - umac-64@openssh.com
        - umac-128@openssh.com  # since 8.3
    userauth:
        - password
        - publickey
        - keyboard-interactive
        - gssapi-with-mic
        - gssapi-keyex
    extension:
        - server-sig-algs   # by 9.7

disabled-by-default:
    kex:
        - diffie-hellman-group1-sha1


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
