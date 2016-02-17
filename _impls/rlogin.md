---
title: RLogin
homepage: http://nanno.dip.jp/softlib/man/rlogin/
source-repository: TODO
# http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/
license: "TODO"
#first-release:
#    date: TODO
latest-release:
    version: 2.20.0
    date: 2016-08-21
changelog: TODO
client: yes
server: no
library: no
platforms:
    - windows
remarks: |
    * Only available in Japanes.
    * The list of supported protocols is based on what the website reports.

protocols:
    cipher:
        - 3des-cbc
        - 3des-ctr
        - blowfish-cbc
        - blowfish-ctr
        - idea-cbc
        - idea-ctr
        - cast128-cbc
        - cast128-ctr
        - arcfour
        - arcfour128
        - arcfour256
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - twofish128-cbc
        - twofish192-cbc
        - twofish256-cbc
        - twofish128-ctr
        - twofish192-ctr
        - twofish256-ctr
        - serpent128-cbc
        - serpent192-cbc
        - serpent256-cbc
        - serpent128-ctr
        - serpent192-ctr
        - serpent256-ctr
        - camellia128-cbc
        - camellia192-cbc
        - camellia256-cbc
        - camellia128-ctr
        - camellia192-ctr
        - camellia256-ctr
        - seed-cbc@ssh.com
        - seed-ctr@ssh.com
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - chacha20-poly1305@openssh.com
    compression:
        - none
        - zlib
        - zlib@openssh.com
    hostkey:
        - ssh-rsa
        - ssh-dss
        - ssh-ed25519
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
#    kex:
#        - unknown
    mac:
        - hmac-md5
        - hmac-md5-96
        - hmac-sha1
        - hmac-sha1-96
        - hmac-ripemd160
        - hmac-whirlpool
        - hmac-sha2-256
        - hmac-sha2-512
#umac-32/64/96/128,
#*-etm@openssh.com

#    userauth:
#        - unknown

---
* Website also lists these HMACs: "umac-32/64/96/128, *-etm@openssh.com"; but this is
  ambiguous (are there -etm variants of all hmacs, or just of the umac family?), and moreover,
  umac-32 and umac-96 seem to be properiatery additions to the umac family.
* Website does not list support key exchange methods. Since testing the software requires
  knowledge of Japanese, this information is missing for now.
