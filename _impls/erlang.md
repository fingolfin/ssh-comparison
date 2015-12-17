---
title: Erlang ssh library
homepage: http://www.erlang.org/doc/man/ssh.html
source-repository: https://github.com/erlang/otp
license: "[Apache-2.0](https://github.com/erlang/otp/blob/maint/LICENSE.txt)"
first-release:
    date: 2005-10-25
# From http://www.erlang.org/download/otp_src_R10B-8.readme: 
# OTP-5631  The previously undocumented and UNSUPPORTED ssh
#	        application has been updated and documented. This
#	        release of the ssh application is still considered to
#	        be a beta release and (if necessary) there could still
#	        be changes in its API before it reaches 1.0.
latest-release:
    version: 4.2 (OTP 18.2)
    date: 2015-12-15
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
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ecdsa-sha2-nistp256   # since version 4.2
        - ecdsa-sha2-nistp384   # since version 4.2
        - ecdsa-sha2-nistp521   # since version 4.2
        - ssh-rsa
        - ssh-dss
    kex:
       - ecdh-sha2-nistp256
       - ecdh-sha2-nistp384
       - diffie-hellman-group14-sha1
       - diffie-hellman-group-exchange-sha256
       - diffie-hellman-group-exchange-sha1
       - ecdh-sha2-nistp521
       - diffie-hellman-group1-sha1
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
---
* Server and client implementation (and library) for the 
  [Erlang](http://www.erlang.org/) programming language.
* Uses OpenSSL crypto library
