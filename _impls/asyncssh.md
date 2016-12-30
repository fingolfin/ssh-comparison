---
title: AsyncSSH
homepage: http://asyncssh.readthedocs.io/
source-repository: https://github.com/ronf/asyncssh
license: "[EPL v1.0](http://www.eclipse.org/legal/epl-v10.html)"
first-release:
    date: 2013-09-14
latest-release:
    version: 1.8.1
    date: 2016-12-29
changelog: http://asyncssh.readthedocs.io/en/latest/changes.html
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305@openssh.com             # since 1.0.0
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-gcm@openssh.com                    # since 0.9.0
        - aes128-gcm@openssh.com                    # since 0.9.0
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - 3des-cbc
        - blowfish-cbc
        - cast128-cbc
        - arcfour256
        - arcfour128
        - arcfour
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ssh-ed25519-cert-v01@openssh.com          # since 1.0.0
        - ecdsa-sha2-nistp521-cert-v01@openssh.com  # since 1.0.0
        - ecdsa-sha2-nistp384-cert-v01@openssh.com  # since 1.0.0
        - ecdsa-sha2-nistp256-cert-v01@openssh.com  # since 1.0.0
        - ssh-rsa-cert-v01@openssh.com              # since 1.0.0
        - ssh-dss-cert-v01@openssh.com              # since 1.0.0
        #- ssh-rsa-cert-v00@openssh.com             # removed in 1.3.2
        #- ssh-dss-cert-v00@openssh.com             # removed in 1.3.2
        - ssh-ed25519                               # since 1.0.0
        - ecdsa-sha2-nistp521                       # since 1.0.0
        - ecdsa-sha2-nistp384                       # since 1.0.0
        - ecdsa-sha2-nistp256                       # since 1.0.0
        - rsa-sha2-256                              # since 1.7.0
        - rsa-sha2-512                              # since 1.7.0
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256                         # since 1.8.0
        - curve25519-sha256@libssh.org              # since 1.0.0
        - ecdh-sha2-nistp521                        # since 1.0.0
        - ecdh-sha2-nistp384                        # since 1.0.0
        - ecdh-sha2-nistp256                        # since 1.0.0
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group16-sha512             # since 1.7.0
        - diffie-hellman-group18-sha512             # since 1.7.0
        - diffie-hellman-group14-sha256             # since 1.7.0
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - ext-info-c                                # since 1.7.0
    mac:
        - umac-64-etm@openssh.com                   # since 1.8.0
        - umac-128-etm@openssh.com                  # since 1.8.0
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-sha2-256-96-etm@openssh.com
        - hmac-sha2-512-96-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - umac-64@openssh.com                       # since 1.8.0
        - umac-128@openssh.com                      # since 1.8.0
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5
        - hmac-sha2-256-96
        - hmac-sha2-512-96
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - publickey
        - keyboard-interactive
        - password
    extension:
        - server-sig-algs                           # since 1.7.0

first_kex_packet_follows: 1
---
* A Python asyncio implementation of SSHv2 and SFTPv3
* Supports TCP/IP, UNIX domain socket, and X11 forwarding
* Supports OpenSSH ssh-agent and agent forwarding on UNIX
* Supports PuTTY Pageant agent on Windows
* Supports OpenSSH-compatible known_hosts and authorized_keys files
