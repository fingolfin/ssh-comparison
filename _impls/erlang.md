---
title: Erlang ssh library
homepage: http://www.erlang.org/doc/man/ssh.html
source-repository: https://github.com/erlang/otp
license: "[Apache-2.0](https://github.com/erlang/otp/blob/maint/LICENSE.txt)"
first-release:
    date: 2005-10-25
latest-release:
    version: 4.7.3 (OTP 21.2.2)
    date: 2018-12-28
changelog: http://www.erlang.org/doc/apps/ssh/notes.html
client: yes
server: yes
library: both
#  SFTP Client + Server, ....
protocols:
    cipher:
        - aes256-ctr                # since version 4.2
        - aes192-ctr                # since version 4.2
        - aes128-ctr
        - aes128-cbc
        - aes128-gcm@openssh.com    # since version 4.2
        - aes256-gcm@openssh.com    # since version 4.2
        - AEAD_AES_128_GCM          # since version 4.2
        - AEAD_AES_256_GCM          # since version 4.2
        - 3des-cbc
        - chacha20-poly1305@openssh.com # since version 4.7.1
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ecdsa-sha2-nistp256   # since version 4.2
        - ecdsa-sha2-nistp384   # since version 4.2
        - ecdsa-sha2-nistp521   # since version 4.2
        - ssh-ed25519
        - ssh-ed448
        - ssh-rsa
        - ssh-dss
        - rsa-sha2-256              # since 4.5
        - rsa-sha2-512              # since 4.5
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - ecdh-sha2-nistp521
        - diffie-hellman-group1-sha1   # disabled by default since 4.5
        - diffie-hellman-group14-sha256      # since 4.5
        - diffie-hellman-group16-sha512      # since 4.5
        - diffie-hellman-group18-sha512      # since 4.5
        - curve25519-sha256                  # since version 4.7.1
        - curve448-sha512                    # since version 4.7.1
        - curve25519-sha256@libssh.org       # since version 4.7.1
        - ext-info-c                         # since 4.5
        - ext-info-s                         # since 4.5
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - AEAD_AES_128_GCM     # since version 4.2
        - AEAD_AES_256_GCM     # since version 4.2
    userauth:
        - publickey
        - password
        - keyboard-interactive
    extension:
        - server-sig-algs                   # since 4.5
---
* Server and client implementation (and library) for the 
  [Erlang](http://www.erlang.org/) programming language.
* Uses OpenSSL crypto library or other libraries with compatible API.
