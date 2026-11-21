---
title: Prompt 2
homepage: https://www.panic.com/prompt/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 2.6.19
    date: 2022-05-02
changelog: https://help.panic.com/releasenotes/prompt2/
client: yes
server: no
platforms:
    - iphone
    - ipad
# "since" versions are Prompt 2 releases: https://help.panic.com/releasenotes/prompt2/
protocols:
    cipher:
        - chacha20-poly1305
        - chacha20-poly1305@openssh.com # since 2.6.4
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
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
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519   # since 2.6
        - rsa-sha2-512
        - rsa-sha2-256
        - ssh-rsa
        - ssh-dss
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
    mac:
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-256
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
#    userauth:
#        - unknown

first_kex_packet_follows: 0
ident: "SSH-2.0-OpenSSH_5.4"
based-on: "[OpenSSH](/impls/openssh.html)"
---
* iOS client for Apple iPhone and iPad.
* No longer in the App Store; its successor is [Prompt 3](/impls/prompt3.html).
* 2015-07-10: Version 2.1.1 identifies itself on the wire as `SSH-2.0-OpenSSH_5.4`
* 2016-02-17: Version 2.5 identifies itself on the wire as `SSH-2.0-OpenSSH_5.4`
* 2026-11-21: Version 2.6.19 identifies itself on the wire as `SSH-2.0-OpenSSH_5.4`
* Vendor provides a [list of supported protocols](https://help.panic.com/prompt/prompt-key-security/)
