---
id: 910
title: 'VanLife – Power and lights v0.1'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: https://tzeny.com/?p=910
thumbnail: 2019/12/Sketch.jpg
categories:
  - engineering
  - hardware
tags:
  - 12V
  - 220V
  - 5V
  - ac
  - dc
  - LED
  - lights
  - power
---
After living without AC power, with only handheld LED lamps and my phone light for 2.5 months in Rusty, I decided enough is enough and installed some lights and a 300W inverter.

The inverter is temporary, as in the end I’ll need a much beefier inverter (~2000W continuous should suffice). And I’d like to find a better way of attaching the lights instead of hot glue, as I don’t really like its opaqueness when it hardens. 

Future additions: more fuses, battery level indicator.

Parts list:

  * 300W (600W peaks) DC to AC inverter – 25 USD
  * Warm light copper wire 22m LED strip – 12 USD
  * Schuko outlets – 0 USD
  * 12V – 5V conversion board – 0 USD
  * small electrical switch – 0 USD
  * misc electrical components and wires – 0 USD

## Overall setup

What I wanted was a module that would take 12V DC power on one side, and provide 220V AC outlets, and 5V DC power output for the ceiling LEDs. Both the outlets and the LEDs should have power switches and obvious on/off indicators.

These being said, here is my current setup:<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/12/Sketch-1024x877.jpg) </figure> 

I was lucky that Rusty already has a 2 battery system, which means that I can drain the consumer battery and then easily start the car to recharge it.<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/12/whole_thing-1024x768.jpg) <figcaption>Testing the whole thing, without the fan on the inverter; spotlight powered by inverter, LED strip powered by 5V converter; notice the red LED indicating that 5V power is switched on; the inverter has a power LED + the fan’s LEDs</figcaption></figure> 

I used hot glue to secure the LED strip to Rusty’s roof. This is the result:<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/12/rusty_light-1024x768.jpg) <figcaption>The single LED strip, laid out; next to the window on the left is the mounted power plank, with both the 5V converter board (red LED) and inverter (blue fan) turned on</figcaption></figure> 

The inverter was really useful, as I could power my 10W hot glue gun, without needing an extension cord and shore power.

## Building it

I decided to place all the components on a 1500mm x 200mm(?) x 20mm board. That way it would be easy to screw in components later on.

### Power delivery board

This is a small PCB designed to take it 12V power via screw terminals and split it to wires leading to the inverter and the 5V converter.

The 3 connectors on the bottom side are there to help me connect additional 12V devices / modules easily (like the <a href="https://tzeny.com/2019/11/21/vanlife-heating-with-the-propex-hs2000/" target="_blank" rel="noreferrer noopener" aria-label="Propex heater (opens in a new tab)">Propex heater</a>).

**Tip**: always color code your negative / positive terminals.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-42" data-gallery_id="918"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-42" data-gallery_no="42"> 
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/12/PowerDistribution1.jpg" title="Finished power distribution board" data-rl_title="Finished power distribution board" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-42">![My helpful screenshot](/assets/img/posts/2019/12/PowerDistribution1-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Finished power distribution board</span></span></a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/12/PowerDistribution2.jpg" title="Note: I added solder above the terminal used to make the 2 long parallel connections" data-rl_title="Note: I added solder above the terminal used to make the 2 long parallel connections" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-42">![My helpful screenshot](/assets/img/posts/2019/12/PowerDistribution2-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Note: I added solder above the terminal used to make the 2 long parallel connections</span></span></a>
  </div>
</div></div></div> 

**Note: always reinforce high amp rails with solder**

### 12V DC – 220V AC 300W inverter

I modded my inverter by replacing its small, noisy fan with a 120mm PC Fan. Learn how to do it here: <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://tzeny.com/2019/12/23/silencing-a-noisy-car-inverter/" target="_blank">https://tzeny.com/2019/12/23/silencing-a-noisy-car-inverter/</a>.<figure class="wp-block-image size-medium">

![My helpful screenshot](/assets/img/posts/2019/12/body9-300x225.jpg) <figcaption>Bonus: LED light on</figcaption></figure> 

I fixed it on the board using 3D printed L brackets: <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://www.thingiverse.com/thing:2226" target="_blank">https://www.thingiverse.com/thing:2226</a>. I cut its supplied wires and fixed them into some screw on terminals on a small PCB used for power delivery.

Fortunately, this inverter comes with an inbuilt power switch on the output side.

**Note: this inverter has a build in 40A fuse; you should add one in line if you haven’t already**

### 12V – 5V 3A converter

This converter is based around this kind of conversion board: <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://www.openimpulse.com/blog/products-page/product-category/mp1584en-mini-dc-dc-step-module/" target="_blank">https://www.openimpulse.com/blog/products-page/product-category/mp1584en-mini-dc-dc-step-module/</a>.

<div class="wp-block-responsive-lightbox-gallery">
  <div class="rl-gallery-container rl-loading" id="rl-gallery-container-43" data-gallery_id="921"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-43" data-gallery_no="43"> 
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/12/5vconverter1.jpg" title="Board layout without switch and indicator LED" data-rl_title="Board layout without switch and indicator LED" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-43">![My helpful screenshot](/assets/img/posts/2019/12/5vconverter1-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Board layout without switch and indicator LED</span></span></a>
  </div>
  
  <div class="rl-gallery-item">
    <a href="https://tzeny.com/wp-content/uploads/2019/12/5vconverter2.jpg" title="Switch added between 12V in and the converter board; LED soldered in series with a 220 Ohm resistor to output" data-rl_title="Switch added between 12V in and the converter board; LED soldered in series with a 220 Ohm resistor to output" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-43">![My helpful screenshot](/assets/img/posts/2019/12/5vconverter2-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Switch added between 12V in and the converter board; LED soldered in series with a 220 Ohm resistor to output</span></span></a>
  </div>
</div></div></div> 

The switch turns off the power delivery to the inputs of the board; it was mounted to the top of the wooden plank for easy access. 

**Tip:** This board should also have a small fuse but I didn’t have one on hand.

### Schuko outlet

This is just a basic 3 output schuko outlet that I took apart in order to screw its bottom half to the board with 2 wood screws; I kept the wire at the original 3M length and coiled it underneath the inverter, securing it with zipties.<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/12/outlet-1024x768.jpg) </figure> 

## Mounting it

I used 2 long wood screws to mount it inside Rusty, where it now powers my ceiling light strips.<figure class="wp-block-image size-large">

![My helpful screenshot](/assets/img/posts/2019/12/mount.jpg) </figure>
