---
title: Dropbear
homepage: https://matt.ucc.asn.au/dropbear/dropbear.html
source-repository: https://secure.ucc.asn.au/hg/dropbear/
license: "[MIT style](https://secure.ucc.asn.au/hg/dropbear/raw-file/tip/LICENSE)"
first-release:
    date: 2003-04-06    # according to CHANGES file
latest-release:
    version: 2015.71
    date: 2015-12-03
changelog: https://matt.ucc.asn.au/dropbear/CHANGES
client: yes
server: yes
library: no

# X11 forwarding, and authentication-agent forwarding, ...
protocols:
    cipher:
        - aes128-ctr
        - aes256-ctr
        #- twofish256-ctr           # Disabled by default
        #- twofish128-ctr           # Disabled by default
        - aes128-cbc
        - aes256-cbc
        - twofish256-cbc
        - twofish-cbc
        - twofish128-cbc
        - 3des-ctr
        - 3des-cbc
        #- blowfish-cbc             # Disabled by default
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-rsa
        - ssh-dss
    kex:
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - kexguess2@matt.ucc.asn.au     # Dropbear extension (only documented in their CHANGES file?)
    mac:
        - hmac-sha1-96
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-md5
    userauth:
        - publickey
        - password
        - keyboard-interactive

first_kex_packet_follows: 1
ident: "SSH-2.0-dropbear_2015.71"
---
* Server and client for POSIX-based platforms.
* [Wikipedia](https://en.wikipedia.org/wiki/Dropbear_%28software%29)
