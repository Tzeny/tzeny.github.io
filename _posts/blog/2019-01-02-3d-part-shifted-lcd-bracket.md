---
id: 513
title: '3D part: Shifted LCD Bracket'
base: Blog
base_url: /blog
author: Tzeny
layout: post
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

<link rel="stylesheet" type="text/css" href="http://tzeny.com/wp-content/plugins/canvasio3d-light/inc/css/style.css" />
</link>

<div class="canvasio3D" style='background-color:#afafaf;color:#000000;border:0px solid;border-color:#f6f6f6;max-width:600px;max-height:400px;width:100%;height:100%;overflow: hidden;-moz-box-shadow: 0 0 0px #888; -webkit-box-shadow: 0 0 0px#888; box-shadow: 0 0 0px #888;padding:0px;'>
  <div id="3D_0" data-parameter="{'loadingtext':'Loading ...','vector':'off','mousewheel':'on','backimg':'','reflection':'','refval':'0','floor':'off','floorheight':'42','objpath':'https:\/\/tzeny.com\/wp-content\/uploads\/2019\/01\/LCD_Bracket_Shifted.stl','texturpath':'','envtexturpath':'','objcol':'','objcolor':'0x0000ff','objscale':'1','objshadow':'off','width':'600','height':'400','dropshadow':'0','zoom':'50','textcol':'#000000','border':'0','bordercol':'#f6f6f6','backcol':'#afafaf','text':'','rollspeedx':'0','rollspeedy':'0','rollspeedh':'0','rollspeedv':'0','rollmode':'','mouse':'on','lightset':'1','lightrotate':'off','shine':'0','ambient':'0xaaa','fps':'','wincount':'0','_uploadUrl':'https:\/\/tzeny.com\/wp-content\/uploads','_picUrl':'http:\/\/tzeny.com\/wp-content\/plugins','lang':'en_US','help':'off','winCount':0}" style="width:600px;height:400px;">
  </div>
  
  <div id="caHandDiv_0" class="caHandDiv">
    <div class="caHpIcon" id="caHpIcon_0" style="top:0;left:0">
    </div>
  </div>
</div>

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
