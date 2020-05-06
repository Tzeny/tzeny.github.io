---
id: 893
title: Silencing a noisy car inverter
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: https://tzeny.com/?p=893
thumbnail: 2019/12/body9.jpg
categories:
  - engineering
  - hardware
tags:
  - 12V
  - 220V
  - ac
  - dc
  - fan
  - inverter
  - silence
excerpt: I bought a 300W continous / 600W peak 12V DC to 220V AC inverter for my car. It was pretty cheap, at around 25$. However it has one major drawback, a continuously on small noisy fan. 
---
<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure> 

I bought a 300W continous / 600W peak 12V DC to 220V AC inverter for my car. It was pretty cheap, at around 25$. However it has one major drawback, a continuously on small noisy fan. 

So I decided to cut open its top part and add a 120mm PC fan on top. 

**Note: be careful when working with the inverter’s insides as it has live 220V exposed pins and components**

### Parts list

  * Generic 12V DC to 220V AC inverter – 25$
  * 120 mm PC Fan (bonus: it has blue LED lights and a temperature sensor) – 0$ (had one laying around)
  * 120mm PC Fan grill and dust cover – 0$ (had some laying around)

### Tools list

  * Angle grinder (I initially tried a small multitool but the aluminum body is pretty thick)
  * Hot glue gun 

## The build process

Idea: Add a fan on top of the inverter, cutting small section (or maybe a large section) of the top part of to allow cool air to get in. The fan will be covered by a dust filter, and blow air into the inverter. The air will exit through the lateral holes already present in the inverter.

Upon opening it I discovered its internal fan was powered by a 12V header, which is just perfect as 120mm PC fans are also powered by a 12V input, and are significantly quieter (mine was basically indistinguishable from background noise) whilst being able to move the same amount of air (in this case, size does matter).

As a bonus, the one I had also has blue LEDs that can be toggled and a temperature sensor, which I taped to a piece of metal in direct contact with some how ICs. 

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-41" data-gallery_id="895"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-41" data-gallery_no="41"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body1.jpg" thumbnail_image="/assets/img/posts/2019/12/body1.jpg" caption="This is how the inverter looks like, with 3D printed non conductive L brackets attached" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body2.jpg" thumbnail_image="/assets/img/posts/2019/12/body2-300x225.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body3.jpg" thumbnail_image="/assets/img/posts/2019/12/body3-300x225.jpg" caption="This is the part we'll have to remove in order to allow the air from the fan to cool the insides of the inverter" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body4.jpg" thumbnail_image="/assets/img/posts/2019/12/body4.jpg" caption="To take it apart we have to remove the 2 top screws from each end" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body5.jpg" thumbnail_image="/assets/img/posts/2019/12/body5-300x225.jpg" caption="Opening it reveals the header and cables used to power its internal fan; voltage: ~12V" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body6.jpg" thumbnail_image="/assets/img/posts/2019/12/body6-300x225.jpg" caption="The top part after being cut with the angle grinder" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/bodywelp-1.jpg" thumbnail_image="/assets/img/posts/2019/12/bodywelp-1-300x225.jpg" caption="Fan's temperature sensor was attached to this metal piece that holds some hot ICs flat against the side of the case for heat dissipation" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/bodywelp2.jpg" thumbnail_image="/assets/img/posts/2019/12/bodywelp2-300x225.jpg" caption="I used the hole of the old fan to pass the power and sensor wires of the new fan" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body7.jpg" thumbnail_image="/assets/img/posts/2019/12/body7-300x225.jpg" caption="First I glued in place the black fan guard, then clipped in the fan" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body8.jpg" thumbnail_image="/assets/img/posts/2019/12/body8-300x225.jpg" caption="Finally I screwed in a dust filter on the fan" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/body9.jpg" thumbnail_image="/assets/img/posts/2019/12/body9-300x225.jpg" caption="Bonus: LED light on" set_name="set_1" %}
</div></div></div> 

## The result

A quiet 300W inverter, that you can easily sleep next to. It will be useful for charging my phone or laptop overnight in <a rel="noreferrer noopener" aria-label="Rusty (opens in a new tab)" href="https://tzeny.com/2019/11/14/van-life-the-story-so-far/" target="_blank">Rusty</a>. 

Since the inverter draws about 0.30A in standby, I decided to leave the fan’s LEDs always on as a power indicator (since it can’t be easily heard).
