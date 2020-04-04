---
id: 513
title: '3D part: Shifted LCD Bracket'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=513
thumbnail: 2019/01/IMG_20190101_120545-360x210.jpg
categories:
  - 3ddesign
tags:
  - bracket
  - lcd
  - sketchup
  - stl
  - thingverse
---
This is the first 3D part I designed and printed myself. Well, designed is an overstatement. This part is a remix of the [Tevo Tarantula LCD bracket](https://www.thingiverse.com/thing:1622728).

**Thingverse:** [Tevo Tarantula Shifted LCD bracket](https://www.thingiverse.com/thing:3326501)

## Part

The problem with the original is that, if you have the dual Z motors upgrade the space between the motor supports will be too narrow to fit 2 of the LCD Brackets.

My solution was this: 
<script src="https://embed.github.com/view/3d/Tzeny/tzeny.github.io/master/assets/img/posts/2019/01/LCD_Bracket_Shifted.stl"></script>

A bracket that has the base shifted by 20 mm. This is how my LCD looks with a shifted bracket (left) and a normal one (right):<figure class="wp-block-image"><a href="https://tzeny.com/wp-content/uploads/2019/01/IMG\_20190101\_120545.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">

![My helpful screenshot](/assets/img/posts/2019/01/IMG_20190101_120545-1024x768.jpg) </a></figure> 

## Design

Software used:

  * [SketchUp](https://www.sketchup.com/)
      * Extension [Solid Inspector²](https://extensions.sketchup.com/en/content/solid-inspector%C2%B2)
      * Extension [SketchUp STL](https://extensions.sketchup.com/en/content/sketchup-stl)

After loading the original file in SketchUp and moving the base 20 mm up, I added the triangular support strut.

I grouped everything together, and used Solid Inspector to check and fix any issues.

Then I used the export STL option, selecting the file type **ASCII** and the unit **millimeters**. (it is very important to set the millimeters as export unit, otherwise when you try to slice the part you will find it is either very small or very large).
