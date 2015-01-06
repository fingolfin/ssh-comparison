## {{ page.title }}

* Homepage: [{{ page.impl.homepage }}]({{ page.impl.homepage }})
* Latest release: {{ page.impl.latest-release.version }} ({{ page.impl.latest-release.date }})
* Client: {{ page.impl.client }}
* Server: {{ page.impl.client }}

## Supported protocols

### Ciphers
  {% for x in page.impl.protocols.cipher %}
  * {{ x }}
  {% endfor %}

### Compression
  {% for x in page.impl.protocols.compression %}
  * {{ x }}
  {% endfor %}

### Hostkey
  {% for x in page.impl.protocols.hostkey %}
  * {{ x }}
  {% endfor %}

### Key exchange
  {% for x in page.impl.protocols.kex %}
  * {{ x }}
  {% endfor %}

### MAC
  {% for x in page.impl.protocols.mac %}
  * {{ x }}
  {% endfor %}

### Userauth
  {% for x in page.impl.protocols.userauth %}
  * {{ x }}
  {% endfor %}
