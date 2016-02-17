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

<div id='cmp-table-{{ type }}-parent' class='cmp-table-parent'>
<table id='cmp-table-{{ type }}' class='impl-comparison table-header-rotated'> <!--  table-header-rotated -->
<thead>
  <tr>
    <th class="fixedcol">id</th>
    <th class="speccol" class='rotate'><div><span>Specification</span></div></th>
    {% for impl in site.impls %}
    <th class='rotate'><div><span><a href='{{ impl.url }}'>{{ impl.title }}</a></span></div></th>
    {% endfor %}
  </tr>
</thead>
<tbody>
{% for item in namelist %}
  <tr>
    <td class="fixedcol">{{ item }}</td>
    <td class="speccol">
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
</div>

{% endfor %}

<script>
$(document).ready(function(){ 
{% for type in page.types %}
    $("#cmp-table-{{ type }}").tableHeadFixer({'left' : 1});
{% endfor %}
})
</script>
