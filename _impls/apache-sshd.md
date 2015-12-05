---
title: Apache SSHD
homepage: http://mina.apache.org/sshd-project/
source-repository: http://git-wip-us.apache.org/repos/asf/mina-sshd.git
license: "[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)"
first-release:
    date: 2009      # according to Wikipedia
latest-release:
    version: 1.0.0
    date: 2015-08-19
client: yes
server: yes
library: both
protocols:
    cipher:
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - arcfour256
        - arcfour128
        - aes128-cbc
        - 3des-cbc
        - blowfish-cbc
        - aes192-cbc
        - aes256-cbc
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
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1
    mac:
        - hmac-md5
        - hmac-sha1
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - keyboard-interactive
        - password
        - publickey
        - gssapi-with-mic           # only OID 1.2.840.113554.1.2.2 / Kerberos
---
* Pure Java implementation.
* 2015-07-10: Does not seem to provide an overview of changes in new releases?
  But at least there was a
  [release announcment for 0.14.0](http://www.mail-archive.com/users@mina.apache.org/msg05959.html).
