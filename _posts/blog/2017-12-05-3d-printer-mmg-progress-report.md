---
id: 269
title: '3D Printer – MMG – progress report 1'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=269
post_grid_post_settings:
  - 'a:14:{s:9:"post_skin";s:4:"flat";s:19:"custom_thumb_source";s:89:"https://tzeny.com/wp-content/plugins/post-grid/assets/frontend/css/images/placeholder.png";s:16:"thumb_custom_url";s:0:"";s:17:"font_awesome_icon";s:0:"";s:23:"font_awesome_icon_color";s:0:"";s:22:"font_awesome_icon_size";s:0:"";s:17:"custom_youtube_id";s:0:"";s:15:"custom_vimeo_id";s:0:"";s:21:"custom_dailymotion_id";s:0:"";s:14:"custom_mp3_url";s:0:"";s:20:"custom_soundcloud_id";s:0:"";s:16:"custom_video_MP4";s:0:"";s:16:"custom_video_OGV";s:0:"";s:17:"custom_video_WEBM";s:0:"";}'
thumbnail: 2017/12/IMG_20171203_135218-360x210.jpg
categories:
  - hardware
tags:
  - 3d printer
  - case
  - creeper
  - diy
  - mmg
  - raspberry
  - tarantula
---
About 2 month ago I bought a [Tarantula I3 3D printer from Aliexpress](https://www.aliexpress.com/item/2016-Newest-TEVO-Tarantula-I3Aluminium-Extrusion-3D-Printer-kit-printer-3d-printing-2-Rolls-Filament-8GB/32596996503.html?spm=a2g0s.9042311.0.0.6nm20Z). After getting it through customs and assembling it, I must say it is one of the most challenging and rewarding projects I have ever worked on. I only had time to work on it during weekends, but now I must say I am quite satisfied with the results. There is room for improvement, but that will come at a later date.

## Status right now

  * 3D printer operational, 1 role of magenta filament installed
  * printed a [radial fan fang](https://www.thingiverse.com/thing:2175956) to improve future print accuracy(and then printed a new and improved one)
  * installed [OctoPrint](http://octoprint.org/) on a RaspberryPi 2 and connected it to the printer
  * added LED light strips

<div class="rl-gallery-container" id="rl-gallery-container-21" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-21" data-gallery_no="21"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171201_112536.jpg" title="On the left a creeper I have had for 3 years now, on the right his bigger brother who was just born" data-rl_title="On the left a creeper I have had for 3 years now, on the right his bigger brother who was just born" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171201_112536-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">On the left a creeper I have had for 3 years now, on the right his bigger brother who was just born</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_094505.jpg" title="And now a smaller one; I experimented with a glass bed while printing them" data-rl_title="And now a smaller one; I experimented with a glass bed while printing them" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_094505-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">And now a smaller one; I experimented with a glass bed while printing them</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_022656.jpg" title="Trying to print the bottom part of a Raspberry Pi case" data-rl_title="Trying to print the bottom part of a Raspberry Pi case" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_022656-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Trying to print the bottom part of a Raspberry Pi case</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_022742.jpg" title="But the first layer does not stick to the glass unfortunately so I have to call it off" data-rl_title="But the first layer does not stick to the glass unfortunately so I have to call it off" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_022742-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">But the first layer does not stick to the glass unfortunately so I have to call it off</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_160553.jpg" title="A completed case (printed on the original bed)" data-rl_title="A completed case (printed on the original bed)" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_160553-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">A completed case (printed on the original bed)</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_160614.jpg" title="Incidentally this is the Raspberry Pi responsible for my VPN" data-rl_title="Incidentally this is the Raspberry Pi responsible for my VPN" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_160614-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Incidentally this is the Raspberry Pi responsible for my VPN</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_160619.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_160619-300x225.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_160600.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_160600-300x225.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_172618.jpg" title="All of the rejects and waste from failed prints" data-rl_title="All of the rejects and waste from failed prints" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_172618-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">All of the rejects and waste from failed prints</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_010058.jpg" title="The evolution of the parts" data-rl_title="The evolution of the parts" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_010058-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The evolution of the parts</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_134855.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_134855-300x225.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_134904.jpg" title="The evolution of the calibration cube throughout different prints" data-rl_title="The evolution of the calibration cube throughout different prints" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_134904-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The evolution of the calibration cube throughout different prints</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_134915.jpg" title="Another case for the OctoPrint Rasberry" data-rl_title="Another case for the OctoPrint Rasberry" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_134915-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Another case for the OctoPrint Rasberry</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_134922.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_134922-300x225.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_134930.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_134930-300x225.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_185142.jpg" title="This is the state of the printer now" data-rl_title="This is the state of the printer now" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_185142-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is the state of the printer now</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_134847.jpg" title="I added the LEDs because the printer is in a darker corner of my room" data-rl_title="I added the LEDs because the printer is in a darker corner of my room" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_134847-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">I added the LEDs because the printer is in a darker corner of my room</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171202_185139.jpg" title="The LCD will be mounted on top of the printer" data-rl_title="The LCD will be mounted on top of the printer" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171202_185139-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The LCD will be mounted on top of the printer</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_135209.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_135209-225x300.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_135212.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_135212-225x300.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_135218.jpg" title="Unfortunately (or not) the LEDs have different colors" data-rl_title="Unfortunately (or not) the LEDs have different colors" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_135218-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Unfortunately (or not) the LEDs have different colors</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_135223.jpg" title="DIY spool holder" data-rl_title="DIY spool holder" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-21">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_135223-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">DIY spool holder</span></span></a>
</div></div> </div>

## Future plans:

  * Mount OctoPrint Raspberry to printer frame
  * Mount LCD to printer frame
  * Print backpane for PSU
  * Cable management
  * Printing on a glass bed
  * Increase print accuracy
  * Calibrate printer
