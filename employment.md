---
layout: default
title: Employment
---

{% assign sorted_education = site.employment | sort: 'date' | reverse %}
{% for employment in sorted_education %}
## **{{ employment.company }}**, {{ employment.country }}
<div>
{{ employment.position }} ({% if employment.type %}{{ employment.type }}, {% endif %}{{ employment.duration }})
</div>
{{ employment.content }}
{% endfor %}