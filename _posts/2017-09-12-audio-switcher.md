---
id: 131
title: Audio switcher
date: 2017-09-12T20:00:28+00:00
author: Tzeny
layout: post
guid: http://192.168.0.110:8000/?p=131
permalink: /2017/09/12/audio-switcher/
thumbnail: 2017/09/final-360x210.jpg
categories:
  - hardware
tags:
  - "3.5"
  - audio
  - box
  - jack
  - switch
---
So, since I got an old audio station on my desk, I wanted to be able to connect both the desk PC and another device (phone, laptop etc.) to the station without too much hassle. The best way to do this was a 3.5 mm audio switcher. Since after searching online I came up empty handed I decided to build one myself. This is the final result:

<div class="rl-gallery-container" id="rl-gallery-container-3" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-3" data-gallery_no="3"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/final_3.jpg" title="Audio switcher front" data-rl_title="Audio switcher front" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-3">![My helpful screenshot](/assets/img/posts/2017/09/final_3-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Audio switcher front</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/final_2.jpg" title="Audio switcher back" data-rl_title="Audio switcher back" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-3">![My helpful screenshot](/assets/img/posts/2017/09/final_2-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Audio switcher back</span></span></a>
</div></div> </div>

Parts used:

  * Old toy plastic box
  * 2 pole 3 way switch
  * 3 x 3.5 mm female stereo jacks
  * some colored wires

Tools used:

  * Electric screwdriver and bit
  * [Easy PDA](https://easyeda.com/)

<figure id="attachment_137" aria-describedby="caption-attachment-137" style="width: 300px" class="wp-caption alignnone">![My helpful screenshot](/assets/img/posts/2017/09/pieces-300x225.jpg)<figcaption id="caption-attachment-137" class="wp-caption-text">The PCBs were not used in the end</figcaption></figure>

## 1. Preparing the plastic box

First up, I had to come up with a way to mount everything inside the box. I decided to do this before doing any soldering, just to make sure everything worked. To this end, I used an electric screwdriver with a bit the same size as my switch. Fortunately, the bit was also perfect for the 3.5 mm jack holes.

<div class="rl-gallery-container" id="rl-gallery-container-4" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-4" data-gallery_no="4"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hole_1.jpg" title="The bit and the hole created by it; I had to smooth the hole a bit afterwards" data-rl_title="The bit and the hole created by it; I had to smooth the hole a bit afterwards" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-4">![My helpful screenshot](/assets/img/posts/2017/09/hole_1-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The bit and the hole created by it; I had to smooth the hole a bit afterwards</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hole_2.jpg" title="The switch fitted through the hole, it will be secured by a washer and nut" data-rl_title="The switch fitted through the hole, it will be secured by a washer and nut" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-4">![My helpful screenshot](/assets/img/posts/2017/09/hole_2-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The switch fitted through the hole, it will be secured by a washer and nut</span></span></a>
</div></div> </div>

## 2. Connections

So, now satisfied that everything fitted in the box, I needed to make all the required connections. To this end I used [Easy PDA](https://easyeda.com/), an online tool that lets you easily create sketches and PCB layouts (not needed for this project).

<figure id="attachment_132" aria-describedby="caption-attachment-132" style="width: 300px" class="wp-caption alignnone">![My helpful screenshot](/assets/img/posts/2017/09/sketch-300x159.jpg)<figcaption id="caption-attachment-132" class="wp-caption-text">Green wire – GND  
Grey wire – left channel  
Red wire – right channel</figcaption></figure>

The unconnected pins are used to determine if a jack is inserted or not, which was not necessary for our build.

Next up, I had to solder everything together. The jacks were a bit of a pain, as the plastic around the connection pins melted sometimes while I was soldering, but eventually I got everything connected.

<figure id="attachment_140" aria-describedby="caption-attachment-140" style="width: 300px" class="wp-caption alignnone">![My helpful screenshot](/assets/img/posts/2017/09/connections-300x225.jpg)<figcaption id="caption-attachment-140" class="wp-caption-text">Everything is finally wired up</figcaption></figure>

I also took this opportunity to do a quick check, just to make sure everything worked. First using a multimeter to check for shorts, then plugging it into the station and testing it with my phone.

## 3. Putting it all together

So, now with everything connected, I just had to put it all in the box and fit the jacks and switch through their respective holes.

![My helpful screenshot](/assets/img/posts/2017/09/box_1-300x225.jpg) 

I also did another check now, just to make sure. But quickly, I realized I had a problem. The jacks were very easy pushed inside. I thought I could solve this with glue but I was wrong. So, what to do? Lego to the rescue!

![My helpful screenshot](/assets/img/posts/2017/09/box_2-300x225.jpg) 

A lego brick was the perfect width and length to keep everything stable. It was a tight fit, but that was very good in this case.

## 4. Final touches

As a final touch, I marked the Output and Input on the back, and added some black marker lines to indicate which input the switch was connected to. In the end it looked better than expected.

![My helpful screenshot](/assets/img/posts/2017/09/final_2-300x225.jpg) 

Using some double tape, I fixed it on my desk, where it has been doing its job for the pas few months.
