---
id: 464
title: Building my homelab – part 4
base: Blog
base_url: /blog
author: Tzeny
layout: post
guid: http://192.168.0.110:8000/?p=464
thumbnail: 2019/01/IMG_20181231_213214-360x210.jpg
categories:
  - engineering
tags:
  - docker
  - server
  - xfce
---
I changed my networking setup and switched from Proxmox to Ubuntu, moving most of my services to containers.

**Part 3:** [**Building my homelab – part 3**](https://tzeny.com/2017/11/30/building-my-homelab-part-3/)<figure class="wp-block-image">

![My helpful screenshot](/assets/img/posts/2019/01/IMG_20181231_213214-768x1024.jpg) </figure> 

## Networking

Parts used:

  * [N3150M-E Asus motherboard](https://www.asus.com/Motherboards/N3150ME/) with an integrated [Intel Celeron N3150](https://ark.intel.com/products/87258/Intel-Celeron-Processor-N3150-2M-Cache-up-to-2-08-GHz-) 
  * 4GB of DDR3 RAM
  * Old computer case and power supply
  * 2 x Gigabit PCI 1x network cards
  * 5 port Gigabit ethernet switch

I wanted to try using a [pfSense](https://www.pfsense.org/) machine as my router / firewall, and use my existing wireless router as an access point. So I bought a cheap Asus motherboard with an integrated Intel CPU supporting AES NI (a requirement for newer versions of pfSense) and built a system around it.

The CPU is a low power quad core, which I figured would be more than enough for my needs.

After installing and configuring pfSense I had some issues with it after a couple of weeks: I could no longer access the web interface and I had rare, random internet failures. 

Although it was interesting playing around with it, I reverted back to my wireless router, as it offers all the functionality that I need. In the future I plan on trying pfSense again, but with a different hardware configuration.<figure class="wp-block-image">

![My helpful screenshot](/assets/img/posts/2018/12/IMG_20181231_213356-1024x768.jpg) <figcaption>Here you can see Farcaster, the pfSense machine and a black gigabit ethernet switch</figcaption></figure> 

The other addition to the Homelab is a 5 port ethernet gigabit switch. It connects all the computers (only Tesla and my laptop) to the network, and is really useful when transferring files between my laptop and Tesla. 

Although I have a 300 mb/s symmetric internet connection, with my current router (a [TL-WR740N](https://www.tp-link.com/au/products/details/TL-WR740N.html)) all I can get is 100 mb/s. That is part of the next upgrade.

## Tesla

Parts used:

  * Old 120GB SSD

Software used:

  * [Ubuntu 18.04 LTS](https://www.ubuntu.com/download/desktop)
  * [Docker](https://www.docker.com/)
      * [Nginx Reverse Proxy](https://github.com/jwilder/nginx-proxy)
      * [Let’s Encrypt Nginx Proxy Companion](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion)
      * [Media Wiki](https://hub.docker.com/_/mediawiki/) 
      * [MariaDB](https://hub.docker.com/_/mariadb/)
      * [Samba Server](https://hub.docker.com/r/sixeyed/samba/)
      * [OpenVPN](https://github.com/kylemanna/docker-openvpn)
  * [obfsproxy](https://blog.torproject.org/obfsproxy-next-step-censorship-arms-race)
  * [TightVNC](https://www.tightvnc.com/)

I added an old 120 Gb SSD to Tesla, which now acts as the OS drive, speeding everything up.

I installed Ubuntu 18.04 Desktop edition as I had planned to use Gnome together with [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/), but when I used it like that the maximum resolution was that of the attached display; I ended up using [TightVNC](https://www.tightvnc.com/) and [Xfce](https://www.xfce.org/) instead, as shown in [Digital Ocean’s tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-18-04).<figure class="wp-block-image">

![My helpful screenshot](/assets/img/posts/2018/12/homelab.png) <figcaption>Sketch of my current network architecture</figcaption></figure> 

### MediaWiki

I started looking into ML some time ago, and I decided to use a wiki in order to take notes. You can access it here if you want: [https://tzeny.ddns.net/](https://tzeny.ddns.net/index.php/Main_Page)

MediaWiki is “a free and open source software wiki package written in PHP, originally for use on Wikipedia. It is now also used by several other projects of the non-profit Wikimedia Foundation and by many other wikis, including this website, the home of MediaWiki.  
Use the links below to explore the site contents. You’ll find some content translated into other languages, but the primary documentation language is English.”

I decided to use it since it is simple, yet powerful and also open source. 

The wiki itself consists of 2 parts: the PHP server, and the SQL database. They are hosted in separate containers, and linked together using a Docker network.

The next step is adding SSL support. An easy way to do this is to follow  
[this guide](https://cloud.google.com/community/tutorials/nginx-reverse-proxy-docker) from Google. It details how to use Nginx as a reverse proxy with [Let’s Encrypt](https://letsencrypt.org/) certificates that are auto renewed every month.

### Samba

I have a basic Samba server running which gives me easy access to the files on the RAID 1 array (which I use as a NAS).

### VPN

For the VPN I used a [Docker container](https://github.com/kylemanna/docker-openvpn) which supports both UDP and TCP and [obfsproxy](https://blog.torproject.org/obfsproxy-next-step-censorship-arms-race), which obfuscates the traffic so that Deep Packet Inspection cannot figure out which protocol is used and thus can not selectively block it.

Generally I connect directly to the UDP container, but when that doesn’t work I use obfsproxy + OpenVPN TCP.

This is a good tutorial explaining how to use obfsproxy and Open VPN: [How to hide OpenVPN traffic using Obfsproxy on a Windows PC and Linux EC2 server](https://www.comparitech.com/blog/vpn-privacy/hide-openvpn-traffic-obfsproxy-on-windows-and-linux-ec2/).

### TightVNC

I use a TightVNC server to be able to launch long running visual processes. Here is a great guide on how to install it and Xfce in Ubunut: [Digital Ocean guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-18-04).



## Main changes

  * Tried pfSense, returned to router
  * Gigabit ethernet switch
  * Dockerized most servicies
  * Switched to Ubuntu 18.04
  * Added 120GB system drive to Tesla
  * Got a new low power quad core Celeron server that is currently unused
