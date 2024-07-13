---
title: TinySSH
homepage: https://tinyssh.org/
source-repository: https://github.com/janmojzis/tinyssh
license: "[CC0](https://tinyssh.org/LICENCE)"
first-release:
    date: 2014-02-16    # according to Wikipedia
    # see also https://news.ycombinator.com/item?id=7727738 from May 11, 2014
    # and http://tuxdiary.com/2014/05/11/tinyssh/
latest-release:
    version: 20240101
    date: 2024-01-01
changelog: https://github.com/janmojzis/tinyssh/releases
client: no
server: yes
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        #- aes256-ctr                               # removed in 20190101
    compression:
        - none
    hostkey:
        - ssh-ed25519
        #- ecdsa-sha2-nistp256                      # removed in 20190101
    kex:
        - curve25519-sha256                         # added in 20180201
        - curve25519-sha256@libssh.org
        #- ecdh-sha2-nistp256                       # removed in 20190101
        #- sntrup4591761x25519-sha512@tinyssh.org   # added in 20190101, removed in 20210319
        - sntrup761x25519-sha512@openssh.com        # added in 20210319
        - kex-strict-c-v00@openssh.com
        - kex-strict-s-v00@openssh.com
    mac:
        #- chacha20-poly1305@openssh.com    # not an actual allowed MAC value, but implied by the choice of cipher
        - hmac-sha2-256
    userauth:
        - publickey
---
* Minimalistic SSH implementation, still in alpha stage.
