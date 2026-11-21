---
title: WebSSH
homepage: https://webssh.net/
license: Proprietary
#first-release:
#    date: YYYY-MM-DD
latest-release:
    version: 33.4
    date: 2026-11-18
changelog: https://webssh.net/documentation/changelog/33/
client: yes
server: no
platforms:
    - iphone
    - ipad
    - macos

# cipher, hostkey, kex, mac: https://webssh.net/documentation/help/SSH/supported-algorithms/
protocols:
    cipher:
        - chacha20-poly1305@openssh.com         # disabled by default
        - aes128-ctr
        - aes256-ctr
        - aes192-ctr                            # disabled by default
        - aes128-cbc                            # disabled by default
        - aes256-cbc                            # disabled by default
        - aes192-cbc                            # disabled by default
        - aes128-gcm@openssh.com
        - aes256-gcm@openssh.com
        - twofish256-cbc                        # disabled by default
        - twofish128-cbc                        # disabled by default
        - blowfish-cbc                          # disabled by default
        #- 3des-cbc                             # no longer listed
        #- arcfour128                           # no longer listed
        #- arcfour256                           # no longer listed
    compression:
        - zlib
        - zlib@openssh.com
        - none
    hostkey:
        - ecdsa-sha2-nistp256                   # disabled by default
        - ecdsa-sha2-nistp384                   # disabled by default
        - ecdsa-sha2-nistp521                   # disabled by default
        - ssh-ed25519
        - rsa-sha2-256
        - rsa-sha2-512
        - ssh-rsa                               # disabled by default
        - ssh-dss                               # disabled by default
    kex:
        - curve25519-sha256
        - curve25519-sha256@libssh.org
        - ecdh-sha2-nistp256                    # disabled by default
        - ecdh-sha2-nistp384                    # disabled by default
        - ecdh-sha2-nistp521                    # disabled by default
        - diffie-hellman-group14-sha256         # disabled by default
        - diffie-hellman-group16-sha512
        - diffie-hellman-group18-sha512
        - diffie-hellman-group-exchange-sha256
        - diffie-hellman-group1-sha1            # disabled by default
        - diffie-hellman-group14-sha1           # disabled by default
        - diffie-hellman-group-exchange-sha1    # disabled by default
    mac:
        - hmac-sha2-256                         # disabled by default
        - hmac-sha2-512                         # disabled by default
        - hmac-sha2-256-etm@openssh.com
        - hmac-sha2-512-etm@openssh.com
        - hmac-sha1-etm@openssh.com             # disabled by default
        - hmac-sha1                             # disabled by default
        - hmac-ripemd160                        # disabled by default
        - hmac-sha1-96                          # disabled by default
        - hmac-md5                              # disabled by default
    userauth:
        - keyboard-interactive
        - publickey
        - password

first_kex_packet_follows: 0
ident: "SSH-2.0-PuTTY_Release_0.63"
based-on: "[PuTTY](/impls/putty.html)"
---
* Client for Apple iOS (iPhone, iPod, iPad).
* Available on the Apple App Store in two versions:
   [WebSSH Essential](https://itunes.apple.com/us/app/id958955657),
   [WebSSH Pro](https://itunes.apple.com/us/app/id497714887)
* 2015-07-10: Version 8.3.2 identifies itself on the wire as `SSH-2.0-PuTTY_Release_0.63`.
* 2015-12-05: Version 13.1 identifies itself on the wire as `SSH-2.0-PuTTY_Release_0.63`.
