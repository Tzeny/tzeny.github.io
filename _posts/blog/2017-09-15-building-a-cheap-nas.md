---
id: 145
title: Building a cheap NAS
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=145
thumbnail: 2017/09/IMG_20170914_221530-360x210.jpg
categories:
  - engineering
tags:
  - attached
  - diy
  - hdd
  - network
  - server
  - storage
  - ubuntu
---
Do you have an old computer laying around? Do you want to have easy access to all of your files and folders?

If the answer to these questions is yes, then follow me and let’s build a cheap NAS (Network Attached Storage) together!

This is the end result:

<div class="rl-gallery-container" id="rl-gallery-container-5" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-5" data-gallery_no="5"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/IMG_20170914_221530.jpg" title="The computer housing the NAS" data-rl_title="The computer housing the NAS" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-5">![My helpful screenshot](/assets/img/posts/2017/09/IMG_20170914_221530-300x225.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The computer housing the NAS</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hidra_network.jpg" title="This is how Windows sees our NAS, as a Network Share location" data-rl_title="This is how Windows sees our NAS, as a Network Share location" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-5">![My helpful screenshot](/assets/img/posts/2017/09/hidra_network-300x172.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is how Windows sees our NAS, as a Network Share location</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hidra_phone.jpg" title="This is how our Phone sees our NAS" data-rl_title="This is how our Phone sees our NAS" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-5">![My helpful screenshot](/assets/img/posts/2017/09/hidra_phone-169x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is how our Phone sees our NAS</span></span></a>
</div></div> </div>

Our goal here is to create a Network storage location, accessible for anyone on the network, no matter what device they are using. I tested mine with Windows and Android, but it should work with Linux as well.

Note: Using VPN you can access your NAS remotely and securely. <a href="https://tzeny.com/2017/08/03/making-your-own-vpn/" target="_blank" rel="noopener">Click here</a> to learn how to create your own 35$ VPN server.

## What is a NAS?

Network-attached storage (NAS) is a file-level computer data storage server connected to a computer network providing data access to a heterogeneous group of clients. NAS is specialized for serving files either by its hardware, software, or configuration. It is often manufactured as a computer appliance – a purpose-built specialized computer. NAS systems are networked appliances which contain one or more storage drives, often arranged into logical, redundant storage containers or RAID.Network-attached storage removes the responsibility of file serving from other servers on the network. They typically provide access to files using network file sharing protocols such as NFS, SMB/CIFS, or AFP.

 

Parts used:

  * Old Dell computer (any old PC should work, but having SATA ports and RAID support are big bonuses; I used a Dell Optiplex G520)
  * 1 TB HDD (the capacity depends on what your storage needs are)

Software used:

  * [Ubuntu Server](https://www.ubuntu.com/download/server)
  * Windows Explorer
  * [ES File Explorer](https://play.google.com/store/apps/details?id=com.estrongs.android.pop&hl=en)

 

## Hardware

There’s not much to it. Just make sure your computer is powered on and is connected to the network.

In my case I also did a slight modification of the design. Because I had a HDD laying about, I decided I want to add it to the NAS. But, this was a problem since there was no room in the case for an extra drive. So, after a bit of tinkering I managed to fix it inside the CD Rom bay. Note that this is a 2.5” drive.

<figure id="attachment_147" aria-describedby="caption-attachment-147" style="width: 300px" class="wp-caption alignnone"><a href="https://tzeny.com/wp-content/uploads/2017/09/IMG\_20170914\_221559.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2017/09/IMG_20170914_221559-300x225.jpg)</a><figcaption id="caption-attachment-147" class="wp-caption-text">A 1 TB drive mounted inside the CD Rom bay</figcaption></figure>

## Software

### 1. OS

First of all, just install Ubuntu Server the normal way. I used the server version because it is lighter on resources.

[Here](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-server) you can find a great guide if you’re not sure how to proceed. I recommend setting a secure password, as this will be a network connected device.

You should also assign a static IP to your server now, and note it down.

### 2. Extra drive (optional)

If you have added a new drive in the system you need to:

  * [Partition and format it](https://tzeny.com/2017/09/25/formatting-and-partitioning-a-drive-under-ubuntu/)
  * [Automatically mount it](https://tzeny.com/2017/09/25/automounting-partition-ubuntu/)

You should also create a directory which will become the network share now. In my case I used /data.

Since only an admin can create files and folders under the root of the system (/). To achieve this use:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> <span class="kw2">mkdir</span> <span class="sy0">/</span>data<br /> <br /> <span class="kw2">sudo</span> <span class="kw2">chown</span> <span class="br0">[</span>username<span class="br0">]</span> <span class="sy0">/</span>data
  </div>
</div>

### 3. Installing and configuring samba

In order to create network shares, we will use an utility called samba. You can install it using the following commands.

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> <span class="kw2">apt-get update</span><br /> <span class="kw2">sudo</span> <span class="kw2">apt-get install</span> samba
  </div>
</div>

Next, we have to set a password for our samba user (this is a different password from you login one)

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> smbpasswd <span class="re5">-a</span> <span class="br0">[</span>username<span class="br0">]</span>
  </div>
</div>

Good. Now, we have to tell samba which folders should be available to the network.

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> <span class="kw2">cp</span> <span class="sy0">/</span>etc<span class="sy0">/</span>samba<span class="sy0">/</span>smb.conf ~ <span class="co0">#create a backup of the config file</span><br /> <br /> <span class="kw2">sudo</span> <span class="kw2">nano</span> <span class="sy0">/</span>etc<span class="sy0">/</span>samba<span class="sy0">/</span>smb.conf
  </div>
</div>

Now, you should add these lines to the bottom of the file:

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="text codecolorer">
    [somename]<br /> path = /home/username/foldername<br /> valid users = username<br /> read only = no
  </div>
</div>

Note: mind the spaces before and after the equal signs. Replace foldername and username with your own data

So, in the case of my /data folder, I need to write this to the config file:

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="text codecolorer">
    [Share]<br /> path = /data<br /> valid users = [my_user]<br /> read only = no
  </div>
</div>

Now, we need to restart the samba service, and check that everything is all right:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> service smbd restart<br /> <br /> testparm
  </div>
</div>

## Accessing your share

### 1. Windows

Open the File Explorer and go to the network tab. There you should see your machine, and other devices connected to your network. If it asks you whether you want to discover other devices on the network accept.

<div class="rl-gallery-container" id="rl-gallery-container-6" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-6" data-gallery_no="6"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hidra_network_2.jpg" title="Your computer should appear on your network now" data-rl_title="Your computer should appear on your network now" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-6">![My helpful screenshot](/assets/img/posts/2017/09/hidra_network_2-300x144.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Your computer should appear on your network now</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hidra_network_3.jpg" title="Login with your username and Samba password" data-rl_title="Login with your username and Samba password" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-6">![My helpful screenshot](/assets/img/posts/2017/09/hidra_network_3-300x236.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Login with your username and Samba password</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/hidra_network.jpg" title="This is how Windows sees our NAS, as a Network Share location" data-rl_title="This is how Windows sees our NAS, as a Network Share location" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-6">![My helpful screenshot](/assets/img/posts/2017/09/hidra_network-300x172.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">This is how Windows sees our NAS, as a Network Share location</span></span></a>
</div></div> </div>

### 2. Android

Download and install the free app [ES File Explorer](https://play.google.com/store/apps/details?id=com.estrongs.android.pop&hl=en). In the left menu, go to Network -> Lan. Click the big plus on the lower right side of the screen. And add your server’s details (IP, username and password; you can also set a display name here if you wish). After you click done, it should appear as an icon on your screen. Just tap it and you’re in!

Note: you should be on the same network as the server for this to work

<div class="rl-gallery-container" id="rl-gallery-container-7" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-7" data-gallery_no="7"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/nas_android_1.jpg" title="First press the big blue + in the bottom right" data-rl_title="First press the big blue + in the bottom right" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-7">![My helpful screenshot](/assets/img/posts/2017/09/nas_android_1-169x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">First press the big blue + in the bottom right</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/nas_android_2.jpg" title="Now fill in your server information; use the password you set for Samba" data-rl_title="Now fill in your server information; use the password you set for Samba" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-7">![My helpful screenshot](/assets/img/posts/2017/09/nas_android_2-169x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Now fill in your server information; use the password you set for Samba</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/nas_android_3.jpg" title="Now your server should appear" data-rl_title="Now your server should appear" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-7">![My helpful screenshot](/assets/img/posts/2017/09/nas_android_3-169x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Now your server should appear</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2017/09/nas_android_4.jpg" title="And if you click on it you will see your files and folders" data-rl_title="And if you click on it you will see your files and folders" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-7">![My helpful screenshot](/assets/img/posts/2017/09/nas_android_4-169x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">And if you click on it you will see your files and folders</span></span></a>
</div></div> </div>

## Ideas for the future

  1. Set up either RAID or a backup system
  2. Keep the computer turned off when not needed and use Wake on Lan to turn it on (tutorial coming)
  3. Use a VPN to securely acess your NAS from anywhere ([VPN tutorial](https://tzeny.com/2017/08/03/making-your-own-vpn/))
