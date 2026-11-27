---
title: Chosen-plaintext attack on SSH's CBC modes
year: 2002
authors: Mihir Bellare, Tadayoshi Kohno, Chanathip Namprempre
paper: https://homes.cs.washington.edu/~yoshi/papers/SSH/ssh.pdf
venue: ACM CCS 2002; ACM TISSEC 7(2), 2004
summary: The next packet's IV is the previous packet's last ciphertext block, so an attacker who can choose plaintext can test guesses of earlier blocks.
condition: The attacker must control most of a packet's first block; metadata limits this, so a test needs a collision on about 25 bits.
mitigation: Use a counter mode (RFC 4344, written as the fix) or an AEAD mode.
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
RFC 4253's CBC modes chain the IV across packets. Since the attacker sees the
last ciphertext block before the next packet is encrypted, a chosen first
block lets them check whether a guessed plaintext block was ever encrypted.
RFC 4344 cites this paper when it calls the CBC methods "vulnerable to
chosen-plaintext privacy attacks".
