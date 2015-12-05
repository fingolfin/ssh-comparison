---
title: MindTerm
homepage: http://www.cryptzone.com/products/mindterm/
# http://www.cryptzone.com/downloadcenter/mindterm
# http://download.cryptzone.com/files/Mindterm_API_Documentation/index.html
license: Proprietary
first-release:
    date: 1998-11-13    # according to Wikipedia
latest-release:
    version: 4.1.5
    date: 2014-04-01
#changelog: TODO
client: yes
server: no
remarks: |
    * Pure Java implementation.
    * 2015-07-10:  The information provided here is mostly based on the
      [MindTerm Datasheet](http://www.cryptzone.com/pdfs/Cryptzone_Datasheet_MindTerm_EN.pdf)
      as well as the
      [MindTerm 2.0 User's Guide](https://www.astro.umd.edu/resources/internal/ssh/MindTerm_User.pdf).
      But since MindTerm is at version 4.x now, there may be inaccuracies!

# SOCKS, 
protocols:
    cipher:
        - 3des-cbc
        - 3des-ecb
        - 3des-cfb
        - 3des-ofb
        - 3des-ctr
        - blowfish-cbc
        - blowfish-ecb
        - blowfish-cfb
        - blowfish-ofb
        - blowfish-ctr
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - rijndael128-cbc
        - rijndael192-cbc
        - rijndael256-cbc
        - rijndael-cbc@lysator.liu.se
        - twofish128-ctr
        - twofish128-cbc
        - twofish192-ctr
        - twofish192-cbc
        - twofish256-ctr
        - twofish256-cbc
        - twofish-cbc
        - twofish-ecb
        - twofish-cfb
        - twofish-ofb
        - cast128-cbc
        - cast128-ecb
        - cast128-cfb
        - cast128-ofb
        - idea-cbc
        - idea-ecb
        - idea-cfb
        - idea-ofb
        - arcfour
        - arcfour128
        - arcfour256
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
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
    mac:
        - hmac-sha1
        - hmac-md5
        - hmac-ripemd160
        - hmac-sha1-96
        - hmac-md5-96
        - hmac-ripemd160-96
        - hmac-ripemd160@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha256@ssh.com
        - hmac-sha256-2@ssh.com
        - hmac-sha512@ssh.com
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - hostbased
        - gssapi-with-mic           # only OID 1.2.840.113554.1.2.2 / Kerberos
        #- rhosts           # ???
        #- rhostsrsa        # ???
        #- tis              # keyboard-interactive sub-method?
        #- kerberos         # ???
        #- kerbtgt          # ???
        #- securid          # keyboard-interactive sub-method?
        #- cryptocard       # keyboard-interactive sub-method?
---
