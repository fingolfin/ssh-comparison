---
title: Net::SSH::Perl
homepage: https://metacpan.org/pod/Net::SSH::Perl
source-repository: https://github.com/briandfoy/net-ssh-perl
license: "Dual license: [GPLv1](https://github.com/briandfoy/net-ssh-perl/blob/master/LICENSE_GNU) or [Artistic](https://github.com/briandfoy/net-ssh-perl/blob/master/LICENSE_ARTISTIC)"
first-release:
    date: 2001-01-10
latest-release:
    version: 2.144
    date: 2026-01-14
changelog: https://github.com/briandfoy/net-ssh-perl/blob/master/Changes
client: yes
server: no
library: client

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-cbc
        - aes192-cbc
        - aes128-cbc
        - 3des-cbc
        - blowfish-cbc
        - arcfour
    compression:
        - none
        - zlib
    hostkey:
        - ssh-ed25519
        - rsa-sha2-512
        - rsa-sha2-256
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
        - ssh-rsa
        - ssh-dss
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - curve25519-sha256@libssh.org
        - curve25519-sha256
        - ext-info-c
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-256
        - hmac-sha1
        - hmac-md5
    userauth:
        - password
        - publickey
        - keyboard-interactive
    extension:
        - server-sig-algs
---
* Net::SSH::Perl is an all-Perl module implementing an SSH (Secure Shell) client.
