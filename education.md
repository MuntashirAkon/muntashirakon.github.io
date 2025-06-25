---
layout: default
title: Education
---

{% assign sorted_education = site.education | sort: 'date' | reverse %}
{% for education in sorted_education %}
## **{{ education.institute }}**, {{ education.country }}
- {{ education.degree }} ({{ education.duration }})
{% for item in education.extras %}- {% if item.key %}*{{ item.key }}:* {% endif %}{{ item.value }}
{% endfor %}
{{ education.content }}
{% endfor %}