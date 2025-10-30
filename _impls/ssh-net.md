---
title: SSH.NET
homepage: https://sshnet.github.io/SSH.NET/
source-repository: https://github.com/sshnet/SSH.NET
license: "[MIT license](https://github.com/sshnet/SSH.NET/blob/develop/LICENSE)"
first-release:
    date: 2010-09-16
latest-release:
    version: 2025.1.0
    date: 2025-10-27
changelog: https://github.com/sshnet/SSH.NET/releases
client: yes
server: no
library: client

protocols:
    cipher:
        - aes256-ctr
        - 3des-cbc
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        #- blowfish-cbc                 # removed in 2024.2.0
        #- twofish-cbc                  # removed in 2024.2.0
        #- twofish192-cbc               # removed in 2024.2.0
        #- twofish128-cbc               # removed in 2024.2.0
        #- twofish256-cbc               # removed in 2024.2.0
        #- arcfour                      # removed in 2024.2.0
        #- arcfour128                   # removed in 2024.2.0
        #- arcfour256                   # removed in 2024.2.0
        #- cast128-cbc                  # removed in 2024.2.0
        - aes128-ctr
        - aes192-ctr
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com # since 2024.2.0
    compression:
        - none
        - zlib@openssh.com
    hostkey:
        - ssh-ed25519-cert-v01@openssh.com         # since 2024.2.0
        - ecdsa-sha2-nistp256-cert-v01@openssh.com # since 2024.2.0
        - ecdsa-sha2-nistp384-cert-v01@openssh.com # since 2024.2.0
        - ecdsa-sha2-nistp521-cert-v01@openssh.com # since 2024.2.0
        - rsa-sha2-512-cert-v01@openssh.com        # since 2024.2.0
        - rsa-sha2-256-cert-v01@openssh.com        # since 2024.2.0
        - ssh-rsa-cert-v01@openssh.com             # since 2024.2.0
        #- ssh-dss-cert-v01@openssh.com            # removed in 2025.0.0
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
        #- ssh-dss                                 # removed in 2025.0.0
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group18-sha512        # since 2025.1.0
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
        - mlkem768x25519-sha256                # since 2025.0.0
        - sntrup761x25519-sha512               # since 2025.0.0
        - sntrup761x25519-sha512@openssh.com   # since 2025.0.0
    mac:
        #- hmac-md5                      # removed in 2024.2.0
        #- hmac-md5-96                   # removed in 2024.2.0
        - hmac-sha1
        #- hmac-sha1-96                  # removed in 2024.2.0
        - hmac-sha2-256
        #- hmac-sha2-256-96              # removed in 2024.2.0
        - hmac-sha2-512
        #- hmac-sha2-512-96              # removed in 2024.2.0
        #- hmac-ripemd160                # removed in 2024.0.0
        #- hmac-ripemd160@openssh.com    # removed in 2024.0.0
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        #- hmac-sha1-96-etm@openssh.com  # removed in 2024.2.0
        #- hmac-md5-etm@openssh.com      # removed in 2024.2.0
        #- hmac-md5-96-etm@openssh.com   # removed in 2024.2.0
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - hostbased
---
* Library for .NET.
* Supports SFTP, SCP
* Supports SOCKS4, SOCKS5 and HTTP proxies
* Supports remote, dynamic and local port forwarding
* Supports two-factor or higher authentication
