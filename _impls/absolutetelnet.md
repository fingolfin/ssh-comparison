---
title: AbsoluteTelnet
homepage: https://celestialsoftware.net/
license: Proprietary
first-release:
    date: 1996      # according to Wikipedia
latest-release:
    version: 10.15
    date: 2016-01-21
changelog: https://celestialsoftware.net/absolutetelnet-ssh-client/absolutetelnet/ssh-version-history-9.53.html
client: yes
server: no
library: no
platforms:
    - windows
protocols:
    cipher:
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
        - ssh-rsa
        - ssh-dss
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
    mac:
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
        - kex-strict-c-v00@openssh.com  # since 12.11
        - kex-strict-s-v00@openssh.com  # since 12.11

# X11 forwarding, Port forwarding, sftp client, telnet client
---

* Windows client.
* [Wikipedia](https://en.wikipedia.org/wiki/AbsoluteTelnet)
