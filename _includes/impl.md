## {{ page.title }}

* Homepage: [{{ page.homepage }}]({{ page.homepage }}){% if page.developer %}
* Developer: {{ page.developer }}{% endif %}
* First release: {% if page.first-release %}{{ page.first-release.date }}{% else %} ? {% endif %}
* Latest release: {{ page.latest-release.version }} ({{ page.latest-release.date }})
{% if page.changelog %}* Version history: [{{ page.changelog }}]({{ page.changelog }}) {% endif %}
{% if page.source-repository %}* Source repository: [{{ page.source-repository }}]({{ page.source-repository }}) {% endif %}
{% if page.license %}* License: {{ page.license }}{% endif %}
* Client: {{ page.client }}
* Server: {{ page.server }}

{% if page.remarks %}
### Remarks
{{ page.remarks }}
{% endif %}
### Supported protocols

{% for proto_class in site.data.proto_classes %}
{% assign proto_class_id = proto_class[0] %}
#### {{ proto_class[1] }}
  {{ page.protocols[proto_class_id] | join: ', ' }}
{% endfor %}
