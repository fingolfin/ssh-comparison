---
layout: impl

title: OpenSSH
homepage: http://www.openssh.com/
source-repository: https://anongit.mindrot.org/openssh.git
# http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/
license: "[BSD](http://cvsweb.openbsd.org/cgi-bin/cvsweb/~checkout~/src/usr.bin/ssh/LICENCE)"
first-release:
    date: 1999-12-01    # according to Wikipedia
latest-release:
    version: 7.1
    date: 2015-08-21
changelog: http://news.gmane.org/gmane.network.openssh.announce
# perhaps http://www.openssh.com/txt/ is better changelog link?
client: yes
server: yes
remarks: |
    * Probably the most widely deployed SSH implementation.
    * There are actually two versions: Regular OpenSSH is part of OpenBSD.
      This version is hosted in the [OpenBSD CVS repository](http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/).
      For everybody else, there is "Portable OpenSSH". This document is
      refering to the portable version, since that is what the majority
      of OpenSSH users is using (as they are not running OpenBSD).

protocols:
    cipher:
        - chacha20-poly1305@openssh.com # since 6.5
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - aes128-gcm@openssh.com        # since 6.2
        - aes256-gcm@openssh.com        # since 6.2
        - arcfour256                    # will be disabled by default in a future version
        - arcfour128                    # will be disabled by default in a future version
        - aes128-cbc
        - 3des-cbc
        - blowfish-cbc                  # will be disabled by default in a future version
        - cast128-cbc                   # will be disabled by default in a future version
        - aes192-cbc
        - aes256-cbc
        - arcfour                       # will be disabled by default in a future version
        - rijndael-cbc@lysator.liu.se   # will be disabled by default in a future version
    compression:
        - none
        - zlib@openssh.com
        - zlib
    hostkey:
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com  # disabled by default in 7.0
        - ssh-rsa-cert-v00@openssh.com
        - ssh-dss-cert-v00@openssh.com  # disabled by default in 7.0
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp521
        - ssh-ed25519
        - ssh-rsa
        - ssh-dss                       # disabled by default in 7.0
    kex:
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1   # disabled by default in 7.0, susceptible to logjam
    mac:
        - umac-64-etm@openssh.com
        - umac-128-etm@openssh.com
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - umac-64@openssh.com
        - umac-128@openssh.com
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-md5-etm@openssh.com
        - hmac-ripemd160-etm@openssh.com
        - hmac-sha1-96-etm@openssh.com
        - hmac-md5-96-etm@openssh.com
        - hmac-md5
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
        - hmac-sha1-96
        - hmac-md5-96
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - hostbased
---
