---
layout: impl

title: Tectia SSH
homepage: http://www.ssh.com/products/tectia-ssh
license: Proprietary
first-release:
    date: 1995-07
latest-release:
    version: 6.4.6
    date: 2014-01-24
#changelog: TODO
client: yes
server: yes
remarks: |
    * Formerly known as just "SSH" or "ssh.com"
    * Strictly speaking, the Tectica SSH client and server are two separate
      products.
    * The information here is based on the Tectia SSH manual, in particular
      [ssh-server-config](https://support.ssh.com/manuals/server-admin/64/ssh-server-config.html)
      as well as the list of
      [supported user authentication methods](https://support.ssh.com/manuals/server-admin/64/server-auth-supported-methods.html).
protocols:
    cipher:
        - 3des-cbc
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - arcfour
        - blowfish-cbc
        - twofish-cbc
        - twofish128-cbc
        - twofish192-cbc
        - twofish256-cbc
        - crypticore128@ssh.com
        - seed-cbc@ssh.com
    compression:
        - none
        - zlib
    hostkey:
        - ssh-dss
        - ssh-dss-sha224@ssh.com
        - ssh-dss-sha256@ssh.com
        - ssh-dss-sha384@ssh.com
        - ssh-dss-sha512@ssh.com
        - ssh-rsa
        - ssh-rsa-sha224@ssh.com
        - ssh-rsa-sha256@ssh.com
        - ssh-rsa-sha384@ssh.com
        - ssh-rsa-sha512@ssh.com
        - x509v3-sign-dss
        - x509v3-sign-dss-sha224@ssh.com
        - x509v3-sign-dss-sha256@ssh.com
        - x509v3-sign-dss-sha384@ssh.com
        - x509v3-sign-dss-sha512@ssh.com
        - x509v3-sign-rsa
        - x509v3-sign-rsa-sha224@ssh.com
        - x509v3-sign-rsa-sha256@ssh.com
        - x509v3-sign-rsa-sha384@ssh.com
        - x509v3-sign-rsa-sha512@ssh.com
    kex:
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha224@ssh.com
        - diffie-hellman-group14-sha256@ssh.com
        - diffie-hellman-group15-sha256@ssh.com
        - diffie-hellman-group15-sha384@ssh.com
        - diffie-hellman-group16-sha384@ssh.com
        - diffie-hellman-group16-sha512@ssh.com
        - diffie-hellman-group18-sha512@ssh.com
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha224@ssh.com
        - diffie-hellman-group-exchange-sha384@ssh.com
        - diffie-hellman-group-exchange-sha512@ssh.com
    mac:
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha2-256
        - hmac-sha256-2@ssh.com
        - hmac-sha224@ssh.com
        - hmac-sha256@ssh.com
        - hmac-sha384@ssh.com
        - hmac-sha2-512
        - hmac-sha512@ssh.com
        - crypticore-mac@ssh.com
        - hmac-md5
        - hmac-md5-96
    userauth:
        - password
        - publickey
        - hostbased
        - keyboard-interactive
        - gssapi-with-mic
        #- PAM               # through keyboard-interactive / Unix only
        #- RSA SecurID       # through keyboard-interactive
        #- RADIUS            # through keyboard-interactive
        #- LAM               # through keyboard-interactive / AIX only
---
