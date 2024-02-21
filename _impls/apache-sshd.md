---
title: Apache SSHD
homepage: http://mina.apache.org/sshd-project/
source-repository: http://git-wip-us.apache.org/repos/asf/mina-sshd.git
license: "[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)"
first-release:
    date: 2009      # according to Wikipedia
latest-release:
    version: 2.4.0
    date: 2020-01-17
changelog: "https://github.com/apache/mina-sshd/blob/master/CHANGES.md"
client: yes
server: yes
library: both
protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - arcfour256
        - arcfour128
        - aes128-cbc
        - 3des-cbc
        - blowfish-cbc
        - aes192-cbc
        - aes256-cbc
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ssh-dss-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - rsa-sha2-256
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512
        - rsa-sha2-512-cert-v01@openssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - sk-ecdsa-sha2-nistp256@openssh.com
        - ssh-ed25519
        - ssh-ed25519-cert-v01@openssh.com
        - sk-ssh-ed25519@openssh.com
    kex:
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512                 # was brokeb before 1.1.0
        - hmac-sha1-96
        - hmac-md5-96
        - hmac-sha1-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
    userauth:
        - keyboard-interactive
        - password
        - publickey
        - gssapi-with-mic               # only OID 1.2.840.113554.1.2.2 / Kerberos
    extension:
        - kex-strict-c-v00@openssh.com  # since 2.12.0
        - kex-strict-s-v00@openssh.com  # since 2.12.0
---
* Pure Java implementation.
