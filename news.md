---
layout: default
title: News
---

<ul>
{% for item in site.data.news %}
  <li markdown="span"><b>[{{ item.year }}]</b> {{ item.news }}</li>
{% endfor %}
</ul>
