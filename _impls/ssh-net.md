---
title: SSH.NET
homepage: https://github.com/sshnet/SSH.NET/
source-repository: https://github.com/sshnet/SSH.NET.git
license: "[MIT license](https://github.com/sshnet/SSH.NET/blob/develop/LICENSE)"
first-release:
    date: 2010-09-16
latest-release:
    version: 2020.0.2-pre
    date: 2020-05-29
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
        - blowfish-cbc
        - twofish-cbc
        - twofish192-cbc
        - twofish128-cbc
        - twofish256-cbc
        - arcfour
        - arcfour128
        - arcfour256
        - cast128-cbc
        - aes128-ctr
        - aes192-ctr
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-md5
        - hmac-md5-96
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha2-256
        - hmac-sha2-256-96
        - hmac-sha2-512
        - hmac-sha2-512-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
---
* Library for .NET.
* Supports SFTP, SCP
* Supports SOCKS4, SOCKS5 and HTTP proxies
* Supports remote, dynamic and local port forwarding
* Supports two-factor or higher authentication
