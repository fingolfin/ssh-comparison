A technical comparison of various SSH implementations (clients, servers and
libraries), in terms of supported SSH crypto protocols.

Pull requests are welcome! In particular for additional implementations
as well as updates or corrections to existing entries. See
[Contributing](#contributing) for how to record a client.

This site is built with `jekyll`. Run `bundle install` once, then
`bundle exec jekyll serve` for local testing. The `Gemfile` pins the same
Jekyll that `.github/workflows/pages.yml` deploys with, so what builds
locally builds in CI.

Each implementation is a file in `_impls/`. The keys that say what it is
(`client`, `server`, `standalone`, `library`, `platforms`, `languages`) are
documented in `_data/impl_meta.yml`; `ruby validate-data.rb` checks them and
runs in CI.

## Contributing

You can help us by contributing new entries, or by updating or
correcting existing ones. One way to do that is to record what a client
offers, as described below, and send us the result. Pages marked "Help
wanted" need such a recording of a current version.

### Recording a client

`ssh-detect.py` is a fake SSH server. It needs Python 3.7 or later and
nothing else. Download
[the script](https://raw.githubusercontent.com/fingolfin/ssh-comparison/gh-pages/ssh-detect.py)
and run it:

    python3 ssh-detect.py --out records

| Option           | Default   | Effect                                                    |
|------------------|-----------|-----------------------------------------------------------|
| `--port PORT`    | 2222      | port to listen on                                         |
| `--bind ADDRESS` | `0.0.0.0` | address to listen on; the default is all IPv4 addresses   |
| `--out DIR`      | none      | also write each record to a `.yml` file in `DIR`          |
| `--once`         | off       | exit after the first record                               |

It prints the address to use, for example `listening on 0.0.0.0:2222;
point clients at 192.168.1.20 port 2222`. In the client, add a host
with that address and port and any user name, and connect. The
connection fails: the server hangs up after the client's first key
exchange message, before host key check or login. The record goes to
standard output, log lines to standard error.

To reach the computer:

- A phone or tablet must be on the same network. Guest and corporate
  Wi-Fi often block connections between devices.
- macOS: if the firewall asks whether Python may accept incoming
  connections, allow it. Windows: allow access on private networks
  when Windows Defender Firewall asks. Linux: open port 2222/tcp if a
  firewall runs.
- Android emulator: run with `--bind 127.0.0.1` and connect to
  `10.0.2.2`, which the emulator maps to the host's 127.0.0.1.
- iOS Simulator: it shares the Mac's network; connect to `127.0.0.1`.

Record the client with its default settings. If it lets you enable
more algorithms, a second record with all of them enabled shows what is
disabled by default (`disabled-by-default:` in the entry).

### What a record contains

```yaml
# ssh-detect 2026-11-23 20:24:50 from 192.168.1.23:58515
protocols:
    cipher:
        - chacha20-poly1305@openssh.com
        - aes128-ctr
    # ... compression, hostkey, kex, mac
first_kex_packet_follows: 0
ident: "SSH-2.0-OpenSSH_10.5"
# * 2026-11-23: Version ? identifies itself on the wire as `SSH-2.0-OpenSSH_10.5`
```

- The first line: time, and the client's IP address and port. Delete
  it if you prefer.
- `protocols`: the algorithms the client offers, in its order. For
  lists that have two directions it shows client to server, with a
  comment if the other direction differs.
- `ident`: the identification string, which usually names the SSH
  library and its version.
- The last line: a draft remark for the entry; replace `?` by the
  client's version.

The client sends nothing else before the server hangs up: no user name,
password or key. User authentication methods are not recorded.

### Submitting

- A pull request that adds or updates `_impls/<name>.md`: replace
  `protocols`, `first_kex_packet_follows` and `ident` with the record,
  update `latest-release`, and add the remark to the text below the
  front matter. For a new client, copy a similar entry.
  `ruby validate-data.rb` checks the front matter.
- Or an
  [issue with the record](https://github.com/fingolfin/ssh-comparison/issues/new?template=recording.yml),
  if you prefer not to edit the files.
