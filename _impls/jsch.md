---
title: JSch
homepage: http://www.jcraft.com/jsch/
#source-repository: http://git.jcraft.com/jsch.git/
license: "[BSD style](http://www.jcraft.com/jsch/LICENSE.txt)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 0.1.53
    date: 2015-06-05
changelog: http://www.jcraft.com/jsch/ChangeLog
client: true
server: unknown
remarks: |
    * Pure Java implementation.
    * 2015-07-10: There is a [git repository](http://git.jcraft.com/jsch.git)
    but it contains only a single commit with an outdated version.
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
        - gssapi-with-mic           # only OID 1.2.840.113554.1.2.2 / Kerberos
---
