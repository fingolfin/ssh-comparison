---
title: FlowSsh
developer: Bitvise
homepage: https://www.bitvise.com/flowssh
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 5.39
    date: 2016-04-05
changelog: https://www.bitvise.com/flowssh-version-history
client: yes
server: no
library: client
protocols:
    cipher:
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - 3des-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - 3des-cbc
    compression:
        - none
        - zlib
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-1.3.132.0.10   # SEC 2 prime curve secp256k1? Not listed in RFC 5656
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
    kex:
        - ecdh-sha2-1.3.132.0.10
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256 # disabled by default
        - diffie-hellman-group-exchange-sha1   # disabled by default
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-sha2-256
        - hmac-sha1
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
---
* Bitvise FlowSshC/Cpp/Net is a SSH library for C, C++, and .NET.
* 2015-07-10: The information provided here is based on the FlowSshC.h header file,
  as well as the [FlowSsh documentation](https://www.bitvise.com/fsd-index).
