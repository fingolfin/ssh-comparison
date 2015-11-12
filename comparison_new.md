---
layout: default
title: The comparison
types:
    - cipher
    - compression
    - hostkey
    - kex
    - userauth
    - mac
---

{% for type in page.types %}
{% include namelist.html type=type %}
### {{ site.data.proto_classes[type] }}

<table id='cmp-table-cipher' class='impl-comparison tablesorter table-header-rotated'>
<thead><tr><th>id</th>
  <th class='rotate'><div><span>Specification</span></div></th>
{% for impl in site.impls %}  <th class='rotate'><div><span><a href='{{ impl.url }}'>{{ impl.title }}</a></span></div></th>
{% endfor %}
</tr></thead>
<tbody>
{% for item in namelist %}<tr>
  <td>{{ item }}</td>
  <td><a href='TODO'>TODO</a></td>
{% for impl in site.impls %}{% if impl.protocols contains type %}{% if impl.protocols[type] contains item %}<td class='yes'>Yes</td>  {% else %}<td class='no'>No</td>    {% endif %}{% else %}<td class='unknown'>?</td>{% endif %}  <!-- {{ impl.relative_path | split:"/" | last | remove:".md" }} -->
{% endfor %}</tr>
{% endfor %}
</tbody>
</table>


{% endfor %}
