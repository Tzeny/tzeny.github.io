---
id: 303
title: 'Clock Vision – face recognition clocking system'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=303
thumbnail: 2018/05/32267096_1532091176901185_2366736973932003328_n-360x210.jpg
categories:
  - engineering
tags:
  - computer vision
  - diy
  - raspberry
---
So, this is not a tutorial, but a showcase of a project I recently build for [HackTM 2018](https://hacktm.ro/) together with a few colleagues from college. The project consists of 3 main components: a raspberry PI with a webcam (and optional display), that will be placed next to an automated door, which will run a face detection algorithm; a webserver running a Flask API and a face recognition algorithm based on OpenCV and finally and administrative [progressive web app](https://developers.google.com/web/progressive-web-apps/) (what they are is apps that are installed seamlessly when you visit a webpage, and which can then provide offline access to data) for managers to see when their employees are at work.

 

# Overall architecture

<a href="https://tzeny.com/wp-content/uploads/2018/05/ClockVision.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">![My helpful screenshot](/assets/img/posts/2018/05/ClockVision-300x218.jpg)</a>

We have 2 actors in our architecture.

  * the employee, whose face is scanned whenever he enters or exits the building. If he is recognized, the door opens, his arrival/departure time is registered and he is free to continue.
  * the manager, who has access to a progressive web app hosted on the server, in which he can view the comings and goings of his employees and also check their current status (at work / not at work)

# Raspberry PI face detector and door controller

<div class="rl-gallery-container" id="rl-gallery-container-22" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-22" data-gallery_no="22"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2018/05/32267096_1532091176901185_2366736973932003328_n.jpg" title="Raspberry PI face detecion, with a 7inch LCD display and a HP webcamera" data-rl_title="Raspberry PI face detecion, with a 7inch LCD display and a HP webcamera" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-22">![My helpful screenshot](/assets/img/posts/2018/05/32267096_1532091176901185_2366736973932003328_n-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Raspberry PI face detecion, with a 7inch LCD display and a HP webcamera</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2018/05/32440491_1532091233567846_8649323595882823680_n.jpg" title="The Raspberry Pi in it's housing behind the LCD" data-rl_title="The Raspberry Pi in it's housing behind the LCD" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-22">![My helpful screenshot](/assets/img/posts/2018/05/32440491_1532091233567846_8649323595882823680_n-225x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">The Raspberry Pi in it's housing behind the LCD</span></span></a>
</div></div> </div>

The Raspberry PI is running the latest distribution of Raspbian (Raspbian Stretch), and is connected to a local wireless network. OpenCV and Numpy packages are installed, and a basic face detection algorithm is running on it. It checks to see only one face is in the image, and also asks the user to hold still so that a clear picture may be taken. After a picture is taken, it is sent to the webserver, who attempts to recognize the person in the picture. Depending on the response, a message is displayed on screen and a gate/door is opened (not yet implemented).

# Progressive web app

<div class="rl-gallery-container" id="rl-gallery-container-23" data-gallery_id="0"> <div class="rl-gallery rl-basicgrid-gallery " id="rl-gallery-23" data-gallery_no="23"> 

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2018/05/testpng.jpg" title="Web app for managers" data-rl_title="Web app for managers" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-23">![My helpful screenshot](/assets/img/posts/2018/05/testpng-300x164.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Web app for managers</span></span></a>
</div>

<div class="rl-gallery-item">
  <a href="https://tzeny.com/wp-content/uploads/2018/05/32490985_1637341603047570_1148425021740285952_n.jpg" title="Mobile app for managers" data-rl_title="Mobile app for managers" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-23">![My helpful screenshot](/assets/img/posts/2018/05/32490985_1637341603047570_1148425021740285952_n-169x300.jpg)<span class="rl-gallery-caption"><span class="rl-gallery-item-title">Mobile app for managers</span></span></a>
</div></div> </div>

This is a screenshot of our application running on a mobile phone. Since it was built with [Polymer](https://www.polymer-project.org/3.0/toolbox/) it is basically a cross-platform application capable of running on any web browser or phone. It is pretty rudimentary right now, showing user’s current status (in/out of the office) and their working hours so far.

# Server

In this case the server was running on a laptop. It was hosting 2 different components:

  * a [Flask Rest API](https://flask-restful.readthedocs.io/en/latest/), which received requests from the Raspberry PI, containing images, ran a face recognition algorithm on them, and send the response back to the Raspberry PI (face detected: yes/no, face name), while also saving them to the database to be later used by the administrative application; it also had routes used by the administrative application to get it’s data
  * a [Polymer Server](https://www.polymer-project.org/3.0/docs/about_30) serving a progressive web app

# 

# Sources

All sources for this project are available at: <https://github.com/ArinToaca/ClockVision>
