---
layout: wiki_post
title: wikiastronomy
permalink: /wiki/categories/wikiastronomy
---

<div class="card">
{% for post in site.categories.wikiastronomy %}
<li class="category-posts"><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</div>