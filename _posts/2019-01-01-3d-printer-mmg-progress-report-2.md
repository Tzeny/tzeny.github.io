---
id: 479
title: 3D Printer – MMG – progress report 2
date: 2019-01-01T18:14:32+00:00
author: Tzeny
layout: post
guid: http://192.168.0.110:8000/?p=479
permalink: /2019/01/01/3d-printer-mmg-progress-report-2/
post_grid_post_settings:
  - 'a:14:{s:9:"post_skin";s:4:"flat";s:19:"custom_thumb_source";s:89:"https://tzeny.com/wp-content/plugins/post-grid/assets/frontend/css/images/placeholder.png";s:16:"thumb_custom_url";s:0:"";s:17:"font_awesome_icon";s:0:"";s:23:"font_awesome_icon_color";s:0:"";s:22:"font_awesome_icon_size";s:0:"";s:17:"custom_youtube_id";s:0:"";s:15:"custom_vimeo_id";s:0:"";s:21:"custom_dailymotion_id";s:0:"";s:14:"custom_mp3_url";s:0:"";s:20:"custom_soundcloud_id";s:0:"";s:16:"custom_video_MP4";s:0:"";s:16:"custom_video_OGV";s:0:"";s:17:"custom_video_WEBM";s:0:"";}'
image: /wp-content/uploads/2019/01/IMG_20190101_120524-360x210.jpg
categories:
  - miscellaneous
---
It’s been more than a year since my last progress report, and about 1.2 years since I bought my 3D Printer. I have made some updates to it, which I’ll be describing below.

Report 1: [3D Printer – MMG – progress report 1](https://tzeny.com/2017/12/05/3d-printer-mmg-progress-report/)

Parts used:

  * [Tevo Tarantula LCD Bracket](https://www.thingiverse.com/thing:1622728)
  * [Tarantula MOSFET mount](https://www.thingiverse.com/thing:2069507)

Status right now:

  * Removed the bottom LED light strip
  * Tested OctoPrint with a web camera (pending frame mounting)
  * Cable management done
  * MOSFET back plate done (to prevent shorts)
  * Added plastic feet to the printer to reduce noise and vibrations
  * Using glass bed for printing (makes it much easier to remove a print after it is done)
  * Upgraded the spool holder to increase structural integrity
  * Mounted LCD to frame
  * RPi OctoPrint server has its own case, but is not mounted to the frame due to lack of space<figure class="wp-block-gallery columns-3 is-cropped">

<ul class="blocks-gallery-grid">
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120524-768x1024.jpg" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120524-768x1024.jpg)</a><figcaption class="blocks-gallery-item__caption">Overview of the printer</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120528-768x1024.jpg" data-rel="lightbox-image-1" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120528-768x1024.jpg)</a><figcaption class="blocks-gallery-item__caption">I have finally done some much needed cable management</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120531-768x1024.jpg" data-rel="lightbox-image-2" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120531-768x1024.jpg)</a><figcaption class="blocks-gallery-item__caption">The LCD has been mounted to the top of the printer frame</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120540-768x1024.jpg" data-rel="lightbox-image-3" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120540-768x1024.jpg)</a><figcaption class="blocks-gallery-item__caption">I’ve designed a slightly shifted LCD bracket for this</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120545-1024x768.jpg" data-rel="lightbox-image-4" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120545-1024x768.jpg)</a><figcaption class="blocks-gallery-item__caption">The shifted right bracket can be better seen from this angle</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120549-1024x768.jpg" data-rel="lightbox-image-5" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120549-1024x768.jpg)</a><figcaption class="blocks-gallery-item__caption">The spool holder received and updated after a small accident</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120552-1024x768.jpg" data-rel="lightbox-image-6" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120552-1024x768.jpg)</a><figcaption class="blocks-gallery-item__caption">The RPi Octoprint server in its pink case; it was mounted to the top of the frame, but that obstructed full movement on the Z axis</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG_20190101_120606-1024x768.jpg" data-rel="lightbox-image-7" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120606-1024x768.jpg)</a><figcaption class="blocks-gallery-item__caption">I have added plastic buffers, to keep the printer from sliding around; this has significantly reduced the noise generated by the printer</figcaption></figure>
  </li>
  <li class="blocks-gallery-item">
    <figure><a href="https://tzeny.com/wp-content/uploads/2019/01/octoprint-1024x955.jpg" data-rel="lightbox-image-8" data-rl_title="" data-rl_caption="" title="">![My helpful screenshot](/assets/img/posts/2019/01/octoprint-1024x955.jpg)</a><figcaption class="blocks-gallery-item__caption">A screenshot of the OctoPrint server</figcaption></figure>
  </li>
</ul></figure> 

Future plans

  * Get a better, quieter PSU
  * Mount RPi to the back of the LCD holder
  * Mount Webcam for time lapses
  * Play around with the print settings to reduce stringing
  * Replace extruder with better version capable of handling elastic filament
