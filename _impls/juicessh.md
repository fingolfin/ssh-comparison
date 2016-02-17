---
title: JuiceSSH
homepage: https://juicessh.com/
license: Proprietary
first-release:
    date: 2012-12   # according to their website
latest-release:
    version: 2.1.0
    date: 2015-12-16
changelog: https://juicessh.com/changelog
client: yes
server: no
platforms:
    - android

protocols:
    cipher:
        - aes128-ctr
        - aes128-cbc
        - 3des-ctr
        - 3des-cbc
        - blowfish-cbc
        - aes192-ctr
        - aes192-cbc
        - aes256-ctr
        - aes256-cbc
    compression:
        - zlib@openssh.com
        - zlib
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
    kex:
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - password
        - publickey
        - keyboard-interactive
        - gssapi-with-mic

first_kex_packet_follows: 0
ident: "SSH-2.0-JuiceSSH"
based-on: "[JSch](/impls/jsch.html)"
---
* Android client
* Available on [Google Play](https://play.google.com/store/apps/details?id=com.sonelli.juicessh)
