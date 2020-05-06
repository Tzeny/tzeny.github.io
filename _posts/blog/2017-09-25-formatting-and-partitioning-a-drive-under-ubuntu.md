---
id: 195
title: Formatting and partitioning a drive under Ubuntu
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=195
thumbnail: 2017/09/partition_8-360x210.jpg
categories:
  - software
tags:
  - ext4
  - formatting
  - gpt
  - partitioning
---
Today we will take a new drive in Ubuntu, and format and partition it. I will be doing this under a VM, because it is easy to add or delete drives.

Software used:

  * [VirtualBox 5.1.28](https://www.virtualbox.org/wiki/Downloads)
  * [Ubuntu 17.04](https://www.ubuntu.com/download)

## 1. Adding a second drive

I started by adding a second drive to my Ubuntu VM.

<div class="rl-gallery-container" id="rl-gallery-container-11" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-11" data-gallery_no="11"> 



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive_-1.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive_-1-300x163.jpg" caption="Click the settings button" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive-300x198.jpg" caption="Go to the Storage section" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive_2.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive_2-300x198.jpg" caption="Click the add drive button" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive_3.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive_3-283x300.jpg" caption="Leave the default" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive_4.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive_4-283x300.jpg" caption="Leave it to dynamic, so as not the use up all the space unless it is required" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive_5.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive_5-283x300.jpg" caption="Select the size; you can leave the default location" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/add_drive_6.jpg" thumbnail_image="/assets/img/posts/2017/09/add_drive_6-300x198.jpg" caption="If everything worked you should now see the second drive" set_name="set_1" %}</div> </div>

## 2. Format and partitioning

Now that we’ve added the drive, we can boot into Ubuntu.

The following command will list all available drives.

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
     <span class="kw2">sudo</span> <span class="kw2">fdisk</span> <span class="re5">-l</span>
  </div>
</div>

If all went well you should see 2 entries:

<a href="https://tzeny.com/wp-content/uploads/2017/09/partition\_1.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl_caption="" title="">

{% include figure_caption.html url="/assets/img/posts/2017/09/partition_1-300x181.jpg" description="" %}/a>

You should now identify the new drive. In my case it is /dev/sdb

Now, to format the drive:

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="text codecolorer">
     sudo cfdisk /dev/sdb
  </div>
</div>

<div class="rl-gallery-container" id="rl-gallery-container-12" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-12" data-gallery_no="12"> 



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_2-1.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_2-1-300x180.jpg" caption="Choose GPT, as it is a newer scheme" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_3.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_3-300x180.jpg" caption="Select New" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_4.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_4-300x180.jpg" caption="Enter the size of the partition; the default is max; if you want multiple partitions enter a smaller size" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_5.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_5-300x180.jpg" caption="Select Write" set_name="set_1" %}



{% include lightbox2_image.html original_image="/assets/img/posts/2017/09/partition_6.jpg" thumbnail_image="/assets/img/posts/2017/09/partition_6-300x180.jpg" caption="Type yes; afterwards you can quit" set_name="set_1" %}</div> </div>

To check the results of our work again type

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
     <span class="kw2">sudo</span> <span class="kw2">fdisk</span> <span class="re5">-l</span>
  </div>
</div>

<a href="https://tzeny.com/wp-content/uploads/2017/09/partition\_7.jpg" data-rel="lightbox-image-1" data-rl\_title="" data-rl_caption="" title="">

{% include figure_caption.html url="/assets/img/posts/2017/09/partition_7-300x180.jpg" description="" %}/a>

## 3. Creating the filesystem

We will use the ext4 filesystem (the most common Linux filesystem today; if you want to learn more go here: <https://opensource.com/article/17/5/introduction-ext4-filesystem>):

On the new drive (/dev/sdb in my case) you should see a partition (/dev/sdb1 in my case). Now we only need to format it. For this you can use the mkfs utility. To see all possible formatting options type

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
     mkfs
  </div>
</div>

and press tab tab.

In our case we will use:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="bash codecolorer">
     <span class="kw2">sudo</span> mkfs.ext4 <span class="sy0">/</span>dev<span class="sy0">/</span>sdb1
  </div>
</div>

<a href="https://tzeny.com/wp-content/uploads/2017/09/partition\_8.jpg" data-rel="lightbox-image-2" data-rl\_title="" data-rl_caption="" title="">

{% include figure_caption.html url="/assets/img/posts/2017/09/partition_8-300x180.jpg" description="" %}/a>

And we are done 🙂

## 

## Automounting

If you want the new partition to be mounted at boot time, you can follow my tutorial [here](https://tzeny.com/2017/09/25/automounting-partition-ubuntu/).
