---
title: Net::SSH
homepage: https://net-ssh.github.io/net-ssh/
source-repository: https://github.com/net-ssh/net-ssh
license: "[MIT style](https://github.com/net-ssh/net-ssh/blob/master/LICENSE.txt)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 7.2.3
    date: 2024-04-02
changelog: https://github.com/net-ssh/net-ssh/blob/master/CHANGES.txt
client: yes
server: no
library: client

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - 3des-cbc                      # deprecated in 6.0, will be removed in 8.0
        - 3des-ctr                      # deprecated in 6.0, will be removed in 8.0
        - aes128-cbc                    # deprecated in 6.0, will be removed in 8.0
        - aes192-cbc                    # deprecated in 6.0, will be removed in 8.0
        - aes256-cbc                    # deprecated in 6.0, will be removed in 8.0
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        #- arcfour                      # removed in 6.0
        #- arcfour128                   # removed in 6.0
        #- arcfour256                   # removed in 6.0
        - blowfish-cbc                  # deprecated in 6.0, will be removed in 8.0
        - blowfish-ctr                  # deprecated in 6.0, will be removed in 8.0
        #- camellia128-cbc
        #- camellia128-cbc@openssh.org  # removed in 4.0
        #- camellia128-ctr              # removed in 4.0
        #- camellia128-ctr@openssh.org  # removed in 4.0
        #- camellia192-cbc              # removed in 4.0
        #- camellia192-cbc@openssh.org  # removed in 4.0
        #- camellia192-ctr              # removed in 4.0
        #- camellia192-ctr@openssh.org  # removed in 4.0
        #- camellia256-cbc              # removed in 4.0
        #- camellia256-cbc@openssh.org  # removed in 4.0
        #- camellia256-ctr              # removed in 4.0
        #- camellia256-ctr@openssh.org  # removed in 4.0
        - cast128-cbc                   # deprecated in 6.0, will be removed in 8.0
        - cast128-ctr                   # deprecated in 6.0, will be removed in 8.0
        - idea-cbc                      # deprecated in 6.0, will be removed in 8.0
        - rijndael-cbc@lysator.liu.se   # deprecated in 6.0, will be removed in 8.0
        #- none                         # deprecated in 6.0, will be removed in 8.0
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-dss   # deprecated in 6.0, will be removed in 8.0
        - ssh-ed25519
        - ssh-rsa
        - rsa-sha2-256
        - rsa-sha2-512
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        #- ssh-rsa-cert-v00@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
    kex:
        - curve25519-sha256
        - diffie-hellman-group-exchange-sha1    # deprecated in 6.0, will be removed in 8.0
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group1-sha1            # deprecated in 6.0, will be removed in 8.0
        - diffie-hellman-group14-sha1
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
    mac:
        - hmac-md5              # deprecated in 6.0, will be removed in 8.0
        - hmac-md5-96           # deprecated in 6.0, will be removed in 8.0
        - hmac-ripemd160        # deprecated in 6.0, will be removed in 8.0
        - hmac-sha1             # for backward compatibility
        - hmac-sha1-96          # deprecated in 6.0, will be removed in 8.0
        - hmac-sha2-256
        - hmac-sha2-256-96      # deprecated in 6.0, will be removed in 8.0
        - hmac-sha2-256-etm
        - hmac-sha2-512
        - hmac-sha2-512-96      # deprecated in 6.0, will be removed in 8.0
        - hmac-sha2-512-etm
        #- none                 # deprecated in 6.0, will be removed in 8.0
    userauth:
        - password
        - publickey
        - hostbased
        - keyboard-interactive
---
* Ruby implementation of the SSH2 client protocol, based on OpenSSL
