---
layout: blog_post
title: Switching from Wordpress + MediaWiki to Jekyll
date: 2020-05-07 01:20 +0300
base: Blog
base_url: /blog 
author: Tzeny
thumbnail: 2020/05/jekyll-logo.jpeg
categories:
- software
tags:
- blog
- jekyll
- wordpress
- markdown
- netlify
- github pages
- import
- conversion
---

[Wordpress](https://wordpress.com/) was a great place for me to start my blog. It was easy to use, and had a beautiful post editor. However, issues arose around hosting it, mainly due to performance. So I decided to convert my blog to a static site using [jekyll](https://jekyllrb.com/) and host it using [Netlify](https://www.netlify.com/) (free for small sites). And oh boy, was it not easy. But let's start at the beggining.

[MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) is a great tool for collaborative wiki creation. However, I had stopped updating my wiki, and all I wanted was to preserve it for posterity. 

# What I had
## Wordpress

I had my blog running on a cheap online host, but it was struggling to keep up. Then I decided, "hey, I can host it at home". I combined dynamic dns (I don't have the option of buying a static IP from my internet provider unfortunately), with an nginx reverse proxy running on a DigitalOcean droplet in order to redirect the domain tzeny.com to my dynamic dns address.

This however introduced a lot of headaches and potential failure points: 
- dynamic dns reliability + cost
- nginx proxy crashed from time to time 
- DigitalOcean cost
- HTTPS certificate for tzeny.com
- Wordpress updates could fail bringing down the blog
- I only had on site backup

## MediaWiki

During my time spend getting aquianted with Machine Learning and Artificial Intelligence I decided to create a personal wiki to host all my notes. It was a very fun process, and MediaWiki made it easy to get started.

However, as with Wordpress it introduces unwanted complexity in the hosting process. 
- I had to run it locally
- when I eventually migrated to the reverse proxy it was hard to configure a subdomain for it
- needed additional php and database containers running
- I only had on site backup

## Distractions

I didn't want to have to wonder "hey, will my blog run today". I wanted to share my thoughts/tutorials/notes online. I wanted to write a piece and not have to worry if I could still read it two months down the line.

# What I wanted
- a write and forget platform, that wouldn't require me to perform any maintenance
- free/cheap hosting; I wanted high availability that was very hard to obtain using a home server
- a way to import all my existing work into this new platform

# How I did it
Whilist keeping these requirements in mind I stumbled across jekyll. It seemed perfect, if only I could import everything I already have into it. This turned out to be a challenge, as I had to use different importers for both WordPress and MediaWiki. 

## The base
After looking through a number of themes I decided to use the [devlopr](https://github.com/sujaykundu777/devlopr-jekyll) theme as a starting point. It was customizable, had a large number of features built in (Google Analytics support, dark theme, easily customizable About Me page just to name a few) and it seemed well structured code wise.

## Wordpress import
First I used this [wordpress-to-jekyll-exporter](https://github.com/benbalter/wordpress-to-jekyll-exporter) to export my posts to .md format. I also copied over all of my assets over into the jekyll project.

Then the fun began. I wrote a markdown importer into Python to further process the .md files to fix the asset links, galleries and other doodads that were not properly imported from Wordpress. 

For example the following code represents a wordpress gallery block: 

``` html
<div class="rl-gallery-container" id="rl-gallery-container-1" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-1" data-gallery_no="1"> 


<div class="rl-gallery-item">
<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214102.jpg" title="Front view, turned off" data-rl_title="Front view, turned off" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img src="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214102-300x225.jpg" width="300" height="225" /><span class="rl-gallery-caption"><span class="rl-gallery-item-title">Front view, turned off</span></span></a>
</div>

<div class="rl-gallery-item">
<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214125.jpg" title="The brains behind AIA, a Raspberry Pi 3" data-rl_title="The brains behind AIA, a Raspberry Pi 3" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img src="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214125-300x225.jpg" width="300" height="225" /><span class="rl-gallery-caption"><span class="rl-gallery-item-title">The brains behind AIA, a Raspberry Pi 3</span></span></a>
</div>

<div class="rl-gallery-item">
<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214218.jpg" title="Standard Raspbian with PIXEL desktop" data-rl_title="Standard Raspbian with PIXEL desktop" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img src="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214218-300x225.jpg" width="300" height="225" /><span class="rl-gallery-caption"><span class="rl-gallery-item-title">Standard Raspbian with PIXEL desktop</span></span></a>
</div>

<div class="rl-gallery-item">
<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214318.jpg" title="Kodi player, showing the music folders on a USB memory stick" data-rl_title="Kodi player, showing the music folders on a USB memory stick" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img src="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214318-300x225.jpg" width="300" height="225" /><span class="rl-gallery-caption"><span class="rl-gallery-item-title">Kodi player, showing the music folders on a USB memory stick</span></span></a>
</div></div> </div>
```

After conversion to proper jekyll/liquid syntax, using an include to make it easy to customize the galleries in the future:

{% raw %}
``` html
<div class="rl-gallery-container" id="rl-gallery-container-1" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-1" data-gallery_no="1"> 



{% include lightbox2_image.html original_image="/assets/img/posts/2017/07/IMG_20170730_214102.jpg" thumbnail_image="/assets/img/posts/2017/07/IMG_20170730_214102-300x225.jpg" caption="Front view, turned off" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/07/IMG_20170730_214125.jpg" thumbnail_image="/assets/img/posts/2017/07/IMG_20170730_214125-300x225.jpg" caption="The brains behind AIA, a Raspberry Pi 3" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/07/IMG_20170730_214218.jpg" thumbnail_image="/assets/img/posts/2017/07/IMG_20170730_214218-300x225.jpg" caption="Standard Raspbian with PIXEL desktop" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/07/IMG_20170730_214318.jpg" thumbnail_image="/assets/img/posts/2017/07/IMG_20170730_214318-300x225.jpg" caption="Kodi player, showing the music folders on a USB memory stick" set_name="set_1" %}</div> </div>
```
{% endraw %}

(I know, I know, there's still some extra stuff in there, but for now it doesn't affect functionality and I wanted to get back to writing, so I'll be leaving the problem of 100% correct formatting to future me)

It took some time for me to write proper scripts to do this. They can be found [here](https://github.com/Tzeny/tzeny.github.io/tree/master/assets/python).

## MediaWiki import

Next I used this [mediawiki-to-markdown](https://github.com/philipashlock/mediawiki-to-markdown) converter to export my wiki as .md files. I also copied all the images in the wiki over to the jekyll project.

Of course, they need further processing, to fix the links between them, properyly include images and create the categories. Some meta pages (for example category pages) I had to create by hand.

As with the wordpress import, it took some time for me to write proper scripts to do this. They can be found [here](https://github.com/Tzeny/tzeny.github.io/tree/master/assets/python).

## Putting it all together

Next I separated the blog and wiki into distinct subfolders inside _posts. I hid the Wiki posts (hidden: true in the Front Matter), so that I could use the pagination plugin only with the blog posts. 

I had to change the theme quite a bit to have all my blog posts under https://tzeny.com/blog and all my wiki entries under https://tzeny.com/wiki.

## Hosting

I chose netlify over [GitHubPages](https://pages.github.com/) as they let me use and plugins and theme I want, have paid hosting options should this website ever grow beyond their free plan and offer their own DNS service for private domains for free.

Funnily enough, I also tried GitHubPages, and now my site is forever (or at least until I delete and recreate the repo) live at both [https://tzeny.com](https://tzeny.com) and [https://tzeny.github.io/](https://tzeny.github.io/). Yay for redundancy?

# What I have

And now, after a couple of months since I first started looking into consolidating my blog and wiki into an easy to maintain resource I have this website, my very own online [demesne](https://en.wikipedia.org/wiki/Demesne). 

And I am so happy I can focus on creating content, and not on hosting it. (and the ocassional css fix xD)


