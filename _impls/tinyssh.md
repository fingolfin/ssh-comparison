---
title: TinySSH
homepage: http://tinyssh.org/
source-repository: https://github.com/janmojzis/tinyssh
license: "[Public domain](http://tinyssh.org/LICENCE)"
first-release:
    date: 2014-02-16    # according to Wikipedia
    # see also https://news.ycombinator.com/item?id=7727738 from May 11, 2014
    # and http://tuxdiary.com/2014/05/11/tinyssh/
latest-release:
    #version: X.Y
    date: 2016-03-18
#changelog: TODO
client: no
server: yes
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes128-ctr
        - aes256-ctr
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - ecdsa-sha2-nistp256
    kex:
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256
    mac:
        #- chacha20-poly1305@openssh.com    # not an actual allowed MAC value, but implied by the choice of cipher
        - hmac-sha2-256
    userauth:
        - publickey
---
* Minimalistic SSH implementation, still in alpha stage.
