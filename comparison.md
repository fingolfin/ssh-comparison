---
layout: default
title: The comparison
types:
    - cipher
    - compression
    - hostkey
    - kex
    - mac
    - userauth
---

{% for type in page.types %}
{% include namelist.html type=type %}
### {{ site.data.proto_classes[type] }}

<table id='cmp-table-cipher' class='impl-comparison tablesorter table-header-rotated'>
<thead>
  <tr>
    <th>id</th>
    <th class='rotate'><div><span>Specification</span></div></th>
    {% for impl in site.impls %}
    <th class='rotate'><div><span><a href='{{ impl.url }}'>{{ impl.title }}</a></span></div></th>
    {% endfor %}
  </tr>
</thead>
<tbody>
{% for item in namelist %}
  <tr>
    <td>{{ item }}</td>
    <td>
    {% for spec in site.data.specs %}
      {% if spec[1].protocols[type] contains item %}
        <a href='{{ spec[1].url }}'>{{ spec[1].name }}</a>
      {% endif %}
    {% endfor %}
    </td>
    {% for impl in site.impls %}
      {% if impl.protocols contains type %}
        {% if impl.protocols[type] contains item %}
          <td class='yes'>Yes</td>
        {% else %}
          <td class='no'>No</td>
        {% endif %}
      {% else %}
        <td class='unknown'>?</td>
      {% endif %}
    {% endfor %}
  </tr>
{% endfor %}
</tbody>
</table>

{% endfor %}
