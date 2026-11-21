---
title: Precomputation against 1024-bit Diffie-Hellman groups
year: 2015
authors: David Adrian, Karthikeyan Bhargavan, Zakir Durumeric, Pierrick Gaudry, Matthew Green, J. Alex Halderman, Nadia Heninger, Drew Springall, Emmanuel Thomé, Luke Valenta, Benjamin VanderSloot, Eric Wustrow, Santiago Zanella-Béguelin, Paul Zimmermann
paper: https://weakdh.org/imperfect-forward-secrecy-ccs15.pdf
venue: ACM CCS 2015 ("Imperfect Forward Secrecy", the Logjam paper)
summary: One number-field-sieve precomputation for a fixed 1024-bit group makes each later discrete log in that group cheap, so every connection using the group can be decrypted passively.
condition: The precomputation is estimated to be within nation-state budgets; in 2015 it would have exposed 25.7% of public SSH servers through Oakley Group 2.
mitigation: Use a MODP group of at least 2048 bits (RFC 8270) or elliptic-curve key exchange.
affects:
  kex:
    - diffie-hellman-group1-sha1
    - gss-group1-sha1-*
---
The paper's TLS downgrade does not apply to SSH; the precomputation does.
Group exchange (`diffie-hellman-group-exchange-*`) is also exposed when the
server offers a 1024-bit group, which RFC 8270 forbids.
