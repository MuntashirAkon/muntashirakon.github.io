---
layout: default
title: Gallery
---

{% assign sorted_gallery = site.gallery | sort: 'priority' %}
{% for gallery in sorted_gallery %}
## {{ gallery.title }}
{{ gallery.content }}
<div class="flex-gallery" style="margin-top: 1rem;">
  {% for image in gallery.gallery %}
  <figure style="display: block; text-align: center;">
    <img src="{{ image.src | relative_url }}" {% if image.alt %}alt="{{ image.alt }}"{% endif %} style="max-width: 24rem; margin-right: 0;" />
    {% if image.cap %}<figcaption>{{ image.cap }} {% if image.cpy %}<small>[{{ image.cpy }}]</small>{% endif %}</figcaption>{% endif %}
  </figure>
  {% endfor %}
</div>
{% endfor %}
