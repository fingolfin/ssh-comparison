---
title: Sweet32
year: 2016
authors: Karthikeyan Bhargavan, Gaëtan Leurent
paper: https://www.sweet32.info/SWEET32_CCS16.pdf
venue: ACM CCS 2016
summary: A 64-bit block cipher repeats a block-cipher input after about 2^32 blocks (32 GB) under one key, and each collision leaks the XOR of two plaintext blocks.
condition: Demonstrated against HTTPS and OpenVPN with about 785 GB of captured traffic, not against SSH; SSH is exposed when it does not rekey well before the bound.
mitigation: Use a 128-bit block cipher; otherwise rekey at least every GB (RFC 4344 §3.2).
affects:
  cipher:
    - 3des-cbc
    - 3des-ctr
    - blowfish-cbc
    - blowfish-ctr
    - idea-cbc
    - idea-ctr
    - cast128-cbc
    - cast128-ctr
---
The birthday bound applies to CBC and CTR alike. The paper notes that SSH
standards recommend rekeying every GB or every 2^(n/4) blocks, "but many
popular SSH clients do not implement this feature".
