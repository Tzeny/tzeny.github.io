categories = ['miscellaneous', 'hardware', 'software', 'engineering', 'sports', 'travelling', '3ddesign', 'artificialintelligence']

output_folder = '/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/categories/'

for category in categories:
    page = ("""---
layout: page""",
        f'title: {category.capitalize()}',
        f'permalink: /blog/categories/{category}',
        """---

<h5> Posts by Category : {{ page.title }} </h5>

<div class="card">""",
f'{{% for post in site.categories.{category} %}}',
"""<li class="category-posts"><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</div>"""
    )

    string = '\n'.join(page)

    with open(output_folder + f'{category}.md', 'w') as file:
        file.write(string)