---
title: Termius (iOS)
homepage: https://termius.com/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 8.2.0
    date: 2026-11-11
changelog: https://docs.termius.com/changelog/ios
client: yes
server: no
standalone: client
library: no
platforms:
    - ios

protocols:
    cipher:
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
        - chacha20-poly1305@openssh.com
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
        - ssh-dss
        - ssh-dss-cert-v01@openssh.com
        - ssh-mldsa-44  # since 7.3.3
        - ssh-mldsa-65
        - ssh-mldsa-87
    kex:
        - ext-info-c
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - mlkem768x25519-sha256 # since 6.3.0
        - mlkem512-sha256
        - mlkem768-sha256
        - mlkem1024-sha384
    mac:
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1
        - hmac-sha1-etm@openssh.com
        - hmac-sha1-96
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5
        - hmac-md5-etm@openssh.com
        - hmac-md5-96
        - hmac-md5-96-etm@openssh.com
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
        - umac-64@openssh.com
        - umac-64-etm@openssh.com
        - umac-128@openssh.com
        - umac-128-etm@openssh.com
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-libssh2_1.11.1"
based-on: "[libssh2](/impls/libssh2.html)"
---
* Mobile client for iOS (iPhone, iPad).
* There is also an [Android version](/impls/serverauditor-android.html).
* Available on the
  [Apple App Store](https://itunes.apple.com/us/app/id549039908).
* Formerly named Serverauditor.
* 2015-12-05: Version 2.2.1 for iOS identifies itself on the wire as
  `SSH-2.0-libssh2_1.4.3`.
* 2016-05-03: Version 2.2.5 for iOS identifies itself on the wire as
  `SSH-2.0-libssh2_1.7.0`.
* 2026-11-21: Version 8.2.0 for iOS identifies itself on the wire as
  `SSH-2.0-libssh2_1.11.1`. Its host key and kex name-lists end in a
  comma, that is, an empty name.
