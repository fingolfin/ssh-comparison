---
title: OpenSSH
homepage: http://www.openssh.com/
source-repository: https://anongit.mindrot.org/openssh.git
# http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/
license: "[BSD](http://cvsweb.openbsd.org/cgi-bin/cvsweb/~checkout~/src/usr.bin/ssh/LICENCE)"
first-release:
    date: 1999-12-01    # according to Wikipedia
latest-release:
    version: 9.9
    date: 2024-09-19
changelog: http://lists.mindrot.org/pipermail/openssh-unix-announce/
# perhaps http://www.openssh.com/txt/ is better changelog link?
client: yes
server: yes

# TODO: strictly speaking, we want:
#  ssh client, ssh server, sftp client, sftp server,
#   and for each whether there is a UI, or a library, or both.
# so any tuple from {ssh, sftp} x {client, server} x {ui, library}
# could specify this as a list of triples, e.g.  ssh-client-ui, sftp-server-library
# perhaps allowing use of asterisk:  *-*-* = all supported; or ssh-*-* for all ssh variants supported, etc.

protocols:
    cipher:
        - chacha20-poly1305@openssh.com # since 6.5
        - aes128-ctr                    # since 3.7
        - aes192-ctr                    # since 3.7
        - aes256-ctr                    # since 3.7
        - aes128-gcm@openssh.com        # since 6.2
        - aes256-gcm@openssh.com        # since 6.2
        - arcfour256                    # disabled by default since 7.2
        - arcfour128                    # disabled by default since 7.2
        - aes128-cbc
        - 3des-cbc                      # disabled by default since 7.4
        - blowfish-cbc                  # disabled by default since 7.2
        - cast128-cbc                   # disabled by default since 7.2
        - aes192-cbc
        - aes256-cbc
        - arcfour                       # disabled by default since 7.2
        - rijndael-cbc@lysator.liu.se   # disabled by default since 7.2
    compression:
        - none
        - zlib@openssh.com
        #- zlib            # removed in 9.9
    hostkey:
        - rsa-sha2-256                      # since 7.1; see https://tools.ietf.org/html/draft-rsa-dsa-sha2-256-03
        - rsa-sha2-512                      # since 7.1; see https://tools.ietf.org/html/draft-rsa-dsa-sha2-256-03
        - ecdsa-sha2-nistp256-cert-v01@openssh.com
        - ecdsa-sha2-nistp384-cert-v01@openssh.com
        - ecdsa-sha2-nistp521-cert-v01@openssh.com
        - ssh-ed25519-cert-v01@openssh.com  # since 6.5
        - ssh-rsa-cert-v01@openssh.com
        - ssh-dss-cert-v01@openssh.com      # disabled by default since 7.0
        - rsa-sha2-256-cert-v01@openssh.com
        - rsa-sha2-512-cert-v01@openssh.com
        #- ssh-rsa-cert-v00@openssh.com      # removed in 7.0
        #- ssh-dss-cert-v00@openssh.com      # removed in 7.0
        - ecdsa-sha2-nistp256               # since 5.7
        - ecdsa-sha2-nistp384               # since 5.7
        - ecdsa-sha2-nistp521               # since 5.7
        - ssh-ed25519                       # since 6.5
        - ssh-rsa
        - ssh-dss                           # disabled by default since 7.0
        - sk-ecdsa-sha2-nistp256-cert-v01@openssh.com
        - sk-ecdsa-sha2-nistp256@openssh.com
        - sk-ssh-ed25519-cert-v01@openssh.com
        - sk-ssh-ed25519@openssh.com
    kex:
        - curve25519-sha256                 # since 7.4
        - curve25519-sha256@libssh.org      # since 6.5
        - ecdh-sha2-nistp256                # since 5.7
        - ecdh-sha2-nistp384                # since 5.7
        - ecdh-sha2-nistp521                # since 5.7
        - diffie-hellman-group-exchange-sha256  # since 4.3
        - diffie-hellman-group-exchange-sha1
        - diffie-hellman-group14-sha1
        - diffie-hellman-group1-sha1        # disabled by default since 7.0; susceptible to logjam
        - diffie-hellman-group14-sha256     # since 7.3
        - diffie-hellman-group16-sha512     # since 7.3
        - diffie-hellman-group18-sha512     # since 7.3
        - ext-info-c                        # since 7.2
        - ext-info-s                        # since 7.2
        - kex-strict-c-v00@openssh.com      # since 9.6
        - kex-strict-s-v00@openssh.com      # since 9.6
        - sntrup761x25519-sha512@openssh.com # since 8.5
        - sntrup761x25519-sha512            # since 9.9
        - mlkem768x25519-sha256             # since 9.9
    mac:
        - umac-64-etm@openssh.com           # since 6.2
        - umac-128-etm@openssh.com          # since 6.2
        - hmac-sha2-256-etm@openssh.com     # since 6.2
        - hmac-sha2-512-etm@openssh.com     # since 6.2
        - hmac-sha1-etm@openssh.com         # since 6.2
        - umac-64@openssh.com               # since 4.7
        - umac-128@openssh.com              # since 6.2
        - hmac-sha2-256                     # since 5.9
        - hmac-sha2-512                     # since 5.9
        - hmac-sha1
        - hmac-md5-etm@openssh.com          # since 6.2; disabled by default since 7.2
        - hmac-ripemd160-etm@openssh.com    # since 6.2
        - hmac-sha1-96-etm@openssh.com      # since 6.2; disabled by default since 7.2
        - hmac-md5-96-etm@openssh.com       # since 6.2; disabled by default since 7.2
        - hmac-md5                          # disabled by default since 7.2
        - hmac-ripemd160
        - hmac-ripemd160@openssh.com
        - hmac-sha1-96                      # disabled by default since 7.2
        - hmac-md5-96                       # disabled by default since 7.2
    userauth:
        - publickey
        - password
        - keyboard-interactive
        - gssapi-with-mic
        - hostbased
        - publickey-hostbound-v00@openssh.com
    extension:
        - ext-info-in-auth@openssh.com      # since 9.6
        - ping@openssh.com                  # since 9.5
        - publickey-hostbound@openssh.com   # since 8.9
        - server-sig-algs                   # since 7.2

first_kex_packet_follows: 0
---
* Probably the most widely deployed SSH implementation.
* There are actually two versions: Regular OpenSSH is part of OpenBSD.
  This version is hosted in the [OpenBSD CVS repository](http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/).
  For everybody else, there is "Portable OpenSSH". This document is
  refering to the portable version, since that is what the majority
  of OpenSSH users is using (as they are not running OpenBSD).
