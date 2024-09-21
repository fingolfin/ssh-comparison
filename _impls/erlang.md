---
title: Erlang ssh library
homepage: https://www.erlang.org/doc/apps/ssh/ssh.html
source-repository: https://github.com/erlang/otp
license: "[Apache-2.0](https://github.com/erlang/otp/blob/maint/LICENSE.txt)"
first-release:
    date: 2005-10-25
latest-release:
    version: 5.2.2 (OTP 27.1)
    date: 2024-09-19
changelog: https://www.erlang.org/doc/apps/ssh/notes.html
client: yes
server: yes
library: both
#  SFTP Client + Server, ....
protocols:
    cipher:
        - aes256-ctr                # since version 4.2
        - aes192-ctr                # since version 4.2
        - aes128-ctr
        - aes256-cbc                # since version 4.8.1
        - aes192-cbc                # since version 4.8.1
        - aes128-cbc
        - aes128-gcm@openssh.com    # since version 4.2
        - aes256-gcm@openssh.com    # since version 4.2
        - AEAD_AES_128_GCM          # since version 4.2, disabled by default
        - AEAD_AES_256_GCM          # since version 4.2, disabled by default
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
        - ssh-ed25519           # since version 4.7.2
        - ssh-ed448             # since version 4.7.2
        - ssh-rsa               # disabled by default since 4.12
        - ssh-dss               # disabled by default since 4.10
        - rsa-sha2-256              # since 4.5
        - rsa-sha2-512              # since 4.5
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - diffie-hellman-group14-sha1  # disabled by default since 4.10
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1 # disabled by default since 4.10
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
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha1-96         # since version 4.8.1, disabled by default
        - AEAD_AES_128_GCM     # since version 4.2, disabled by default
        - AEAD_AES_256_GCM     # since version 4.2, disabled by default
        - hmac-sha2-256-etm@openssh.com # since version 4.10
        - hmac-sha2-512-etm@openssh.com # since version 4.10
        - hmac-sha1-etm@openssh.com     # since version 4.10
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
