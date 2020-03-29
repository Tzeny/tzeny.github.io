---
id: 29
title: 'A quick look at my current car computer – AIA v0.2'
base: Blog
base_url: /blog
author: Tzeny
layout: post
guid: http://timisoarath.ro/?p=29
thumbnail: 2017/07/IMG_20170730_214102.jpg
categories:
  - hardware
tags:
  - car
  - case
  - computer
  - kodi
  - music
  - pixel
  - player
  - raspberry
  - raspbian
---
Because I am planning to embark on quite an epic journey with my friends, I needed to build a car computer. Her name was to be AIA v0.2. For the computing part I decided on a Raspberry Pi 3, with a 7 inch capacitive touch display. The main purpose of the computer right now is to be an advanced music player (features include: playlists, easy navigation, playing music form an USB memory stick)

This is the end result:

<div class="rl-gallery-container" id="rl-gallery-container-1" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-1" data-gallery_no="1"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214102.jpg" title="Front view, turned off" data-rl_title="Front view, turned off" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170730_214102-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Front view, turned off</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214125.jpg" title="The brains behind AIA, a Raspberry Pi 3" data-rl_title="The brains behind AIA, a Raspberry Pi 3" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170730_214125-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The brains behind AIA, a Raspberry Pi 3</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214218.jpg" title="Standard Raspbian with PIXEL desktop" data-rl_title="Standard Raspbian with PIXEL desktop" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170730_214218-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Standard Raspbian with PIXEL desktop</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170730_214318.jpg" title="Kodi player, showing the music folders on a USB memory stick" data-rl_title="Kodi player, showing the music folders on a USB memory stick" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170730_214318-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Kodi player, showing the music folders on a USB memory stick</span></span></a>
</div></div> </div>

Parts used:

  * [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
  * [Waveshare 7” touch display](http://www.waveshare.com/wiki/7inch_HDMI_LCD_(C))
  * Plastic housing
  * Power and audio out wires

Software used:

  * Raspbian with pixel desktop ([download](https://www.raspberrypi.org/downloads/raspbian/))
  * Kodi media player ([wiki](http://kodi.wiki/view/Raspberry_Pi))

I considered running Android on the Raspberry, and using an app for music but I ran into some issues. Although I got it up and running (I used RT Android, not the vanilla one), it was a bit sluggish. This coupled with the fact that my touch screen wasn’t one of the best, made it difficult to use. Another big issue with it was that I didn’t manage to get it to play the music from my USB memory stick with any dedicated music apps (with Es Explorer Pro it worked, but its music playing functionality is minimal).

The cardboard box was the original car computer that I built for another trip last year. It is running the latest version of RT Android, which is an independently developed version of Android designed to support real time applications. You can check it out below.

[RT Android for Raspberry Pi 3](https://rtandroid.embedded.rwth-aachen.de/downloads/raspberry-pi/)

<a href="https://tzeny.com/wp-content/uploads/2017/07/android.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/07/android-300x225.jpg)</a>

## 1. Hardware

### a. LCD

The first thing I did cut a large viewport into my plastic casing (which I unfortunately have no original photos of), so that the LCD screen could be viewed.

<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG\_20170715\_192150.jpg" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170715_192150-287x300.jpg)</a>

 

Afterwards I installed the screen. But, since only 2 of the screw holes were a match I had to glue in 2 more on the other side. Epoxi for the win here.

<a href="https://tzeny.com/wp-content/uploads/2017/07/holes.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/07/holes-300x225.png)</a>

### b. Raspberry

Then, I had to think about mounting the Raspberry. Considering this is just an alpha build of AIA (that’s the computer’s name), v0.2 to be specific, I though I would take the simple route of mounting the Rasberry in a case and putting that behind the LCD. More cutting ensued.

<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG\_20170715\_201749.jpg" data-rel="lightbox-image-3" data-rl\_title="" data-rl\_caption="" title=""><img class="alignnone wp-image-39 size-medium" src="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_201749-300x225.jpg" alt="" width="300" height="225" srcset="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_201749-300x225.jpg 300w, https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_201749-768x576.jpg 768w, https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_201749-1024x768.jpg 1024w, https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_201749.jpg 1200w" sizes="(min-width: 960px) 75vw, 100vw" /></a> <a href="https://tzeny.com/wp-content/uploads/2017/07/IMG\_20170715\_213541.jpg" data-rel="lightbox-image-4" data-rl\_title="" data-rl\_caption="" title=""><img class="alignnone wp-image-40 size-medium" src="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_213541-300x225.jpg" alt="" width="300" height="225" srcset="https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_213541-300x225.jpg 300w, https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_213541-768x576.jpg 768w, https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_213541-1024x768.jpg 1024w, https://tzeny.com/wp-content/uploads/2017/07/IMG_20170715_213541.jpg 1200w" sizes="(min-width: 960px) 75vw, 100vw" /></a> <a href="https://tzeny.com/wp-content/uploads/2017/07/IMG\_20170715\_224431.jpg" data-rel="lightbox-image-5" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170715_224431-300x225.jpg)</a>

The last step was adding a coat of black paint.

 

## 2. Software

### a. Raspbian and LCD

After downloading [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), you just have to write it to an uSD Card. There is a very good tutorial for this [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

After writing the image open up the file config.txt on the uSD Card, and append the following lines:

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="text codecolorer">
    max_usb_current=1<br /> hdmi_group=2<br /> hdmi_mode=87<br /> hdmi_cvt 1024 600 60 6 0 0 0<br /> hdmi_drive=1
  </div>
</div>

These is required for the proper operation of the LCD screen. After that put the card into your Raspberry.

### b. Kodi

After it boots up, just type into your console:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="br0">[</span><span class="kw2">cc</span><span class="br0">]</span><span class="kw2">sudo</span> <span class="kw2">apt-get update</span><br /> <br /> <span class="kw2">sudo</span> <span class="kw2">apt-get upgrade</span><br /> <br /> <span class="kw2">sudo</span> <span class="kw2">apt-get install</span> kodi
  </div>
</div>

And after that you have Kodi. But, in my case at least, the touch screen wasn’t properly working and I had to follow [these instructions](http://markamc.traki-iski.co.uk/raspberry-pi-2-osmc-egalax-touchscreen/) first.

And that’s it. Now you should be able to open Kodi and browse for music, pictures and more.

<a href="https://tzeny.com/wp-content/uploads/2017/07/IMG\_20170715\_224317.jpg" data-rel="lightbox-image-6" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/07/IMG_20170715_224317-300x225.jpg)</a>

### c. Matchbox Keyboard

Another useful piece of software I highly recommend is matchbox keyboard. This is how it looks and it is an invaluable piece of software on a touch only Raspberry.

<a href="https://tzeny.com/wp-content/uploads/2017/07/keyboard.jpg" data-rel="lightbox-image-7" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/07/keyboard-300x175.jpg)</a>

All you need to do to install it is type:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> <span class="kw2">apt-get install</span> matchbox-keyboard
  </div>
</div>

A shortcut will be created in the Accessories tab of the Menu.
