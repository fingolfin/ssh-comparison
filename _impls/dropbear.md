---
title: Dropbear
homepage: https://matt.ucc.asn.au/dropbear/dropbear.html
source-repository: https://secure.ucc.asn.au/hg/dropbear/
license: "[MIT style](https://secure.ucc.asn.au/hg/dropbear/raw-file/tip/LICENSE)"
first-release:
    date: 2003-04-06    # according to CHANGES file
latest-release:
    version: 2022.82
    date: 2022-04-01
changelog: https://matt.ucc.asn.au/dropbear/CHANGES
client: yes
server: yes
library: no

# X11 forwarding, and authentication-agent forwarding, ...
protocols:
    cipher:
        - aes128-ctr
        - aes256-ctr
        - chacha20-poly1305@openssh.com  # since 2020.79
        # - aes128-gcm@openssh.com        # since 2020.79, disabled by default
        # - aes128-gcm@openssh.com        # since 2020.79, disabled by default

        # - aes128-cbc          # disabled by default
        # - aes256-cbc          # disabled by default
        # - 3des-ctr            # disabled by default
        # - 3des-cbc            # disabled by default
        # - 3des-cbc            # disabled by default
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-rsa
        - rsa-sha2-256                   # since 2022.82
        - ssh-dss
        - ssh-ed25519                    # since 2020.79
        - sk-ssh-ed25519@openssh.com     # since 2022.82
        - sk-ecdsa-sha2-nistp256@openssh.com     # since 2022.82
    kex:
        - curve25519                     # since 2018.76
        - curve25519-sha256@libssh.org   # since 2013.62
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256   # since 2018.76
        # - diffie-hellman-group16-sha512   # since 2018.76. disabled by default
        # - diffie-hellman-group1-sha1    # disabled by default
        - kexguess2@matt.ucc.asn.au     # Dropbear extension (only documented in their CHANGES file?)
    mac:
        # - hmac-sha1-96   # disabled by default
        - hmac-sha1
        - hmac-sha2-256
    userauth:
        - publickey
        - password
        - keyboard-interactive

first_kex_packet_follows: 1
ident: "SSH-2.0-dropbear_2022.82"
---
* Server and client for POSIX-based platforms.
* [Wikipedia](https://en.wikipedia.org/wiki/Dropbear_%28software%29)
