---
id: 86
title: Making your own 35$ VPN
date: 2017-08-03T13:42:36+00:00
author: Tzeny
layout: post
guid: http://192.168.0.110:8000/?p=86
permalink: /2017/08/03/making-your-own-vpn/
thumbnail: 2017/08/with-vpn-360x210.jpg
categories:
  - software
tags:
  - own
  - raspberry
  - raspbian
  - vpn
---
Yesterday I decided that I would like to be able to access my home computer that I use as a NAS from anywhere in the world. The easiest and most secure way to do this is by using a VPN. So, what is a VPN? A Virtual Private Network extends a Private Network across a public network (like the internet), enabling users to send and receive data like their devices were connected directly to the Private Network. In my case, this means I can access my windows share without having to open it to the whole internet.

<a href="https://tzeny.com/wp-content/uploads/2017/08/without-vpn.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img class="alignnone wp-image-92 size-medium" src="https://tzeny.com/wp-content/uploads/2017/08/without-vpn-300x160.jpg" alt="" width="300" height="160" srcset="https://tzeny.com/wp-content/uploads/2017/08/without-vpn-300x160.jpg 300w, https://tzeny.com/wp-content/uploads/2017/08/without-vpn-768x410.jpg 768w, https://tzeny.com/wp-content/uploads/2017/08/without-vpn-1024x547.jpg 1024w, https://tzeny.com/wp-content/uploads/2017/08/without-vpn.jpg 1200w" sizes="(min-width: 960px) 75vw, 100vw" /></a> <a href="https://tzeny.com/wp-content/uploads/2017/08/with-vpn.jpg" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/08/with-vpn-300x168.jpg)</a>

The 2 pictures show the difference between a normal connection and a VPN tuneel.

In the first case, the computer connects through the internet to the router. But it cannot access the NAS directly. The router must have a port forwarding rule allowing you to reach the NAS, where a strong authentication mechanism must be present, to deter hackers. This is because the port is always open, and anyone on the internet could access it. If at a later date I add something else I would like to access, I must open another port and so on.

Compare this to the second picture. When you connect to the VPN server running on the Raspberry, you basically become part of the network. This means that you can access the NAS directly. It will become discoverable in you Network directory (if you are using Windows). You still need to create a port forwarding rule for the VPN server, but that’s the only rule you need. Everything else can stay protected behind the router’s firewall.

## VPN advantages

 

## Encryption

All the traffic between you and the server is encrypted after a connection is established. This means that no one can listen in on you, preventing Man In The Middle Attacks. A common example is unsecured or suspicious networks. If you connect to an untrusted network, you can then connect to your VPN and all your traffic will be secured.

## Compression

Open VPN server has the option of compressing traffic, reducing bandwidth use.

## Bypassing web censorship

If you are connected to a network or proxy that blocks certain websites, you can use a VPN to bypass the proxy. Because when you are connected to the VPN, your traffic will be exiting via your home router, you will be able to access any content available from your home.

Parts used:

  * <a href="https://tzeny.com/2017/08/03/installing-raspbian-enabling-ssh/" target="_blank" rel="noopener noreferrer">Raspberry Pi 2 with Raspbian</a>

Software used:

  * [PiVPN](http://www.pivpn.io/)
  * [OpenVPN Client](https://openvpn.net/index.php/open-source/downloads.html)

 

# Setup

 

## Preparing the Raspberry Pi

For this to work, you need to have a Raspberry with Raspbian installed, connected to your network with a static IP address assigned to it. If you don’t already have that, follow my tutorial here:

<a href="https://tzeny.com/2017/08/03/installing-raspbian-enabling-ssh/" target="_blank" rel="noopener noreferrer">Installing Raspbian and enabling SSH</a>

### Changing your password

After you are connected to your Raspberry via SSH, the first step should be to change the default password for user pi. Type the following command to change the password:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">passwd</span>
  </div>
</div>

The current password is ‘raspberry’.

## Installing PiVPN

 

Now we are ready to install the VPN server. We will be using PiVPN. To get things started run the following command:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    curl <span class="re5">-L</span> https:<span class="sy0">//</span>install.pivpn.io <span class="sy0">|</span> <span class="kw2">bash</span>
  </div>
</div>

This will start the install process. The pictures below include the steps which require interaction. I have not included the steps that only require you to click ok.

<div class="rl-gallery-container" id="rl-gallery-container-2" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-2" data-gallery_no="2"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-0.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-0-300x171.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-0-1.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-0-1-300x171.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-0-2.jpg" title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-0-2-300x171.jpg)</a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-1.jpg" title="Network settings. Note the IP on the top, this will be your Raspberry's IP" data-rl_title="Network settings. Note the IP on the top, this will be your Raspberry's IP" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-1-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Network settings. Note the IP on the top, this will be your Raspberry's IP</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-2.jpg" title="Choose the VPN user" data-rl_title="Choose the VPN user" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-2-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Choose the VPN user</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-4.jpg" title="Enable unattended upgrades" data-rl_title="Enable unattended upgrades" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-4-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Enable unattended upgrades</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-6.jpg" title="OpenVPN port; note this down; you can change it if you like" data-rl_title="OpenVPN port; note this down; you can change it if you like" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-6-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">OpenVPN port; note this down; you can change it if you like</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-7.jpg" title="Encryption level; default one is ok" data-rl_title="Encryption level; default one is ok" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-7-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Encryption level; default one is ok</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-8.jpg" title="Generating keys, this will take a long time" data-rl_title="Generating keys, this will take a long time" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-8-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Generating keys, this will take a long time</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-9.jpg" title="You can leave this as is; or if you will later use DNS you can select the 2nd one" data-rl_title="You can leave this as is; or if you will later use DNS you can select the 2nd one" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-9-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">You can leave this as is; or if you will later use DNS you can select the 2nd one</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/08/screen-10.jpg" title="Choose DNS provider; default is ok" data-rl_title="Choose DNS provider; default is ok" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-2">![My helpful screenshot](/assets/img/posts/2017/08/screen-10-300x171.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Choose DNS provider; default is ok</span></span></a>
</div></div> </div>

And you’re done. Now you need to run the following command:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    pivpn add
  </div>
</div>

You will be prompted to pick a name and a password for the new user. Pick a secure password.

<a href="https://tzeny.com/wp-content/uploads/2017/08/add-user.jpg" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/08/add-user-300x171.jpg)</a>

Use WinSCP (or similar) to copy the file <user>.ovpn from /home/pi/ovpns to your desktop.

## Install and configure OpenVPN client

Install OpenVPN client from here: <https://openvpn.net/index.php/open-source/downloads.html>

And a little icon should appear in your taskbar. Right click on it and select Import… and choose the <user>.ovpn file.

<a href="https://tzeny.com/wp-content/uploads/2017/08/import.jpg" data-rel="lightbox-image-3" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/08/import.jpg)</a>

The final step is port forwarding the port that you set up for the VPN server. You can follow any one of the tutorials here: <https://portforward.com/>  
Just use your Raspberry’s IP and your port.

Now when you click connect you should have a secure VPN connection. This works from anywhere in the world. And when you are connected you can access the computers in your network like you were connected too.

If you do not have a static IP you need to configure a DNS server. A tutorial is coming soon.
