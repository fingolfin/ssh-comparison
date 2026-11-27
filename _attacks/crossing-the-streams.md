---
title: Crossing the Streams
year: 2026
authors: Fabian Bäumer, Marcus Brinkmann
paper: https://arxiv.org/pdf/2609.07709
venue: ACM CCS 2026
summary: All channels of a connection share one compression context, so an attacker who injects chosen text into one channel learns, from ciphertext lengths, about secrets in another.
condition: Needs compression to be negotiated and a way to inject text into one channel; in the least noisy setting, an 8-letter secret fell in at most 276 guesses.
mitigation: Do not negotiate compression; delayed compression (zlib@openssh.com) does not help.
affects:
  compression:
    - zlib
    - zlib@openssh.com
---
A compression side channel in the style of CRIME and BREACH, across SSH
channels rather than HTTP requests. Compression algorithms are not rated on
this site; this page records the attack only.
