---
title: SmartFTP
homepage: https://www.smartftp.com/
license: Proprietary
first-release:
    date: 1998
latest-release:
    version: 10.0.3306
    date: 2026-01-17
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
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - x509v3-rsa2048-sha256
        - x509v3-ssh-rsa
        - x509v3-ecdsa-sha2-nistp256
        - x509v3-ecdsa-sha2-nistp384
        - x509v3-ecdsa-sha2-nistp521
        - ssh-ed25519
        - ssh-ed448
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - ssh-mldsa44
        - ssh-mldsa65
        - ssh-mldsa87
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group-exchange-sha1 # Minimum group size 2048-bit
        - diffie-hellman-group-exchange-sha256 # Minimum group size 2048-bit
        - diffie-hellman-group16-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - mlkem768x25519-sha256
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
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
* Supports FTP, FTPS, SFTP, WebDAV, S3, Google Drive, Microsoft OneDrive, Backblaze, SSH, Terminal client.
* [Details on its SSH support](https://www.smartftp.com/client/features/ssh).
