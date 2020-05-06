---
id: 835
title: DIY Vintage Fallout Radio ♫
base: Blog
base_url: /blog
author: Tzeny
excerpt: My Secret Santa match is a work mate who is a yuge fan of the Fallout series. I remembered talking with him about how cool it would be to place a Bluetooth speaker inside of an old radio enclosure and listen to Galaxy News radio. 
layout: blog_post
guid: https://tzeny.com/?p=835
thumbnail: 2019/12/radio_live.jpg
categories:
  - engineering
  - hardware
tags:
  - antenna
  - bluetooth
  - diy
  - fallout
  - fixing
  - long wave
  - medium wave
  - radio
  - vintage
---
<iframe class="youtube-iframe" src="https://www.youtube-nocookie.com/embed/Nl0GyLE6BlM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

With Christmas (and hopefully a good shower of snow) just around the corner, it was time for one of my favorite events of the year: Secret Santa.

My Secret Santa match is a work mate who is a yuge fan of the Fallout series. I remembered talking with him about how cool it would be to place a Bluetooth speaker inside of an old radio enclosure and listen to Galaxy News radio. 

But I decided to take it one step further. Why not get an old, functioning radio and add a Bluetooth module to it; that way we could still use it to listen to real life radio stations (even ones broadcasting on long and medium wave :o), and it would also add that vintage sound vibe to the Fallout music. 

## Hardware

  * Loewe T304 radio, manufactured in 1976 – 12$
  * 12V – 24V TP3110 Bluetooth audio amplifier board – 10$
  * 220V AC – 12V DC transformer – 0$ (had one laying around; a DC to DC booster would’ve been better)
  * 3 position double rocker switch – 0$ (had one laying around)
  * Wires
  * Heat shrink tubing  
  
    **Note: be very careful when working with the insides of the radio and the AC – DC transformer as there are exposed AC high voltage pins**

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-35" data-gallery_id="836"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-35" data-gallery_no="35"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/radio_1.jpg" thumbnail_image="/assets/img/posts/2019/12/radio_1-300x225.jpg" caption="Loewe T304 radio front" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/radio_3.jpg" thumbnail_image="/assets/img/posts/2019/12/radio_3-300x225.jpg" caption="Loewe T304 radio back" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/radio_2.jpg" thumbnail_image="/assets/img/posts/2019/12/radio_2-300x225.jpg" caption="Loewe T304 radio insides" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/bluetooth_amp.jpg" thumbnail_image="/assets/img/posts/2019/12/bluetooth_amp-300x225.jpg" caption="TPA 3110 Bluetooth amplifier" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/ac_transformer.jpg" thumbnail_image="/assets/img/posts/2019/12/ac_transformer-300x225.jpg" caption="AC Transformer - be very careful when working with it, as it has exposed high voltage pins" set_name="set_1" %}
</div></div></div> 

What’s really cool about this radio is that it can also receive Long and Medium wave broadcasts. I managed to listen to a station in Spain that was emitting on long wave from my kitchen. 

List of long wave radio stations in Europe: <a href="https://www.asiawaves.net/longwave-radio.htm" target="_blank" rel="noreferrer noopener" aria-label=" (opens in a new tab)">https://www.asiawaves.net/longwave-radio.htm</a>

## Putting it all together

{% include figure_caption.html url="/assets/img/posts/2019/12/Capture-1024x679.jpg" description="" %} 

This is the schematic of the end product. 

Of course, I should’ve used the Radio’s build in AC – DC converter. But it only outputted 6V, and the Blutooth module needed at least 12V to run properly; this problem could’ve easily been solved by a DC – DC booster, but I didn’t have one on hand so I proceeded by using a AC – DC converter I had laying around from an old charger.

But, first things first.

**Note: always use heat shrink tubing, as it provides structural support for your wires in addition to electrical insulation**

### Fixing the antenna

The antenna was secured with a small screw at the base. 

The antenna was also completely folded, and missing it’s head cap; I managed to push the first part out with a screwdriver, and the rest I pushed and pulled with a pliers. To my relief, the top had a small thread, and I put on a replacement cap from an antenna I had lying around. A good alternative would’ve been to use a small anti lock nut.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-36" data-gallery_id="848"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-36" data-gallery_no="36"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/antenna_3.jpg" thumbnail_image="/assets/img/posts/2019/12/antenna_3-300x205.jpg" caption="Broken antenna base" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/antenna_1.jpg" thumbnail_image="/assets/img/posts/2019/12/antenna_1-300x225.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/antenna_2.jpg" thumbnail_image="/assets/img/posts/2019/12/antenna_2-225x300.jpg" caption="Replacement antenna head" set_name="set_1" %}
</div></div></div> 

### The Bluetooth circuit

Next, I had to solder together my AC – DC 12V transformer, the Bluetooth module and the rocker switch.

Note: a single rocker switch would have been sufficient in this case, as the speaker is always connected to the radio PCB’s ground through the third wire in the middle. 

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-37" data-gallery_id="852"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-37" data-gallery_no="37"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/1.jpg" thumbnail_image="/assets/img/posts/2019/12/1-300x225.jpg" caption="The insides of the radio, unaltered" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/2.jpg" thumbnail_image="/assets/img/posts/2019/12/2-300x225.jpg" caption="I soldered my converters' inputs to the inputs coil of the radio's transformer" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/3.jpg" thumbnail_image="/assets/img/posts/2019/12/3-300x225.jpg" caption="AC-DC converter soldered and working" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/4.jpg" thumbnail_image="/assets/img/posts/2019/12/4-300x225.jpg" caption="I made a small plastic shield, as the AC-DC converter will be tightly squeezed in this particular spot, and I was weary of shorts" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/5.jpg" thumbnail_image="/assets/img/posts/2019/12/5-300x225.jpg" caption="Next I connected the double rocker switch and the Bluetooth module; note the heat shrink tubing" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/6.jpg" thumbnail_image="/assets/img/posts/2019/12/6-300x225.jpg" caption="Finally, it was time to wire it all up" set_name="set_1" %}
</div></div></div> 

### First integration test<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure> 

I was ecstatic to see it working :D.

### Closing it all up

To close it up, I had to find a place for the Bluetooth board and the converter. Fortunately the radio has a battery bay that is not connected to anything. Its wires broke off sometime in the past, as it’s datasheet suggests it is meant to be powered by 4 x 1.5V batteries.

I used my small Dremel style multi tool to make the necessary cuts and holes for the rocker switch and Bluetooth volume knob.

I also tried desoldering the SMT indicator LED used by the Bluetooth board to try to use an old red LED instead. For some reason it worked at first, but then it prevented the Bluetooth board from starting after it was mounted, so I ditched it.

I also had to cut the plastic shield in half to properly fit the transformer. 

For the volume knob I had to make an indent, as the plastic was to thick compared to the length of the thread.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-38" data-gallery_id="864"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-38" data-gallery_no="38"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/1-1.jpg" thumbnail_image="/assets/img/posts/2019/12/1-1-300x225.jpg" caption="First I cut just a part of the battery bay cover" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/2-1.jpg" thumbnail_image="/assets/img/posts/2019/12/2-1-300x225.jpg" caption="Then I realized I need to cut all of it out; if you look closely you can see the indent I had to make for the Bluetooth knob" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/3-1.jpg" thumbnail_image="/assets/img/posts/2019/12/3-1-300x225.jpg" caption="The indicator LED before it stopped working" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/4-1.jpg" thumbnail_image="/assets/img/posts/2019/12/4-1-300x225.jpg" caption="Bluetooth board and rocker switch mounted..." set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/5-1.jpg" thumbnail_image="/assets/img/posts/2019/12/5-1-300x225.jpg" caption="... and secured" set_name="set_1" %}
</div></div></div> 

## The end

In the end (it doesn’t even matter) I closed it all up; together with 50 caps this will be the perfect cheap Christmas Present.

Two final touches have to be added: 2 stickers that came with the radio, one indicating the production date, and one showing the factory number.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-39" data-gallery_id="871"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-39" data-gallery_no="39"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/radio_live.jpg" thumbnail_image="/assets/img/posts/2019/12/radio_live-300x225.jpg" caption="Listening to a live internet Fallout radio on a '70s radio" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/bottom_open.jpg" thumbnail_image="/assets/img/posts/2019/12/bottom_open-225x300.jpg" caption="Opening the battery bay reveals the Bluetooth module and transformer PCBs" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/bottom_close.jpg" thumbnail_image="/assets/img/posts/2019/12/bottom_close.jpg" caption="The back turned out ok; the unfilled hole is for the activity LED; it will be covered up by the factory number sticker" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/radio2.jpg" thumbnail_image="/assets/img/posts/2019/12/radio2-300x225.jpg" caption="I also glued on the original production date sticker" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/radio.jpg" thumbnail_image="/assets/img/posts/2019/12/radio-300x225.jpg" caption="And I use the production number sticker to cover up the hole for the indicator LED" set_name="set_1" %}
</div></div></div> 

## Appendix

This is the radio’s manual, I found it online. I’ll be posting it here for backup’s sake.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-40" data-gallery_id="876"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-40" data-gallery_no="40"> 
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/01-2.jpg" thumbnail_image="/assets/img/posts/2019/12/01-2-207x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/02.jpg" thumbnail_image="/assets/img/posts/2019/12/02-207x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/03.jpg" thumbnail_image="/assets/img/posts/2019/12/03-207x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/04.jpg" thumbnail_image="/assets/img/posts/2019/12/04-208x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/05.jpg" thumbnail_image="/assets/img/posts/2019/12/05-207x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/06.jpg" thumbnail_image="/assets/img/posts/2019/12/06-207x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/07.jpg" thumbnail_image="/assets/img/posts/2019/12/07-207x300.jpg" caption="" set_name="set_1" %}
  
  

{% include lightbox2_image.html original_image="/assets/img/posts/2019/12/08.jpg" thumbnail_image="/assets/img/posts/2019/12/08-207x300.jpg" caption="" set_name="set_1" %}
</div></div></div> 

List of long wave radio stations in Europe: <a href="https://www.asiawaves.net/longwave-radio.htm" target="_blank" rel="noreferrer noopener" aria-label=" (opens in a new tab)">https://www.asiawaves.net/longwave-radio.htm</a>

List of medium wave radio stations in Europe: <a href="https://en.wikipedia.org/wiki/List_of_European_medium_wave_transmitters" target="_blank" rel="noreferrer noopener" aria-label=" (opens in a new tab)">https://en.wikipedia.org/wiki/List_of_European_medium_wave_transmitters</a>

## Ideas for version 2.0

  * Nixie tube clock
  * Stereo speakers
  * Stereo VU meters
  * Working Bluetooth indicator LED
