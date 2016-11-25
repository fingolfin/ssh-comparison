---
title: SmartFTP
homepage: https://www.smartftp.com/
license: Proprietary
first-release:
    date: 1998
latest-release:
    version: 8.0.2270
    date: 2016-11-25
changelog: https://www.smartftp.com/changelog/1
client: yes
server: no
protocols:
    cipher:
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - 3des-cbc
    compression:
        - zlib@openssh.com
        - none
    hostkey:
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-rsa
        - ssh-dss
        - ssh-rsa-sha256@ssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - x509v3-rsa2048-sha256
        - x509v3-ssh-rsa
        - x509v3-ssh-dss
        - x509v3-ecdsa-sha2-nistp256
        - x509v3-ecdsa-sha2-nistp384
        - x509v3-ecdsa-sha2-nistp521
        - ssh-ed25519
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group-exchange-sha1 # Minimum group size 2048-bit
        - diffie-hellman-group-exchange-sha256 # Minimum group size 2048-bit
        - diffie-hellman-group16-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256@libssh.org
        - curve25519-sha256
        - ext-info-c
    mac:
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - hostbased
    extension:
        - server-sig-algs
        - no-flow-control
---
* Windows client.
* Supports FTP, FTPS, SFTP, WebDAV, S3, Google Drive, Microsoft OneDrive, SSH, Terminal client.
* [Details on its SSH support](https://www.smartftp.com/client/features/ssh).
