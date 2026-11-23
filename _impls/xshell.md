---
title: Xshell
homepage: https://www.netsarang.com/en/xshell/
developer: NetSarang
license: Proprietary
first-release:
    date: 2002-11-02
latest-release:
    version: 8 Build 0120
    date: 2026-11-11
changelog: https://www.netsarang.com/en/xshell-update-history/
client: yes
server: no
standalone: client
library: no
platforms:
    - windows
# Bare build numbers are Xshell 5 builds. Additions after 5 Build 0977 are
# from the Xshell 5-8 update histories; these omit what each major release
# added, so the list may be incomplete.
protocols:
    cipher:
        - chacha20-poly1305@openssh.com   # since 6 Build 0114
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
        - zlib@openssh.com          # "delayed" compression, bug fixed in 5 (2017-04)
    hostkey:
        - ssh-ed25519               # since 5 (2017-04)
        - rsa-sha2-256              # since 6 Build 0181
        - rsa-sha2-512              # since 6 Build 0181
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256       # since version 0858
        - ecdsa-sha2-nistp384       # since 6 Build 0170
        - ecdsa-sha2-nistp521       # since 6 Build 0170
    kex:
        - curve25519-sha256         # since 7 Build 0111
        - ecdh-sha2-nistp256        # since version 0858
        - ecdh-sha2-nistp384        # since version 0858
        - ecdh-sha2-nistp521        # since version 0858
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha256 # since 6 Build 0170
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
        - umac-64@openssh.com           # since 6 Build 0181
        - umac-128@openssh.com          # since 6 Build 0181
        - umac-64-etm@openssh.com       # since 6 Build 0181
        - umac-128-etm@openssh.com      # since 6 Build 0181
    userauth:
        - publickey
        - gssapi-with-mic
        - password
        - keyboard-interactive

disabled-by-default:
    compression:
        - zlib

first_kex_packet_follows: 0
ident: "SSH-2.0-nsssh2_5.0.0030 NetSarang Computer, Inc."
---
