---
layout: default
title: Teaching
---

{% assign sorted_teaching = site.teaching | sort: 'date' | reverse %}
{% for teaching in sorted_teaching %}
## **{{ teaching.institute }}**, {{ teaching.country }}
<div>
{{ teaching.position }} ({{ teaching.duration }})
</div>
<ul>
{% for course in teaching.courses %}
  <li markdown="span">{{ course.code }}: {{ course.title }} ({{ course.sessions }})</li>
{% endfor %}
</ul>
{{ teaching.content }}
{% endfor %}