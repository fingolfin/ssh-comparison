---
layout: default
---

<h1 class="page-heading">What is this all about?</h1>

The aim of this page is to compare various implementations of the SSH v2
protocol in terms which cryptographic protocols each implements.

This page does *not* try to give a full comparison of all capabilities of each
implementation. If you want to find "the best SSH client for platform XYZ",
this is the wrong place to look at. However, it is the right place to look at
if you want to find out which SSH implementations support modern crypto suites
and which don't.

**DISCLAIMER**: While I try to keep this page accurate and up-to-date, I make no
guarantee about the correctness of the data presented here. Use it at your own
risk. If you find any inaccuracies or mistakes, please report them via
[the issue tracker](https://github.com/fingolfin/ssh-comparison/issues).

The data listed here is derived from various sources:

* The actual source code, where available.
* Claims made in the documentation of each implementation, where available.
* For SSH clients, a connection is made to a special SSH test server, which
  reports the protocols the client claims to support (the test server does not
  verify this, however).
* Contributions from third parties, sometimes authors of implementations.
