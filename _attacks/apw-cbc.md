---
title: Plaintext recovery against SSH's CBC modes
year: 2009
authors: Martin R. Albrecht, Kenneth G. Paterson, Gaven J. Watson
paper: https://doi.org/10.1109/SP.2009.5
venue: IEEE Symposium on Security and Privacy 2009
cve: CVE-2008-5161
summary: The encrypted packet length field lets an attacker recover 14 bits of plaintext from any CBC-encrypted block, with success probability 2^-14 per attempt.
condition: Each failed attempt ends the connection; OpenSSH estimated about 11,000 connection-killing attempts per success, feasible only against a client that reconnects automatically.
mitigation: Use a counter mode or an AEAD mode.
affects:
  cipher:
    - 3des-cbc
    - blowfish-cbc
    - idea-cbc
    - cast128-cbc
    - aes128-cbc
    - aes192-cbc
    - aes256-cbc
    - serpent128-cbc
    - serpent192-cbc
    - serpent256-cbc
    - twofish128-cbc
    - twofish192-cbc
    - twofish256-cbc
    - twofish-cbc
    - camellia128-cbc
    - camellia192-cbc
    - camellia256-cbc
    - rijndael-cbc@lysator.liu.se
---
The receiver decrypts the first block to learn the packet length, then waits
for that many bytes before checking the MAC. Feeding it a target ciphertext
block as the start of a new packet, and observing when it fails, leaks bits
of the plaintext. Figures above are from OpenSSH's
[advisory](https://www.openssh.com/txt/cbc.adv); the paper itself is not
openly available.
