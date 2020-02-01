---
layout: archive
permalink: /distributed-systems/
title: "Distributed Systems Posts"
author_profile: true
header:
  image: "/images/distributed.png"
---

<ul>
  {% for post in site.categories.basic %}
    {% if post.url %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
