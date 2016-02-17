---
title: Prompt 2
homepage: https://www.panic.com/prompt/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 2.5
    date: 2016-02-16
#changelog: TODO
client: yes
server: no
platforms:
    - iphone
    - ipad
protocols:
    cipher:
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
        - ssh-rsa
        - ssh-dss
    kex:
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
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
* Available on the [Apple App Store](https://itunes.apple.com/us/app/id917437289)
* 2015-07-10: Version 2.1.1 identifies itself on the wire as `SSH-2.0-OpenSSH_5.4`
* 2016-02-17: Version 2.5 identifies itself on the wire as `SSH-2.0-OpenSSH_5.4`
* Vendor provides a [list of supported protocols](https://library.panic.com/prompt/prompt-key-security/)
