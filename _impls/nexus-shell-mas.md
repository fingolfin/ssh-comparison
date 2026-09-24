---
title: Nexus Shell (TestFlight / Mac App Store build)
homepage: https://nexusshell.app/
developer: Nexus Shell
license: Proprietary
first-release:
    date: 2026-05-07
latest-release:
    version: 1.6.9
    date: 2026-08-07
changelog: https://nexusshell.app/releases
client: yes
server: no
library: no
platforms:
    - macos
based-on: "[libssh2 1.11.1](/impls/libssh2.html)"

protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes256-gcm@openssh.com
        - aes128-gcm@openssh.com
        - aes256-ctr
        - aes192-ctr
        - aes128-ctr
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes192-cbc
        - aes128-cbc
        - blowfish-cbc
        - arcfour128
        - arcfour
        - cast128-cbc
        - 3des-cbc
    compression:
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519
        - ssh-ed25519-cert-v01@openssh.com
        - rsa-sha2-512
        - rsa-sha2-256
        - rsa-sha2-512-cert-v01@openssh.com
        - rsa-sha2-256-cert-v01@openssh.com
        - ssh-rsa
        - ssh-rsa-cert-v01@openssh.com
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha1
        - ext-info-c
        - kex-strict-c-v00@openssh.com
    mac:
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
    userauth:
        - password
        - publickey
    extension:
        - server-sig-algs

first_kex_packet_follows: 0
ident: "SSH-2.0-libssh2_1.11.1"
---
* This entry covers the sandboxed TestFlight / Mac App Store build, which
  embeds libssh2 1.11.1 and OpenSSL 3.5.4.
* The direct-download and Homebrew builds delegate SSH transport to the
  macOS system `ssh` executable. Their protocol support therefore depends on
  the OpenSSH version shipped with the installed macOS release and is not
  duplicated in this entry.
* The algorithm lists above were queried from the exact arm64 static archives
  shipped with Nexus Shell 1.6.9 using `libssh2_session_supported_algs()`.
  This build reports only `none` for compression. The application exposes
  password and public-key authentication.
* Submitted by the Nexus Shell developer; corrections are welcome.
