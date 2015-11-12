---
layout: impl

title: TinySSH
homepage: http://tinyssh.org/
source-repository: https://github.com/janmojzis/tinyssh
license: "[Public domain](http://tinyssh.org/LICENCE)"
first-release:
    date: 2014-02-16
latest-release:
    #version: X.Y
    date: 2015-05-01
#changelog: TODO
client: no
server: yes
remarks: |
    * Minimalistic SSH implementation, still in alpha stage.

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
