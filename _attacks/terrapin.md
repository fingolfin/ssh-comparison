---
title: Terrapin
year: 2023
authors: Fabian Bäumer, Marcus Brinkmann, Jörg Schwenk
paper: https://terrapin-attack.com/TerrapinAttack.pdf
venue: USENIX Security 2024
cve: CVE-2023-48795
summary: A man in the middle adjusts sequence numbers during the handshake and then deletes the first encrypted packets undetected, typically the EXT_INFO message that negotiates extensions.
condition: Exploitable with ChaCha20-Poly1305, and with an EtM MAC paired with a CBC cipher; EtM with CTR is exploitable only with low probability, and GCM is immune.
mitigation: Strict key exchange (kex-strict-c/-s), which both ends must offer.
affects:
  cipher:
    - chacha20-poly1305
    - chacha20-poly1305@openssh.com
    - chacha20-poly1305-mt@hpnssh.org
    # only together with an EtM MAC
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
  mac:
    - hmac-md5-etm@openssh.com
    - hmac-md5-96-etm@openssh.com
    - hmac-sha1-etm@openssh.com
    - hmac-sha1-96-etm@openssh.com
    - hmac-sha2-256-etm@openssh.com
    - hmac-sha2-512-etm@openssh.com
    - umac-64-etm@openssh.com
    - umac-128-etm@openssh.com
---
Deleting EXT_INFO can, for example, downgrade the public key signature
algorithm used for user authentication or disable OpenSSH's keystroke
timing obfuscation. Implementation flaws in AsyncSSH turned the same
primitive into session hijacking (CVE-2023-46445, CVE-2023-46446).
