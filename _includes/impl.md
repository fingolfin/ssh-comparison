## {{ page.title }}

* Homepage: [{{ page.impl.homepage }}]({{ page.impl.homepage }})
{% if page.impl.developer %}* Developer: {{ page.impl.developer }}{% endif %}
* First release: {% if page.impl.first-release %}{{ page.impl.first-release.date }}{% else %} ? {% endif %}
* Latest release: {{ page.impl.latest-release.version }} ({{ page.impl.latest-release.date }})
{% if page.impl.changelog %}* Version history: [{{ page.impl.changelog }}]({{ page.impl.changelog }}) {% endif %}
{% if page.impl.source-repository %}* Source repository: [{{ page.impl.source-repository }}]({{ page.impl.source-repository }}) {% endif %}
{% if page.impl.license %}* License: {{ page.impl.license }}{% endif %}
* Client: {{ page.impl.client }}
* Server: {{ page.impl.server }}

{% if page.impl.remarks %}
### Remarks
{{ page.impl.remarks }}
{% endif %}
### Supported protocols

{% for proto_class in site.data.proto_classes %}
{% assign proto_class_id = proto_class[0] %}
#### {{ proto_class[1] }}
  {{ page.impl.protocols[proto_class_id] | join: ', ' }}
{% endfor %}
