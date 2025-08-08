---
title: moussh
homepage: http://ftp.rodents-montreal.org/mouse/git-unpacked/moussh/branch-link/master/tree/moussh/
source-repository: git://git.rodents-montreal.org/moussh
license: "[Public Domain](http://ftp.rodents-montreal.org/mouse/git-unpacked/moussh/branch-link/master/tree/moussh/README)"
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 0.9.2fe6d57aff
    version: 0.9.20250724104234w0400.e4f5ecd6ab
    date: 2025-07-24
#changelog: TODO
client: yes
server: yes

protocols:
    cipher:
        - 3des-cbc
        - 3des-ctr
        - arcfour
        - arcfour128-draft-00@putty.projects.tartarus.org
        - arcfour256-draft-00@putty.projects.tartarus.org
        - arcfour-64k@rodents.montreal.qc.ca
        - blowfish-cbc
        - blowfish-ctr
        - camellia-128-cbc@rodents.montreal.qc.ca
        - camellia-192-cbc@rodents.montreal.qc.ca
        - camellia-256-cbc@rodents.montreal.qc.ca
        - camellia-128-ctr@rodents.montreal.qc.ca
        - camellia-192-ctr@rodents.montreal.qc.ca
        - camellia-256-ctr@rodents.montreal.qc.ca
        - chacha@rodents.montreal.qc.ca
        - idea-cbc
        - aes128-cbc
        - aes192-cbc
        - aes256-cbc
        - rijndael-cbc@lysator.liu.se
        - aes128-ctr
        - aes192-ctr
        - aes256-ctr
        - rijndael-k4b4-cbc@rodents.montreal.qc.ca
        - rijndael-k4b4-ctr@rodents.montreal.qc.ca
        - rijndael-k4b6-cbc@rodents.montreal.qc.ca
        - rijndael-k4b6-ctr@rodents.montreal.qc.ca
        - rijndael-k4b8-cbc@rodents.montreal.qc.ca
        - rijndael-k4b8-ctr@rodents.montreal.qc.ca
        - rijndael-k6b4-cbc@rodents.montreal.qc.ca
        - rijndael-k6b4-ctr@rodents.montreal.qc.ca
        - rijndael-k6b6-cbc@rodents.montreal.qc.ca
        - rijndael-k6b6-ctr@rodents.montreal.qc.ca
        - rijndael-k6b8-cbc@rodents.montreal.qc.ca
        - rijndael-k6b8-ctr@rodents.montreal.qc.ca
        - rijndael-k8b4-cbc@rodents.montreal.qc.ca
        - rijndael-k8b4-ctr@rodents.montreal.qc.ca
        - rijndael-k8b6-cbc@rodents.montreal.qc.ca
        - rijndael-k8b6-ctr@rodents.montreal.qc.ca
        - rijndael-k8b8-cbc@rodents.montreal.qc.ca
        - rijndael-k8b8-ctr@rodents.montreal.qc.ca
        - sharc4-512@rodents.montreal.qc.ca
    compression:
        - none
        - zlib
    hostkey:
        - ssh-dss
        - ssh-rsa
        - rsa-sha2-256
        - rsa-sha2-512
    kex:
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group1-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group14-sha256
        - diffie-hellman-group15-sha512
        - diffie-hellman-group16-sha512
        - diffie-hellman-group17-sha512
        - diffie-hellman-group18-sha512
        - rsa2048-sha256-draft-01@putty.projects.tartarus.org
        - rsa2048-sha256-draft-04@putty.projects.tartarus.org
    mac:
        - hmac-sha1
        - hmac-sha1-96
        - hmac-md5
        - hmac-md5-96
    userauth:
        - keyboard-interactive
        - password
        - publickey
---
* SSH implementation by Mouse.
