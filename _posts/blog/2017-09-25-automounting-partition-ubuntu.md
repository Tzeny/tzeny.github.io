---
id: 214
title: Automounting a partition in Ubuntu
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=214
thumbnail: 2017/09/partition_3-1-360x210.jpg
categories:
  - software
tags:
  - automount
  - fstab
  - partition
  - ubuntu
---
Do you have a second partition you want to automount a boot? Then this is the place for you. I’ll be using the same VM as in other tutorials.

Software used:

  * [VirtualBox 5.1.28](https://www.virtualbox.org/wiki/Downloads)
  * [Ubuntu 17.04](https://www.ubuntu.com/download)

## 1. Creating a mount point

What is a mount point? A typically empty directory, accessible on the current filesystem where an additional filesystem is mounted.

Just open a terminal (Ctrl + Alt + T) and type:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">mkdir</span> <span class="sy0">&</span>lt;name<span class="sy0">&</span>gt;
  </div>
</div>

Remember the name, we will use it later. This creates a directory in your home folder.

## 2. Identifying the partition

Next, type:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> <span class="kw2">fdisk</span> <span class="re5">-l</span>
  </div>
</div>

And identify the partition you want to mount.

<a href="https://tzeny.com/wp-content/uploads/2017/09/partition\_7.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl_caption="" title="">

{% include figure_caption.html url="/assets/img/posts/2017/09/partition_7-300x180.jpg" description="" %}/a>

In my case the partition is /dev/sdb1.

## 3. Writing a fstab entry

What is fstab?

The configuration file /etc/fstab contains the necessary information to automate the process of mounting partitions. In a nutshell, mounting is the process where a raw (physical) partition is prepared for access and assigned a location on the file system tree (or mount point). More info: https://help.ubuntu.com/community/Fstab

First I highly recommend creating a backup:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">cp</span> <span class="sy0">/</span>etc<span class="sy0">/</span>fstab fstab.bk
  </div>
</div>

This creates the backup file fstab.bk in your current directory.

Now, open it up for editing:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">sudo</span> <span class="kw2">nano</span> <span class="sy0">/</span>etc<span class="sy0">/</span>fstab
  </div>
</div>

 

The line I added for my drive:

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="text codecolorer">
    /dev/sdb /home/tzeny/DriveMount ext4 defaults 0 2
  </div>
</div>

Tells fstab to:

  * Try to mount a partition located at /dev/sdb
  * Mount it to /home/tzeny/DriveMount (I created DriveMount in my home directory; if you do the same change this to /home/<your username>/DriveMount)
  * Partition filesystem type is ext4 (Modify this if you have another filesystem)
  * Use default options
  * The first 0 is for dump backup utility, leave it to 0
  * The 2 means check this partition for defects every reboot (a highly recommended option)

<div class="rl-gallery-container" id="rl-gallery-container-13" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-13" data-gallery_no="13"> 



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_1-1.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_1-1-300x179.jpg" caption="This is the original file, just move the cursor to the bottom" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_2-2.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_2-2-300x149.jpg" caption="And append a line telling fstab to mount our drive" set_name="set_1" %}</div> </div>

Now reboot, and type:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
    <span class="kw2">mount</span>
  </div>
</div>

This should show you all of the mounted devices, including the one you just added.

<a href="https://tzeny.com/wp-content/uploads/2017/09/partition\_3-1.jpg" data-rel="lightbox-image-1" data-rl\_title="" data-rl_caption="" title="">

{% include figure_caption.html url="/assets/img/posts/2017/09/partition_3-1-300x179.jpg" description="" %}/a>

And as you can see our drive is mounted.
