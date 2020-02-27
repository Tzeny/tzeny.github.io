---
id: 225
title: VirtualBox connect to VM via SSH / Portforwarding in VirtualBox
date: 2017-11-17T09:52:36+00:00
author: Tzeny
layout: post
guid: http://192.168.0.110:8000/?p=225
permalink: /2017/11/17/virtualbox-portforward-ssh/
thumbnail: 2017/11/final-360x210.jpg
categories:
  - engineering
tags:
  - linux
  - portforward
  - portforwarding
  - ports
  - putty
  - server
  - ssh
  - virtualbox
---
Ever wanted to connect to a VirtualBox VM via SSH, SCP or others and found out you couldn’t? This is because, by default you don’t have access to the ports of your VM. Today I’ll show you how you can enable port forwarding so you can easily connect to all your VMs.

Software used:

  * [VirtualBox](https://www.virtualbox.org)
  * [PuTTY](http://www.putty.org/)

## 

## 1. Find your guest VMs IP

Fire up your virtual machine, login and find you ipaddress. In most Linux distributions you can do this by using the command 

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">ifconfig</span>
  </div>
</div>

or 

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">ip</span> a
  </div>
</div>

. Note down this ip, we will use it in the next step.

<div class="rl-gallery-container" id="rl-gallery-container-14" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-14" data-gallery_no="14"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/11/ip-1.jpg" title="This is the output of ifconfig, look for the lines not belonging to lo (loopback)" data-rl_title="This is the output of ifconfig, look for the lines not belonging to lo (loopback)" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-14">![My helpful screenshot](/assets/img/posts/2017/11/ip-1-300x252.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is the output of ifconfig, look for the lines not belonging to lo (loopback)</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/11/ip-2.jpg" title="This is the output of ip a, look for the lines not belonging to lo (loopback adapter)" data-rl_title="This is the output of ip a, look for the lines not belonging to lo (loopback adapter)" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-14">![My helpful screenshot](/assets/img/posts/2017/11/ip-2-300x252.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is the output of ip a, look for the lines not belonging to lo (loopback adapter)</span></span></a>
</div></div> </div>

## 

## 2. Enable portforwarding

In VirtualBox, select your VM and click Settings. Go to Network -> Adapter 1 -> under Advanced -> Port Forwarding. Click the add button, and a new rule will appear. Edit its IP to be 127.0.1.1 (a loopback address you can easily remember), for the host port use 22 (SSH, I’ll add a list of commonly used ports at the bottom of this article), and for the guest port 22. For the guest ip use the one you got above.

<div class="rl-gallery-container" id="rl-gallery-container-15" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-15" data-gallery_no="15"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/11/port-forward.jpg" title="Open the Settings menu, then the Networking one, then the Portforwarding One" data-rl_title="Open the Settings menu, then the Networking one, then the Portforwarding One" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-15">![My helpful screenshot](/assets/img/posts/2017/11/port-forward-300x226.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Open the Settings menu, then the Networking one, then the Portforwarding One</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/11/port-forward-2.jpg" title="Next add a new rule, with the ports set as shown; replace Guest IP with your own" data-rl_title="Next add a new rule, with the ports set as shown; replace Guest IP with your own" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-15">![My helpful screenshot](/assets/img/posts/2017/11/port-forward-2-300x160.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Next add a new rule, with the ports set as shown; replace Guest IP with your own</span></span></a>
</div></div> </div>

## 

## 3. Connect with PuTTY to the VM

Open up PuTTY and connect to 127.0.1.1:22. Login and voila, you should now be connected to the VM. You can use this procedure for any other port.

<div class="rl-gallery-container" id="rl-gallery-container-16" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-16" data-gallery_no="16"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/11/putty.jpg" title="Fill in 127.0.1.1 as the IP" data-rl_title="Fill in 127.0.1.1 as the IP" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-16">![My helpful screenshot](/assets/img/posts/2017/11/putty-300x290.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Fill in 127.0.1.1 as the IP</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/11/final.jpg" title="Login and you are now connected to your VM" data-rl_title="Login and you are now connected to your VM" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-16">![My helpful screenshot](/assets/img/posts/2017/11/final-300x160.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Login and you are now connected to your VM</span></span></a>
</div></div> </div>

 

## 

## Appendix – list of common ports

  * 21 – FTP (File Transfer Protocol, used to copy files between remote computers)
  * 22 – SSH, SCP (Secure Shell, open a terminal on the remote computer; Secure Copy, secure file transfer)
  * 80 – HTTP (HyperTextTransferProtocol, used by most sites today)
  * 443 – HTTPS (HTTP over TLS/SSL, used to securely transfer data between a site and a client)
  * 3306 – MySQL (MySQL database port)

 
