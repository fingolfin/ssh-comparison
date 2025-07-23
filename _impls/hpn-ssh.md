---
title: HPN-SSH
homepage: https://www.psc.edu/hpn-ssh-home/
source-repository: https://github.com/rapier1/hpn-ssh
license: "[BSD](https://github.com/rapier1/hpn-ssh/blob/master/LICENCE)"
first-release:
    date: 2004
latest-release:
    version: 18.7.0
    date: 2025-04-10
changelog: https://github.com/rapier1/hpn-ssh/releases
client: yes
server: yes

protocols:
    cipher:
        - chacha20-poly1305-mt@hpnssh.org
        - chacha20-poly1305@openssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - aes128-cbc
        - 3des-cbc
        - aes192-cbc
        - aes256-cbc
    compression:
        - none
        - zlib@openssh.com
    hostkey:
        - rsa-sha2-256
        - rsa-sha2-512
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - ssh-rsa
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com
        - sk-ecdsa-sha2-nistp256@openssh.com
        - sk-ssh-ed25519-cert-v01@openssh.com
        - sk-ssh-ed25519@openssh.com
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - ext-info-c
        - ext-info-s
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
        - sntrup761x25519-sha512@openssh.com
        - sntrup761x25519-sha512
        - mlkem768x25519-sha256
    mac:
        - none
        - umac-64-etm@openssh.com
        - umac-128-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - umac-64@openssh.com
        - umac-128@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - hmac-md5
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - hostbased
        - publickey-hostbound-v00@openssh.com
    extension:
        - ext-info-in-auth@openssh.com
        - ping@openssh.com
        - publickey-hostbound@openssh.com
        - server-sig-algs

first_kex_packet_follows: 0
---
* A high performance soft fork of OpenSSH that can provide significnatly faster throughput for bulk data transfers over a wide range of network paths.
