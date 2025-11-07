---
title: AbsoluteTelnet
homepage: https://celestialsoftware.net/
license: Proprietary
first-release:
    date: 1996      # according to Wikipedia
latest-release:
    version: 13.13
    date: 2025-10-22
changelog: https://www.celestialsoftware.net/version-history
client: yes
server: no
library: no
platforms:
    - windows
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - 3des-cbc
        - 3des-ctr
        - twofish128-cbc                # disabled by default in 9.84
        - twofish256-cbc                # disabled by default in 9.84
        - arcfour                       # disabled by default in 9.84
        - arcfour128                    # disabled by default in 9.84
        - arcfour256                    # disabled by default in 9.84
        - blowfish-cbc                  # disabled by default in 9.84
        - cast128-cbc                   # disabled by default in 9.84
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
        - ssh-dss
        - sk-ecdsa-sha2-nistp256@openssh.com
        - sk-ssh-ed25519@openssh.com
    kex:
        - mlkem768x25519-sha256
        - sntrup761x25519-sha512
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group18-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - hmac-md5                      # disabled by default in 9.84
        - hmac-md5-96                   # disabled by default in 9.84
        - hmac-sha1
        - hmac-sha1-96                  # disabled by default in 9.84
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

# X11 forwarding, Port forwarding, sftp client, telnet client
---

* Windows client.
* [Wikipedia](https://en.wikipedia.org/wiki/AbsoluteTelnet)
* [AbsoluteTelnet SSH Client](https://www.celestialsoftware.net)
* [AbsoluteTelnet/SSH Supported Algorithms](https://www.celestialsoftware.net/supported-algorithms)
