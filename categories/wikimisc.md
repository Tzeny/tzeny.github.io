---
layout: wiki_post
title: wikimisc
permalink: /wiki/categories/wikimisc
---

<div class="card">
{% for post in site.categories.wikimisc %}
<li class="category-posts"><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</div>