---
title: PuTTY
homepage: https://www.chiark.greenend.org.uk/~sgtatham/putty/
source-repository: git://git.tartarus.org/simon/putty.git
license: "[MIT style](http://www.chiark.greenend.org.uk/~sgtatham/putty/licence.html)"
first-release:
    date: 1998
# It is not clear when exactly the first *public* PuTTY release was. The
# changelog starts at version 0.45, released 1999-01-22, and this is
# also the date Wikipedia lists. I contacted Simon Tatham about this,
# and he cannot fully reconstruct when the first release was. But with
# help from the Internet archive, it is clear that already version 0.43
# was released to the public, at the latest in in December 1998.
# The _name_ 'PuTTY' appeared around May/June 1998, and according to Simon,
# the development code made its first successful SSH connection 1998-05-29.
# So, all in all, this is why I give 1998 as date of the first release.
latest-release:
    version: 0.81
    date: 2024-04-15
changelog: https://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html
client: yes
server: no
platforms:
    - windows

protocols:
    cipher:
        - 3des-cbc
        - 3des-ctr
        - des-cbc
        - des-cbc@ssh.com
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - arcfour128
        - arcfour256
        - blowfish-cbc
        - blowfish-ctr
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ssh-ed25519
        - ssh-ed448
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - curve448-sha512
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - sntrup761x25519-sha512@openssh.com
        - rsa1024-sha1
        - rsa2048-sha256
        - gss-gex-sha1-*
        - gss-group1-sha1-*
        - gss-group14-sha1-*
        - gss-group14-sha256-*
        - gss-group15-sha512-*
        - gss-group16-sha512-*
        - gss-group17-sha512-*
        - gss-group18-sha512-*
        - gss-curve25519-sha256-*
        - gss-nistp256-sha256-*
        - gss-nistp384-sha384-*
        - gss-nistp521-sha512-*
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-etm@openssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - gssapi-keyex
    extension:
        - server-sig-algs
---
* [Wikipedia](https://en.wikipedia.org/wiki/PuTTY)
