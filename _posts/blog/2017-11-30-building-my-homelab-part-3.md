---
id: 236
title: 'Building my homelab – part 3'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=236
thumbnail: 2017/11/Front-360x210.jpg
categories:
  - engineering
tags:
  - cables
  - homelab
  - hydra
  - networking
  - proxmox
  - server
  - storage
  - tesla
  - vm
---
Finally all my networking hardware, servers and UPS are in the same place. I also did some cable management, but since I’m trying to do this in an old cabinet it is quite difficult to make is both accessible and beautiful.

**Part 2: [Building my Homelab – part 2](https://tzeny.com/2017/09/17/building-my-homelab-part-2/)**

Parts used:

  * Wire ties <https://www.aliexpress.com/item/50PCS-CL-1-White-and-Black-Sticky-Adjustable-Wire-Ties-Cable-Clips-Clamp-Plastic-Self-Adhesive/32761449948.html>
  * Ethernet wires
  * Power wires
  * Routers and switces (will write a more detailed post)
  * Server (right now only Tesla is fully configured, will write a post about it soon enough)

The main change is the addition of Tesla, a server powered by an Intel i5-2400S (for power efficiency), with 8 GB of RAM, 1 TB of Raid 1 (ZFS) storage space and 600 GB of WD Black used for a Proxmox install and maybe VM scratch space. An article about it will soon follow.

<div class="rl-gallery-container" id="rl-gallery-container-17" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-17" data-gallery_no="17"> 



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/Front.jpg" thumbnail_image="/assets/img/posts/2017/11/Front-225x300.jpg" caption="This is how it looks now, the LEDs are off because I need to buy a new power wire" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/front-open.jpg" thumbnail_image="/assets/img/posts/2017/11/front-open-225x300.jpg" caption="This is a view with the doors open; top shelf: raspberry pi and LED psu, then networking shelf, then server shelf and UPS area" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/IMG_20171126_174841.jpg" thumbnail_image="/assets/img/posts/2017/11/IMG_20171126_174841-225x300.jpg" caption="My plan for how the homelab should be structured; I made it by using SketchUp to create an accurate schematic of the furniture and then print it out" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/tesla.jpg" thumbnail_image="/assets/img/posts/2017/11/tesla-300x225.jpg" caption="Tesla, my new powerhouse; it's powered by an Intel i5 2400s, as 8 GB of RAM; storage: 1TB ZFS Raid 1, 600 GB WD Black; 2 x GIgabyte Lan" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/old-hidra.jpg" thumbnail_image="/assets/img/posts/2017/11/old-hidra-300x225.jpg" caption="Old Hydra sever, leaving it offline now so that it won't uselessly drain power" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/cable-management.jpg" thumbnail_image="/assets/img/posts/2017/11/cable-management-300x225.jpg" caption="The cable ties I got from AliExpress, cheap and did the job nicely" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/11/WebGUI.jpg" thumbnail_image="/assets/img/posts/2017/11/WebGUI-300x164.jpg" caption="This is the Proxmox GUI of Tesla; not too much happening yet" set_name="set_1" %}</div> </div>

## Main changes:

  * Cable management
  * Took Hydra offline
  * Built Tesla to take its place
  * LEDs offline for now
  * Tidying up
