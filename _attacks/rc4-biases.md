---
title: RC4 keystream biases
year: 2013
authors: Nadhem AlFardan, Daniel J. Bernstein, Kenneth G. Paterson, Bertram Poettering, Jacob C. N. Schuldt
paper: https://www.usenix.org/system/files/conference/usenixsecurity13/sec13-paper_alfardan.pdf
venue: USENIX Security 2013
summary: Statistical biases throughout the RC4 keystream reveal plaintext that is encrypted many times under different keys.
condition: Shown for TLS, needing 2^26 sessions or 13×2^30 encryptions (RFC 7465); no SSH-specific demonstration.
mitigation: RFC 8758 says RC4 MUST NOT be used in SSH.
affects:
  cipher:
    - arcfour
    - arcfour128
    - arcfour256
    - arcfour128-draft-00@putty.projects.tartarus.org
    - arcfour256-draft-00@putty.projects.tartarus.org
    - arcfour-64k@rodents.montreal.qc.ca
    - sharc4-512@rodents.montreal.qc.ca
---
Dropping the start of the keystream (`arcfour128`, `arcfour256`,
`arcfour-64k`) or changing the key schedule (`sharc4-512`) removes the
early biases only; the attack also uses biases that persist through the
whole keystream.
