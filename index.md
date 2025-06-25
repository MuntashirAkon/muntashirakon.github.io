---
layout: base
title: About
---

<!-- BEGIN Header -->
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
      {% if site.google_scholar_user_id %}<li><a href="https://scholar.google.com/citations?user={{ site.google_scholar_user_id }}" title="Google Scholar" target="_blank" rel="noreferrer">{% include icons/scholar.svg %}</a></li>{% endif %}
      {% if site.orcid_id %}<li><a href="https://orcid.org/{{ site.orcid_id }}" title="ORCiD" target="_blank" rel="noreferrer">{% include icons/orcid.svg %}</a></li>{% endif %}
      {% if site.research_gate_profile_id %}<li><a href="https://www.researchgate.net/profile/{{ site.research_gate_profile_id }}" title="Research Gate" target="_blank" rel="noreferrer">{% include icons/rg.svg %}</a></li>{% endif %}
      {% if site.linkedin_username %}<li><a href="https://www.linkedin.com/in/{{ site.linkedin_username }}" title="LinkedIn" target="_blank" rel="noreferrer">{% include icons/linkedin.svg %}</a></li>{% endif %}
      {% if site.github_username %}<li><a href="https://github.com/{{ site.github_username }}" title="GitHub" target="_blank" rel="noreferrer">{% include icons/github.svg %}</a></li>{% endif %}
      {% if site.twitter_username %}<li><a href="https://x.com/{{ site.twitter_username }}" title="X (Twitter)" target="_blank" rel="noreferrer">{% include icons/x.svg %}</a></li>{% endif %}
      {% if site.mastodon_url %}<li><a href="{{ site.mastodon_url | relative_url }}" title="Mastodon" target="_blank" rel="noreferrer">{% include icons/mastodon.svg %}</a></li>{% endif %}
      {% if site.stackoverflow_id %}<li><a href="https://stackoverflow.com/users/{{ site.stackoverflow_id }}" title="Stack Overflow" target="_blank" rel="noreferrer">{% include icons/stack-overflow.svg %}</a></li>{% endif %}
      {% if site.facebook_username %}<li><a href="https://fb.com/{{ site.facebook_username }}" title="Facebook" target="_blank" rel="noreferrer">{% include icons/facebook.svg %}</a></li>{% endif %}
      {% if site.cv %}<li><a href="{{ site.cv | relative_url }}" title="CV" target="_blank" rel="noreferrer">{% include icons/cv.svg %}</a></li>{% endif %}
    </ul>
  </div>
</header>

---
<!-- END Header -->


<!-- BEGIN Recent News -->
{% if site.conf.homepage.news and site.data.news.size > 0 %}
{% assign show_more_as_page = site.conf.pages.news %}
## Recent News
<ul>
{% for item in site.data.news %}
  {% if forloop.index0 == 3 %}
  {% assign has_details = true %}
  {% if show_more_as_page != true %}
</ul>

<details markdown="block">
  <summary>More…</summary>

<ul>
  {% endif %}
  {% endif %}
  {% if has_details != true or show_more_as_page != true %}
  <li markdown="span"><b>[{{ item.year }}]</b> {{ item.news }}</li>
  {% endif %}
{% endfor %}
</ul>

{% if has_details %}
{% if show_more_as_page %}
<div class="right" ><a href="{{ "/news" | relative_url }}">More…</a></div>
{% else %}
</details>
{% endif %}
{% endif %}
---
{% endif %}
<!-- END Recent News -->


<!-- BEGIN Intro -->
{% if site.conf.homepage.intro %}{% include intro.md %}{% endif %}
<!-- END Intro -->


<!-- BEGIN Publications -->
{% if site.conf.homepage.publications %}
## Publications
{% include publications.html subheading="h3" %}
{% endif %}
<!-- END Publications -->


<!-- BEGIN Projects -->
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
<!-- END Projects -->


<!-- BEGIN Teaching -->
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
<!-- END Teaching -->


<!-- BEGIN Honors and Awards -->
{% if site.conf.homepage.awards %}
## Honors and Awards
{% assign awards = site.data.awards %}
<ul>
{% for item in awards %}
<li markdown="span"><b>[{{ item.year }}]</b> {{ item.award }}</li>
{% endfor %}
</ul>
{% endif %}
<!-- END Honors and Awards -->
