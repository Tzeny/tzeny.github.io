---
id: 247
title: 'Building a proxmox server – Tesla'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=247
thumbnail: 2017/12/IMG_20171118_172650-360x210.jpg
categories:
  - engineering
tags:
  - container
  - docker
  - lxc
  - openvpn
  - proxmox
  - raid
  - samba
  - second hand
  - share
  - vm
  - zfs
---
Sometime ago I decided it would be better to build a moderately powerful VM server instead of having many cheap PCs. This way it would take up a lot less space and consume less power. I build mine using second hand hardware, and named it Tesla.

Parts used:

  * [Intel i5-2400S](https://ark.intel.com/products/52208/Intel-Core-i5-2400S-Processor-6M-Cache-up-to-3_30-GHz) processor (4 x 2.50 GHz); I chose this because it uses less power than a normal processor (this has a [TDP](https://en.wikipedia.org/wiki/Thermal_design_power) of 65W compared to 95W of an i5-2400)
  * [Intel DQ77MK](https://ark.intel.com/products/59044/Intel-Desktop-Board-DQ77MK) motherboard
  * 8 GB DDR3 non-ECC RAM (2 x KVR1333D3N9/4G)
  * [Deepcool GAMMAXX 200T](http://deepcool.com/product/cpucooler/2015-09/7_4054.shtml) cooler
  * 2 x 1 TB 2.5” HDD
  * 1 x 600 GB HDD (WD Black)
  * Old PSU and case I had lying around

Software used:

  * [Proxmox](https://www.proxmox.com/en/)

## Objective

Let’s start by defining our objective. We want to build a server capable of running a couple of Virtual Machines at the same time. The server should be up 24/7. It should have redundant storage, as I plan to create a samba share that I want to use as a backup location. I also wanted to use this server as a VPN (the [one running on the Raspberry PI](https://tzeny.com/2017/08/03/making-your-own-vpn/) still runs, but only as a backup as this has more throughput).

The server should be cheap. For everything I bought I paid 178 € (I already had the PSU, case and 1 x 1 TB HDD + 1 x 600 GB HDD). Proxmox is open source.

## Hardware

### 1. Unboxing

I ordered everything during the week and it arrived, one package at a time during the next couple of days.

<div class="rl-gallery-container" id="rl-gallery-container-18" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-18" data-gallery_no="18"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_165053.jpg" title="Some of the boxes are mislabeled, as everything except the cooler is second part" data-rl_title="Some of the boxes are mislabeled, as everything except the cooler is second part" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-18">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_165053-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Some of the boxes are mislabeled, as everything except the cooler is second part</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_165432.jpg" title="CPU and motherboard" data-rl_title="CPU and motherboard" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-18">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_165432-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">CPU and motherboard</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_165439.jpg" title="Close up of the CPU" data-rl_title="Close up of the CPU" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-18">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_165439-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Close up of the CPU</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_171003.jpg" title="I choose this cooler because it has a big fan(120mm), meaning it will be quieter than others" data-rl_title="I choose this cooler because it has a big fan(120mm), meaning it will be quieter than others" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-18">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_171003-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">I choose this cooler because it has a big fan(120mm), meaning it will be quieter than others</span></span></a>
</div></div> </div>

### 2. Putting it all together

<div class="rl-gallery-container" id="rl-gallery-container-19" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-19" data-gallery_no="19"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_171600.jpg" title="First step is mounting the CPU; I used the motherboard box as a stand; then I mounted the heatsink" data-rl_title="First step is mounting the CPU; I used the motherboard box as a stand; then I mounted the heatsink" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_171600-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">First step is mounting the CPU; I used the motherboard box as a stand; then I mounted the heatsink</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_171746.jpg" title="Next I attached the fan" data-rl_title="Next I attached the fan" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_171746-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Next I attached the fan</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_171830.jpg" title="Inserted the RAM" data-rl_title="Inserted the RAM" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_171830-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Inserted the RAM</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_172650.jpg" title="I connected it like this to be able to easily debug problems" data-rl_title="I connected it like this to be able to easily debug problems" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_172650-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">I connected it like this to be able to easily debug problems</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_173238.jpg" title="This is the original BIOS of the motherbaord" data-rl_title="This is the original BIOS of the motherbaord" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_173238-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is the original BIOS of the motherbaord</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/23798289_1369997706443867_591928934_o.jpg" title="And this is the BIOS after the update" data-rl_title="And this is the BIOS after the update" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/23798289_1369997706443867_591928934_o-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">And this is the BIOS after the update</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171118_174754.jpg" title="The end result" data-rl_title="The end result" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-19">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171118_174754-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The end result</span></span></a>
</div></div> </div>

## Software

### 1. Proxmox

After everything was running nicely, I flashed Proxmox onto an USB drive, connected the server (Tesla) to my LAN and installed Proxmox. I had a small hitch with the networking but after I solved that I was greeted by the web interface.

<figure id="attachment_244" aria-describedby="caption-attachment-244" style="width: 300px" class="wp-caption alignnone"><a href="https://tzeny.com/wp-content/uploads/2017/11/WebGUI.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/11/WebGUI-300x164.jpg)</a><figcaption id="caption-attachment-244" class="wp-caption-text">This is the Proxmox GUI of Tesla; not too much happening yet</figcaption></figure>

### 2. ZFS Raid

ZFS is a software RAID utility. To set it up with Proxmox I followed [this tutorial](https://forum.level1techs.com/t/how-to-create-a-nas-using-zfs-and-proxmox-with-pictures/117375).

### 3. Samba share

After setting up ZFS I created a directory which I then [shared using a Samba server](https://tzeny.com/2017/09/15/building-a-cheap-nas/).

### 4. VPN

I followed [this tutorial](https://www.servethehome.com/creating-the-ultimate-virtualization-and-container-setup-with-management-guis/) to install Docker and Portainer.

Then I used the OpenVPN docker container [here](https://github.com/kylemanna/docker-openvpn).

## End result

I have a server which idles at around 50W (my UPS can keep this and my networking equipment running for about 45 min), and packs a bit of a punch. Right now I’m also running an Ubuntu VM and a VPN docker container.

<div class="rl-gallery-container" id="rl-gallery-container-20" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-20" data-gallery_no="20"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_135509.jpg" title="All the components inside of the case" data-rl_title="All the components inside of the case" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-20">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_135509-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">All the components inside of the case</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/12/IMG_20171203_135536.jpg" title="The 2 1TB drives in the upper part, and the 600 GB WD Black in the lower part" data-rl_title="The 2 1TB drives in the upper part, and the 600 GB WD Black in the lower part" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-20">![My helpful screenshot](/assets/img/posts/2017/12/IMG_20171203_135536-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The 2 1TB drives in the upper part, and the 600 GB WD Black in the lower part</span></span></a>
</div></div> </div>
