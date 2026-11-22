---
title: dartssh2
homepage: https://github.com/vicajilau/dartssh2
source-repository: https://github.com/vicajilau/dartssh2
license: "[MIT](https://github.com/vicajilau/dartssh2/blob/main/LICENSE)"
first-release:
    date: 2021-10-04
latest-release:
    version: 4.1.0
    date: 2026-09-04
changelog: https://github.com/vicajilau/dartssh2/blob/main/CHANGELOG.md
client: yes
server: no
library: client

# Default order first; "not default" names are implemented but have to be
# requested through SSHAlgorithms. Versions from CHANGELOG.md.
protocols:
    cipher:
        - aes256-gcm@openssh.com        # since 2.17.0
        - aes128-gcm@openssh.com        # since 2.17.0
        - chacha20-poly1305@openssh.com # since 3.2.0
        - aes256-ctr
        - aes128-ctr
        - aes192-ctr                    # not default
        - aes256-cbc                    # not default since 4.0.0
        - aes192-cbc                    # not default
        - aes128-cbc                    # not default since 4.0.0
    compression:
        - none
    hostkey:
        - ssh-ed25519
        - rsa-sha2-512
        - rsa-sha2-256
        - ecdsa-sha2-nistp521
        - ecdsa-sha2-nistp384
        - ecdsa-sha2-nistp256
        - ssh-rsa                       # not default since 4.0.0
    kex:
        - curve25519-sha256             # since 2.22.4
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp521
        - ecdh-sha2-nistp384
        - ecdh-sha2-nistp256
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group14-sha256
        - diffie-hellman-group14-sha1           # not default since 4.0.0
        - diffie-hellman-group-exchange-sha1    # not default since 4.0.0
        - diffie-hellman-group1-sha1            # not default since 3.1.0
        - ext-info-c                    # since 3.1.0
        - kex-strict-c-v00@openssh.com  # since 3.1.0
        - kex-strict-s-v00@openssh.com  # since 3.1.0
    mac:
        - hmac-sha2-256-etm@openssh.com # since 2.13.0
        - hmac-sha2-512-etm@openssh.com # since 2.13.0
        - hmac-sha2-256
        - hmac-sha2-512
        - hmac-sha1
        - hmac-sha2-256-96              # since 2.13.0, not default since 3.1.0
        - hmac-sha2-512-96              # since 2.13.0, not default since 3.1.0
        - hmac-md5                      # not default since 3.1.0
    userauth:
        - password
        - publickey
        - hostbased                     # since 3.2.0
        - keyboard-interactive
    extension:
        - server-sig-algs               # since 3.1.0

first_kex_packet_follows: 0
ident: "SSH-2.0-DartSSH_2.0"
---
* Pure Dart; runs on the Dart VM, in Flutter apps and in browsers.
* Published on [pub.dev](https://pub.dev/packages/dartssh2). The repository
  moved from TerminalStudio/dartssh2 to vicajilau/dartssh2.
* The version string after `SSH-2.0-` is configurable; `DartSSH_2.0` is the
  default.
* The unreleased main branch has ML-KEM-768, but no key exchange uses it yet.
