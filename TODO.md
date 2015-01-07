* track for each implementation which version added (or removed) each protocol
* record default order client tries protocols
* record which protocols are disabled / enabled by default
* for impls which are both client and server, some protocols may
  only be supported by one but not the other. support that
* link to specs, or perhaps just
   http://www.openssh.com/specs.html
* note whether its a library, stand-alone client/server, or both
* record more features? e.g. SCP/SFTP support, ...
* mention SSH v1 support (I guess not supporting it could be counted as a 
  feature these days... or at least it is important that one can disable it)
* Add a subpage for each implementation which lists all details for that
  particular information on one quick glance. This makes it easier to
  verify whether the information for that implementation is accurate.
* Allow alternative sorting of the tables?
* Allow restricting comparisons to a subset of implementations and protocols
* In the comparison tables, display how many impls per proto / protos per implicit=false
  there are.

For the table with the protocol specifications:
* record for each protocol where it is described (RFC, etc.),
* also: whether it is required / recommended / optional / not listed in the RFC
* whether is deemed unsafe (with link(s) to substantiate that)


Add more implementations! Some lists:
* https://en.wikipedia.org/wiki/Comparison_of_SSH_clients
* https://en.wikipedia.org/wiki/Comparison_of_SSH_servers


* Record additional information on various protocols somewhere. E.g.:

  aes128-gcm@openssh.com, aes256-gcm@openssh.com:
  see http://www.openssh.com/txt/release-6.2:
  "[...] uses an identical packet format to the
   AES-GCM mode specified in RFC 5647, but uses simpler and different
   selection rules during key exchange."

* Indeed, perhaps add more pages on various specs and protocols with
  additional information on each?

* Record for OpenSSH on which common platforms it is shipped
  in which version(s) by default (say: recent versions of Ubuntu,
  Mac OS X, Fedora, etc.)

* Distinguish clients and servers in comparison; perhaps offer
  separate comparison pages for clients, servers, and combined...?