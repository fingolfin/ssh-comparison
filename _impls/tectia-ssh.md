---
title: Tectia SSH
homepage: https://www.ssh.com/products/tectia-ssh
license: Proprietary
first-release:
    date: 1995-07
latest-release:
    version: 6.6.6
    date: 2025-06-16

#Sources for information:
# * https://answers.ssh.com/questions/4164/whats-new-in-tectia-clientserverconnectsecure-6413
# * http://sshcommunicationssecurity.force.com/documents
#   * http://sshcommunicationssecurity.force.com/documents/servlet/fileField?id=0BE330000004GVK

# TODO: seems the z/OS version has a separate version number 6.5.0:
#  https://answers.ssh.com/questions/4152/whats-new-in-tectia-ssh-server-for-ibm-zos-650

changelog: https://www.ssh.com/tectia-server-product-update
client: yes
server: yes
protocols:
    cipher:
        - 3des-cbc
        - AEAD_AES_128_GCM
        - AEAD_AES_256_GCM
        - aes128-cbc
        - aes128-ctr
        - aes128-gcm@openssh.com
        - aes192-cbc
        - aes192-ctr
        - aes256-cbc
        - aes256-ctr
        - aes256-gcm@openssh.com
        - arcfour
        - blowfish-cbc
        - crypticore128@ssh.com
        - seed-cbc@ssh.com
        - twofish128-cbc
        - twofish192-cbc
        - twofish256-cbc
        - twofish-cbc
    compression:
        - none
        - zlib
    hostkey:
        - ecdsa-sha2-nistp256
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - rsa-sha2-256
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512
        - rsa-sha2-512-cert-v01@openssh.com
        - ssh-dss
        - ssh-dss-cert-v01@openssh.com
        - ssh-dss-sha224@ssh.com
        - ssh-dss-sha256@ssh.com
        - ssh-dss-sha384@ssh.com
        - ssh-dss-sha512@ssh.com
        - ssh-ed25519
        - ssh-ed25519-cert-v01@openssh.com
        - ssh-rsa
        - ssh-rsa-cert-v01@openssh.com
        - ssh-rsa-sha224@ssh.com
        - ssh-rsa-sha256@ssh.com
        - ssh-rsa-sha384@ssh.com
        - ssh-rsa-sha512@ssh.com
        - x509v3-ecdsa-sha2-nistp256
        - x509v3-ecdsa-sha2-nistp384
        - x509v3-ecdsa-sha2-nistp521
        - x509v3-rsa2048-sha256
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
        - x509v3-ssh-dss
        - x509v3-ssh-rsa
    kex:
        - curve25519-frodokem1344-sha512@ssh.com
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - curve448-kyber1024-sha512@ssh.com
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha224@ssh.com
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha256@ssh.com
        - diffie-hellman-group15-sha256@ssh.com
        - diffie-hellman-group15-sha384@ssh.com
        - diffie-hellman-group16-sha384@ssh.com
        - diffie-hellman-group16-sha512
        - diffie-hellman-group16-sha512@ssh.com
        - diffie-hellman-group18-sha512
        - diffie-hellman-group18-sha512@ssh.com
        - diffie-hellman-group1-sha1
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group-exchange-sha224@ssh.com
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group-exchange-sha384@ssh.com
        - diffie-hellman-group-exchange-sha512@ssh.com
        - ecdh-nistp521-kyber1024-sha512@ssh.com
        - ecdh-sha2-nistp256
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp521
        - mlkem1024nistp384-sha384
        - mlkem768nistp256-sha256
        - mlkem768x25519-sha256
        - sntrup761x25519-sha512@openssh.com
    mac:
        - crypticore-mac@ssh.com
        - hmac-md5
        - hmac-md5-96
        - hmac-md5-96-etm@openssh.com
        - hmac-md5-etm@openssh.com
        - hmac-sha1
        - hmac-sha1-96
        - hmac-sha1-96-etm@openssh.com
        - hmac-sha1-etm@openssh.com
        - hmac-sha224@ssh.com
        - hmac-sha2-256
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha256@ssh.com
        - hmac-sha256-2@ssh.com
        - hmac-sha384@ssh.com
        - hmac-sha512@ssh.com
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
* Formerly known as just "SSH" or "ssh.com"
* Strictly speaking, the Tectica SSH client and server are two separate
  products.
* The information here is based on the Tectia SSH manual, in particular the list of
  [default and supported SSH algorithms](https://docs.ssh.com/manuals/server-admin/66/csc-algorithms.html)
  as well as the list of
  [supported user authentication methods](https://docs.ssh.com/manuals/server-admin/66/server-auth-supported-methods.html).
* WARNING: The data here was lasted update for release 6.6.6; changes made
  since then are not reflected by the list above.
