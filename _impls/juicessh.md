---
title: JuiceSSH
homepage: https://juicessh.com/
license: Proprietary
first-release:
    date: 2012-12   # according to their website
latest-release:
    version: 2.0.9
    date: 2015-10-15
changelog: https://juicessh.com/changelog
client: yes
server: no
#platforms:
#    - android
#
remarks: |
    * Android client
    * Available at the [Google Play](https://play.google.com/store/apps/details?id=com.sonelli.juicessh)
    * Based on [JSch](/impls/jsch.html)
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
        - arcfour           # supported, but not enabled by default
        - arcfour128        # supported, but not enabled by default
        - arcfour256        # supported, but not enabled by default
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha256 
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha2-256
        - hmac-md5-96
        - hmac-sha1-96
        #  hmac-sha2-512 implemented, but disabled in source. Quote from JSch.java:
        #  The "hmac-sha2-512" will require the key-length 2048 for DH,
        #   but Sun's JCE has not allowed to use such a long key.
    userauth:
        - password
        - publickey
        - keyboard-interactive
        - gssapi-with-mic
---
