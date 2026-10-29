---
title: Net::SSH
homepage: https://net-ssh.github.io/net-ssh/
source-repository: https://github.com/net-ssh/net-ssh
license: "[MIT style](https://github.com/net-ssh/net-ssh/blob/master/LICENSE.txt)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 8.0.4
    date: 2026-10-25
changelog: https://github.com/net-ssh/net-ssh/blob/master/CHANGES.txt
client: yes
server: no
library: client

protocols:
    cipher:
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com
        - 3des-cbc                      # disabled by default in 8.0
        - 3des-ctr                      # disabled by default in 8.0
        - aes128-cbc                    # disabled by default in 8.0
        - aes192-cbc                    # disabled by default in 8.0
        - aes256-cbc                    # disabled by default in 8.0
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        #- arcfour                      # removed in 6.0
        #- arcfour128                   # removed in 6.0
        #- arcfour256                   # removed in 6.0
        - blowfish-cbc                  # disabled by default in 8.0
        - blowfish-ctr                  # disabled by default in 8.0
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
        - cast128-cbc                   # disabled by default in 8.0
        - cast128-ctr                   # disabled by default in 8.0
        - idea-cbc                      # disabled by default in 8.0
        - rijndael-cbc@lysator.liu.se   # disabled by default in 8.0
        #- none                         # disabled by default in 8.0
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-dss   # disabled by default in 8.0
        - ssh-ed25519
        - ssh-rsa   # disabled by default in 8.0
        - rsa-sha2-256
        - rsa-sha2-512
        #- sk-ecdsa-sha2-nistp256@openssh.com # supported via ssh-agent in 8.0
        #- sk-ssh-ed25519@openssh.com         # supported via ssh-agent in 8.0
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        #- ssh-rsa-cert-v00@openssh.com  # disabled by default & deprecated in 8.0
        - ssh-rsa-cert-v01@openssh.com   # disabled by default in 8.0
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
    kex:
        - curve25519-sha256
        - diffie-hellman-group-exchange-sha1    # disabled by default in 8.0
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group1-sha1            # disabled by default in 8.0
        - diffie-hellman-group14-sha1           # disabled by default in 8.0
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
    mac:
        - hmac-md5              # disabled by default in 8.0
        - hmac-md5-96           # disabled by default in 8.0
        - hmac-ripemd160        # disabled by default in 8.0
        - hmac-ripemd160@openssh.com # disabled by default in 8.0
        - hmac-sha1             # for backward compatibility
        - hmac-sha1-etm@openssh.com # for backward compatibility
        - hmac-sha1-96          # disabled by default in 8.0
        - hmac-sha2-256
        - hmac-sha2-256-96      # disabled by default in 8.0
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-96      # disabled by default in 8.0
        - hmac-sha2-512-etm@openssh.com
        #- none                 # disabled by default in 8.0
    userauth:
        - password
        - publickey
        - hostbased
        - keyboard-interactive
---
* Ruby implementation of the SSH2 client protocol, based on OpenSSL
