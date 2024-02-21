---
title: Xshell 5
homepage: http://www.netsarang.com/products/xsh_overview.html
developer: NetSarang
license: Proprietary
first-release:
    date: 2002-11-02
latest-release:
    version: 0977
    date: 2016-04-22
changelog: http://www.netsarang.com/products/xsh_update.html
client: yes
server: no
library: no
platforms:
    - windows
protocols:
    cipher:
        - aes128-cbc
        - 3des-cbc
        - blowfish-cbc
        - cast128-cbc
        - arcfour
        - aes192-cbc
        - aes128-gcm@openssh.com    # since version 0788
        - aes256-gcm@openssh.com    # since version 0788
        - aes256-cbc
        - rijndael128-cbc
        - rijndael192-cbc
        - rijndael256-cbc
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - rijndael-cbc@lysator.liu.se
        - arcfour128                # since version 0752
        - arcfour256                # since version 0752
    compression:
        - none
        - zlib                      # disabled by default
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256       # since version 0858
    kex:
        - ecdh-sha2-nistp256        # since version 0858
        - ecdh-sha2-nistp384        # since version 0858
        - ecdh-sha2-nistp521        # since version 0858
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha2-256-etm@openssh.com # since version 0752
        - hmac-sha2-512-etm@openssh.com # since version 0858
        - hmac-sha1-etm@openssh.com     # since version 0752
        - hmac-sha2-256
        - hmac-sha2-512                 # since version 0858
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
        - hmac-sha1-96-etm@openssh.com  # since version 0752
        - hmac-md5-etm@openssh.com      # since version 0752
        - hmac-md5-96-etm@openssh.com   # since version 0752
    userauth:
        - publickey
        - gssapi-with-mic
        - password
        - keyboard-interactive
    extension:
        - kex-strict-c-v00@openssh.com  # since version 0144
        - kex-strict-s-v00@openssh.com  # since version 0144

first_kex_packet_follows: 0
ident: "SSH-2.0-nsssh2_5.0.0030 NetSarang Computer, Inc."
---
