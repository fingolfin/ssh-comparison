---
title: AsyncSSH
homepage: http://asyncssh.readthedocs.io/
source-repository: https://github.com/ronf/asyncssh
license: "[EPL v2.0](https://www.eclipse.org/legal/epl-2.0/faq.php)"
first-release:
    date: 2013-09-14
latest-release:
    version: 2.4.0
    date: 2020-08-29
changelog: http://asyncssh.readthedocs.io/en/latest/changes.html
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305@openssh.com                 # since 1.0.0
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-gcm@openssh.com                        # since 0.9.0
        - aes128-gcm@openssh.com                        # since 0.9.0
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
        - "null"                                        # since 1.9.0
        - sk-ssh-ed25519-cert-v01@openssh.com           # since 2.2.0
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com   # since 2.2.0
        - ssh-ed25519-cert-v01@openssh.com              # since 1.0.0
        - ssh-ed448-cert-v01@openssh.com                # since 1.16.0
        - ecdsa-sha2-nistp521-cert-v01@openssh.com      # since 1.0.0
        - ecdsa-sha2-nistp384-cert-v01@openssh.com      # since 1.0.0
        - ecdsa-sha2-nistp256-cert-v01@openssh.com      # since 1.0.0
        - ecdsa-sha2-1.3.132.0.10-cert-v01@openssh.com  # since 1.13.1
        - ssh-rsa-cert-v01@openssh.com                  # since 1.0.0
        - ssh-dss-cert-v01@openssh.com                  # since 1.0.0
        #- ssh-rsa-cert-v00@openssh.com                 # removed in 1.3.2
        #- ssh-dss-cert-v00@openssh.com                 # removed in 1.3.2
        - x509v3-ssh-ed25519                            # since 2.4.0
        - x509v3-ssh-ed448                              # since 2.4.0
        - x509v3-ecdsa-sha2-nistp521                    # since 1.11.0
        - x509v3-ecdsa-sha2-nistp384                    # since 1.11.0
        - x509v3-ecdsa-sha2-nistp256                    # since 1.11.0
        - x509v3-ecdsa-sha2-1.3.132.0.10                # since 1.13.1
        - x509v3-rsa2048-sha256                         # since 1.11.0
        - x509v3-ssh-rsa                                # since 1.11.0
        - x509v3-ssh-dss                                # since 1.11.0
        - sk-ssh-ed25519@openssh.com                    # since 2.2.0
        - sk-ecdsa-sha2-nistp256@openssh.com            # since 2.2.0
        - ssh-ed25519                                   # since 1.0.0
        - ssh-ed448                                     # since 1.16.0
        - ecdsa-sha2-nistp521                           # since 1.0.0
        - ecdsa-sha2-nistp384                           # since 1.0.0
        - ecdsa-sha2-nistp256                           # since 1.0.0
        - ecdsa-sha2-1.3.132.0.10                       # since 1.13.1
        - rsa-sha2-256                                  # since 1.7.0
        - rsa-sha2-512                                  # since 1.7.0
        - ssh-rsa
        - ssh-dss
    kex:
        - gss-curve25519-sha256-*                       # since 1.18.0
        - gss-curve448-sha512-*                         # since 1.18.0
        - gss-nistp521-sha512-*                         # since 1.18.0
        - gss-nistp384-sha256-*                         # since 1.18.0
        - gss-nistp256-sha256-*                         # since 1.18.0
        - gss-13.3.132.0.10-sha256-*                    # since 1.18.0
        - gss-gex-sha256-*                              # since 1.9.0
        - gss-gex-sha1-*                                # since 1.9.0
        - gss-group14-sha256-*                          # since 1.9.0
        - gss-group15-sha512-*                          # since 1.9.0
        - gss-group16-sha512-*                          # since 1.9.0
        - gss-group17-sha512-*                          # since 1.9.0
        - gss-group18-sha512-*                          # since 1.9.0
        - gss-group14-sha1-*                            # since 1.9.0
        - gss-group1-sha1-*                             # since 1.9.0
        - curve25519-sha256                             # since 1.8.0
        - curve25519-sha256@libssh.org                  # since 1.0.0
        - curve448-sha512                               # since 1.16.0
        - ecdh-sha2-nistp521                            # since 1.0.0
        - ecdh-sha2-nistp384                            # since 1.0.0
        - ecdh-sha2-nistp256                            # since 1.0.0
        - ecdh-sha2-1.3.132.0.10                        # since 1.13.1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha256                 # since 1.7.0
        - diffie-hellman-group15-sha512                 # since 1.9.0
        - diffie-hellman-group16-sha512                 # since 1.7.0
        - diffie-hellman-group17-sha512                 # since 1.9.0
        - diffie-hellman-group18-sha512                 # since 1.7.0
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - rsa2048-sha256                                # since 1.13.1
        - rsa1024-sha1                                  # since 1.13.1
        - ext-info-c                                    # since 1.7.0
    mac:
        - umac-64-etm@openssh.com                       # since 1.8.0
        - umac-128-etm@openssh.com                      # since 1.8.0
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-sha2-256-96-etm@openssh.com
        - hmac-sha2-512-96-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - umac-64@openssh.com                           # since 1.8.0
        - umac-128@openssh.com                          # since 1.8.0
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5
        - hmac-sha2-256-96
        - hmac-sha2-512-96
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - gssapi-keyex                                  # since 1.9.0
        - gssapi-with-mic                               # since 1.9.0
        - hostbased                                     # since 1.13.1
        - publickey
        - keyboard-interactive
        - password
    extension:
        - server-sig-algs                               # since 1.7.0

first_kex_packet_follows: 1
---
* A Python asyncio implementation of SSHv2, SFTPv3, and SCP
* Supports TCP/IP, UNIX domain socket, and X11 forwarding
* Supports OpenSSH ssh-agent and agent forwarding on UNIX
* Supports PuTTY Pageant agent on Windows
* Supports OpenSSH-compatible known_hosts and authorized_keys files
