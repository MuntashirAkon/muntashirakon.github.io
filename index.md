---
layout: base
title: About
---

<header>
  {% if site.avatar %}
  <div class="logo-container">
    <img class="logo middle" src="{{ site.avatar | absolute_url }}" />
  </div>
  {% endif %}

  <div class="author-container" style="flex: 1;">
    <h1>{{ site.title }}</h1>
    <p class="no-margin-top no-margin-bottom" markdown="span">
{% if site.alt_names %}(*a.k.a.* {{ site.alt_names }})<br>{% endif %}
{% if site.headline %}{{ site.headline }}<br>{% endif %}
{% if site.department %}{{ site.department }}<br>{% endif %}
{% if site.address %}{{ site.address }}<br>{% endif %}
Email: {% if site.work_email %}[{{ site.work_email }}](mailto:{{ site.work_email }}){% if site.work_email != site.email %}, {% endif %}{% endif %}[{{ site.email }}](mailto:{{ site.email }})
  </p>
    <ul class="icon-list no-margin-top">
      {% if site.linkedin_username %}<li><a href="https://www.linkedin.com/in/{{ site.linkedin_username }}" title="LinkedIn" target="_blank" rel="noreferrer">{% include icons/linkedin.svg %}</a></li>{% endif %}
      {% if site.github_username %}<li><a href="https://github.com/{{ site.github_username }}" title="GitHub" target="_blank" rel="noreferrer">{% include icons/github.svg %}</a></li>{% endif %}
      {% if site.twitter_username %}<li><a href="https://twitter.com/{{ site.twitter_username }}" title="Twitter" target="_blank" rel="noreferrer">{% include icons/twitter.svg %}</a></li>{% endif %}
      {% if site.mastodon_url %}<li><a href="{{ site.mastodon_url }}" title="Mastodon" target="_blank" rel="noreferrer">{% include icons/mastodon.svg %}</a></li>{% endif %}
      {% if site.stackoverflow_id %}<li><a href="https://stackoverflow.com/users/{{ site.stackoverflow_id }}" title="Stack Overflow" target="_blank" rel="noreferrer">{% include icons/stack-overflow.svg %}</a></li>{% endif %}
      {% if site.cv %}<li><a href="{{ site.cv }}" title="CV" target="_blank" rel="noreferrer">{% include icons/cv.svg %}</a></li>{% endif %}
    </ul>
  </div>
</header>

---

{% if site.conf.homepage.news %}
## Recent News
<ul>
{% for item in site.data.news %}
<li markdown="span"><b>[{{ item.year }}]</b> {{ item.news }}</li>
  {% if forloop.index0 == 2 %}
</ul>

<details markdown="block">
  <summary>More…</summary>

<ul>
  {% endif %}
{% endfor %}
</ul>

</details>
---
{% endif %}

{% if site.conf.homepage.intro %}{% include intro.md %}{% endif %}

{% if site.conf.homepage.publications %}
## Publications
{% include publications.html subheading="h3" %}
{% endif %}

{% if site.conf.homepage.projects %}
## Selected Projects
{% assign sorted_projects = site.projects | sort: 'priority' %}
<ul>
{% for project in sorted_projects %}
{% if project.selected %}
  <li><a href="{{ project.link }}"><strong>{{ project.name }}</strong></a><br>{{ project.description }}</li>
{% endif %}
{% endfor %}
</ul>
{% endif %}

{% if site.conf.homepage.teaching %}
## Teaching
{% assign sorted_teaching = site.teaching | sort: 'date' | reverse %}
{% for teaching in sorted_teaching %}
### **{{ teaching.institute }}**, {{ teaching.country }}
<div>
{{ teaching.position }} ({{ teaching.duration }})<br>
<em>Courses:</em> {% for course in teaching.courses %}
  {{ course.title }}{% unless forloop.last %}, {% endunless %}
{% endfor %}
</div>
{{ teaching.content }}
{% endfor %}
{% endif %}

{% if site.conf.homepage.awards %}
## Honors and Awards
{% assign awards = site.data.awards %}
<ul>
{% for item in awards %}
<li markdown="span"><b>[{{ item.year }}]</b> {{ item.award }}</li>
{% endfor %}
</ul>
{% endif %}