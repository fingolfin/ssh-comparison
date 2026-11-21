---
title: SHA-1 chosen-prefix collisions
year: 2020
authors: Gaëtan Leurent, Thomas Peyrin
paper: https://www.usenix.org/system/files/sec20-leurent.pdf
venue: USENIX Security 2020 ("SHA-1 is a Shambles")
summary: Two documents with arbitrary, different prefixes can be made to share a SHA-1 hash for about 2^63.4 SHA-1 computations, so a signature on one is valid for the other.
condition: Practical against signatures on data the attacker helps shape, such as certificates; forging a key-exchange signature would need the collision during the handshake, which took two months of GPU time.
mitigation: Use a SHA-2 signature algorithm (RFC 8332 for RSA). HMAC-SHA-1 is not affected.
affects:
  hostkey:
    - ssh-rsa
    - ssh-rsa-cert
    - ssh-rsa-cert-v01@openssh.com
    - ssh-dss
    - ssh-dss-cert
    - ssh-dss-cert-v01@openssh.com
    - x509v3-ssh-rsa
    - x509v3-ssh-dss
    - x509v3-sign-rsa-sha1
    - x509v3-sign-dss-sha1
---
OpenSSH 8.2 announced the deprecation of `ssh-rsa` citing this result. The
paper's own conclusion for SSH: SHA-1 for "authentication of handshake
messages in TLS or SSH is dangerous".
