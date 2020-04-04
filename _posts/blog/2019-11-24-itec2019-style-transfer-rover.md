---
id: 782
title: 'iTec2019 – Style transfer rover'
base: Blog
base_url: /blog
author: teny96@gmail.com
layout: blog_post
guid: https://tzeny.com/?p=782
thumbnail: 2019/11/top8.jpeg
categories:
  - artificialintelligence
  - engineering
  - hardware
tags:
  - gan
  - intel
  - ncs2
  - openvino
  - raspberry
  - style transfer
---
<a rel="noreferrer noopener" aria-label="iTEC (opens in a new tab)" href="https://itec.ligaac.ro/" target="_blank">iTEC</a> is a contest dedicated to pupils and students with an interest in IT. This was its 13th edition; over 200 participants showed up. It consists of a couple of short (~6 hour) challenges and 4 hackathons (web, mobile, game dev and embedded).

Together with Arin we took part in the embedded hackathon. We received:

  * 1 x 4WD robotics kit, similar to this <a rel="noreferrer noopener" href="https://www.amazon.com/Robot-Chassis-Motor-Arduino-Raspberry/dp/B07F759T89?ref_=nav_custrec_signin&" target="_blank">one</a>
  * 1 x Raspberry Pi 3
  * 1 x <a rel="noreferrer noopener" aria-label="Intel NCS2 (opens in a new tab)" href="https://software.intel.com/en-us/neural-compute-stick" target="_blank">Intel NCS2</a>
  * 1 x Raspberry Pi Camera
  * assorted accessories like H bridges, level converters, battery holders and screws

## Our idea

We wanted to build a rover that ran different style transfer Generative Adversarial networks on the NCS2. It would be remote controlled, with controls for rover movement and camera movement.

This will allow people to explore the real world through the eyes of Van Gogh, or an acid tripping person. And for those of you thinking we could’ve done it with a phone and a cloud computer, well, we could’ve but GLaDOS wanted to live.

## The hard how behind it

For the camera we used a 2 axis mount with <a rel="noreferrer noopener" aria-label="SG 90 (opens in a new tab)" href="https://components101.com/servo-motor-basics-pinout-datasheet" target="_blank">SG 90</a> servos. <figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/11/camera-1024x768.jpeg) </figure> 

We mounted it upside down because it looked cool, and it kind of resembled GLaDOS. We had some issues with the servo driver, and ended up switching to the **pigpio** library instead of the standard **RPi.GPIO** and it worked out pretty well.

The engines were wired together in 2 parallel groups (left and right) and used an H bridge powered by 4 AA batteries (later 8 AA batteries in parallel) to control them.<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/11/engines-1024x768.jpeg) </figure> 

The brain of the whole machine is a Raspberry Pi 3, which controls the 4 motors and 2 camera servos through 3.3 to 5 bidirectional <a rel="noreferrer noopener" aria-label="logic level converters (opens in a new tab)" href="https://www.addicore.com/Logic-Level-Converter-Bi-Directional-5V-to-3-3V-p/227.htm" target="_blank">logic level converters</a>. Inference was performed on the Intel NCS 2. <figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/11/brains-768x1024.jpeg) </figure> 

To top it off we added a small <a rel="noreferrer noopener" aria-label="128 x 128 TFT Display (opens in a new tab)" href="https://www.aliexpress.com/item/33014277663.html" target="_blank">128 x 128 TFT Display</a> and a 10Ah power bank to power the Rasberry.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-33" data-gallery_id="788"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-33" data-gallery_no="33"> 
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top99.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top99-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top8.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top8-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top7.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top7-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top6.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top6-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top5.jpeg" title="Image processed to the 'mosaic' style" data-rl_title="Image processed to the 'mosaic' style" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top5-300x225.jpeg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Image processed to the 'mosaic' style</span></span></a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top4.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top4-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top3.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top3-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top2.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top2-300x225.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/top.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-33">![My helpful screenshot](/assets/img/posts/2019/11/top-300x225.jpeg)</a>
  </div>
</div></div></div> 

## The soft how behind it

In true hackathon style we ran 3 servers on the Raspberry Pi. 

One that ran the inference, created the video stream and provided a route allowing the client to request a model change. 

One was a Flask REST API that allowed the client to control the motors and the camera servos.

And finally, a small Python 3 HTTP server that provided the frontend. Although initially we planned on using it from the laptop, I decided to turn it into a mobile ‘app’ with 2 joysticks.<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.03-1024x485.jpeg) </figure> 

The cyan joystick controls the motor, and the orange one controls the camera.

We found a number of network styles pretrained, and we also trained one of our own based on this image:<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/11/acid.resized.jpg) </figure> 

## The results

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-34" data-gallery_id="799"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-34" data-gallery_no="34"> 
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.04.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.04-300x142.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.041.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.041-300x142.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.03-1.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.03-1-300x142.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.054.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.054-300x142.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.043.jpeg" title="Camera covered, image generated from blackness" data-rl_title="Camera covered, image generated from blackness" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.043-300x142.jpeg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Camera covered, image generated from blackness</span></span></a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.05.jpeg" title="Camera covered, image generated from blackness" data-rl_title="Camera covered, image generated from blackness" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.05-300x142.jpeg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Camera covered, image generated from blackness</span></span></a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/WhatsApp-Image-2019-11-24-at-14.25.051.jpeg" title="Camera covered, image generated from blackness" data-rl_title="Camera covered, image generated from blackness" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/WhatsApp-Image-2019-11-24-at-14.25.051-300x142.jpeg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Camera covered, image generated from blackness</span></span></a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/hand.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/hand-225x300.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/welp.jpeg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/welp-225x300.jpeg)</a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/11/muschi.jpeg" title="Failing attempts at training a GAN; on the bright side it learned to color skin green" data-rl_title="Failing attempts at training a GAN; on the bright side it learned to color skin green" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-34">![My helpful screenshot](/assets/img/posts/2019/11/muschi-225x300.jpeg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Failing attempts at training a GAN; on the bright side it learned to color skin green</span></span></a>
  </div>
</div></div></div> 

We managed to win second place using our little rover. A good hackathon indeed.
