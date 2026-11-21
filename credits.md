---
layout: default
title: Credits
---

<h1 class="page-heading">Credits</h1>

<p>
This site is the work of a good number of people. A comparison table is only
worth as much as the effort spent keeping it accurate, and that effort is
mostly invisible: reading release notes, diffing source trees, and correcting
entries that have quietly gone stale.
</p>

<h2>Maintainers</h2>

<dl class="credits-list">
{% for person in site.data.credits.maintainers %}
  <dt>{% if person.github %}<a href="https://github.com/{{ person.github }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</dt>
  <dd>{{ person.role }}</dd>
{% endfor %}
</dl>

<h2>Contributors</h2>

<p>
Thanks to everyone who has sent a pull request, reported an error, or supplied
data about an implementation — in several cases the authors of the
implementation in question, which is the best source there is:
</p>

<ul class="credits-contributors">
{% for person in site.data.credits.contributors %}
  <li>{% if person.github %}<a href="https://github.com/{{ person.github }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</li>
{% endfor %}
</ul>

<p>
The <a
href="https://github.com/fingolfin/ssh-comparison/graphs/contributors">contributors
graph on GitHub</a> is the authoritative, always-current version of this list.
If you have contributed and are missing here, that is an oversight — please <a
href="https://github.com/fingolfin/ssh-comparison/issues">say so</a>.
</p>

<h2>Built with</h2>

<ul>
<li><a href="https://jekyllrb.com/">Jekyll</a>, hosted on <a href="https://pages.github.com/">GitHub Pages</a></li>
<li>The rotated table headers follow <a href="https://css-tricks.com/rotated-table-column-headers/">a CSS-Tricks recipe</a>; the table colours came out of <a href="https://paletton.com/">Paletton</a></li>
</ul>
