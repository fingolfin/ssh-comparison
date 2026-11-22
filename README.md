A technical comparison of various SSH implementations (clients, servers and
libraries), in terms of supported SSH crypto protocols.

Pull requests are welcome! In particular for additional implementations
as well as updates or corrections to existing entries.

This site is built with `jekyll`. Run `bundle install` once, then
`bundle exec jekyll serve` for local testing. The `Gemfile` pins the same
Jekyll that `.github/workflows/pages.yml` deploys with, so what builds
locally builds in CI.

Each implementation is a file in `_impls/`. The keys that say what it is
(`client`, `server`, `standalone`, `library`, `platforms`, `languages`) are
documented in `_data/impl_meta.yml`; `ruby validate-data.rb` checks them and
runs in CI.

## Probing an SSH client

`ssh-detect.py` is a fake SSH server that records which algorithms a
client offers. Run `python3 ssh-detect.py` (standard library only),
point the client at this machine on port 2222, and copy the printed
YAML into the client's `_impls/*.md` entry. The client fails to
connect by design: the server hangs up after the client's KEXINIT, so
user authentication methods are not recorded.
