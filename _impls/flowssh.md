---
title: FlowSsh
developer: Bitvise
homepage: https://www.bitvise.com/flowssh
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 9.69
    date: 2026-11-16
changelog: https://www.bitvise.com/flowssh-version-history
client: yes
server: no
standalone: no
library: client
platforms:
    - windows
# Additions since 5.39 from https://bitvise.com/flowssh-version-history
protocols:
    cipher:
        - chacha20-poly1305@openssh.com # since 9.12
        - aes256-gcm@openssh.com        # since 7.12
        - aes128-gcm@openssh.com        # since 7.12
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - 3des-ctr
        - aes256-cbc        # disabled by default since 5.35
        - aes192-cbc        # disabled by default since 5.35
        - aes128-cbc        # disabled by default since 5.35
        - 3des-cbc          # disabled by default since 5.35
    compression:
        - none
        - zlib              # disabled by default
    hostkey:
        - ssh-mldsa44-ed25519       # since 9.67
        - ssh-ed25519               # since 7.21
        - rsa-sha2-256              # since 7.12
        - rsa-sha2-512              # since 7.12
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-1.3.132.0.10   # SEC 2 prime curve secp256k1? Not listed in RFC 5656
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
    kex:
        - mlkem1024nistp384-sha384      # since 9.51
        - mlkem768x25519-sha256         # since 9.51
        - curve25519-sha256             # since 7.21
        - ecdh-sha2-1.3.132.0.10
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256 # disabled by default
        - diffie-hellman-group-exchange-sha1   # disabled by default
        - diffie-hellman-group16-sha512        # since 7.21
        - diffie-hellman-group15-sha512        # since 7.21
        - diffie-hellman-group14-sha256        # since 7.21
        - diffie-hellman-group14-sha1          # disabled by default since 9.12
        - diffie-hellman-group1-sha1           # disabled by default since 5.35
        - ext-info-c                    # since 7.12
        - ext-info-s                    # by 8.15: the client sends its own EXT_INFO
        - kex-strict-c-v00@openssh.com  # since 9.32
        - kex-strict-s-v00@openssh.com  # since 9.32
    mac:
        - hmac-sha2-256-etm@openssh.com # since 9.12
        - hmac-sha2-512-etm@openssh.com # since 9.12
        - hmac-sha2-256
        - hmac-sha2-512     # since 9.12
        - hmac-sha1         # disabled by default since 9.12
        - hmac-md5          # disabled by default
        - hmac-sha2-256-96  # disabled by default
        - hmac-sha1-96      # disabled by default
        - hmac-md5-96       # disabled by default
    userauth:
        - publickey
        - password
        - keyboard-interactive
    extension:
        - elevation
        - server-sig-algs
        - delay-compression     # since 8.15
        - no-flow-control       # by 8.35
        - global-requests-ok    # since 8.21

disabled-by-default:
    cipher:
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - 3des-cbc
    compression:
        - zlib
    kex:
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha1
        - hmac-md5
        - hmac-sha2-256-96
        - hmac-sha1-96
        - hmac-md5-96
---
* Bitvise FlowSshC/Cpp/Net is an SSH library for C, C++, and .NET.
* 2015-07-10: The information provided here is based on the FlowSshC.h header file,
  as well as the [FlowSsh documentation](https://www.bitvise.com/fsd-index).
