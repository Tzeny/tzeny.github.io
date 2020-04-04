---
id: 557
title: 'DeepStellar – a StarCraft2 Reinforcement Learning agent part 0.1'
base: Blog
base_url: /blog
author: Tzeny
layout: blog_post
guid: http://192.168.0.110:8000/?p=557
inline_featured_image:
  - "0"
post_grid_post_settings:
  - 'a:14:{s:9:"post_skin";s:4:"flat";s:19:"custom_thumb_source";s:89:"https://tzeny.com/wp-content/plugins/post-grid/assets/frontend/css/images/placeholder.png";s:16:"thumb_custom_url";s:0:"";s:17:"font_awesome_icon";s:0:"";s:23:"font_awesome_icon_color";s:0:"";s:22:"font_awesome_icon_size";s:0:"";s:17:"custom_youtube_id";s:0:"";s:15:"custom_vimeo_id";s:0:"";s:21:"custom_dailymotion_id";s:0:"";s:14:"custom_mp3_url";s:0:"";s:20:"custom_soundcloud_id";s:0:"";s:16:"custom_video_MP4";s:0:"";s:16:"custom_video_OGV";s:0:"";s:17:"custom_video_WEBM";s:0:"";}'
thumbnail: 2019/04/DeepStellar_v0-360x210.jpg
categories:
  - artificialintelligence
---
Last week me and a couple of friends had an idea: let’s use PySC2 (a Python wrapper for the StarCraft 2 API) to build a reinforcement learning agent that can teach itself how to play StarCraft 2. 

This is no easy task, and many people have attempted it: 

  * <https://paperswithcode.com/task/starcraft>
  * <https://paperswithcode.com/task/starcraft-ii>

But we thought it would be an interesting way to get into the world of Reinforcement Learning.

Our agent is an A2C network, that, if trained, right now, converges to outputting only 0s.

Below is our first version of the AI, taking random actions. The map is called CollectMineralShards; the aim is to move your marines (the two green circles) to as many Mineral Shards (blue circles) as possible in the allotted time.

<div style="width:640px;height:480px;position:relative;padding-bottom:75.000%;">
</div>

## Getting it to run

If you want to try out our project yourselves, head over to <https://github.com/deepmind/pysc2> and follow their instructions to get the StarCraft2 environment.

For our algorithm we used PyTorch, so make sure you have that installed and running.

After you install PyTorch, head over to github, clone our repository, and run it according to the instructions: <https://github.com/Tzeny/deepstellar>

## PySC2 – StarCraft II Learning Environment

PySC2 is DeepMind’s Python component of the StarCraft II Learning Environment (SC2LE). It exposes Blizzard Entertainment’s StarCraft II Machine Learning API as a Python RL Environment. 

It can run one or two agents / game, and many games in parallel. 

Agent get an observation of the game state after each N in game time steps. N can be set, in our case we used N = 16 for an equivalent APM of 90. 

Below is the code for an agent that takes a random action at each time step.

<div class="codecolorer-container python default" style="overflow:auto;white-space:nowrap;width:435px;">
  <div class="python codecolorer">
    <span class="kw1">class</span> RandomAgent<span class="br0">(</span>base_agent.<span class="me1">BaseAgent</span><span class="br0">)</span>:<br />   <span class="st0">"""A random agent for starcraft."""</span><br /> <br />   <span class="kw1">def</span> step<span class="br0">(</span><span class="kw2">self</span><span class="sy0">,</span> obs<span class="br0">)</span>:<br />     <span class="kw2">super</span><span class="br0">(</span>RandomAgent<span class="sy0">,</span> <span class="kw2">self</span><span class="br0">)</span>.<span class="me1">step</span><span class="br0">(</span>obs<span class="br0">)</span><br />     function_id <span class="sy0">=</span> numpy.<span class="kw3">random</span>.<span class="me1">choice</span><span class="br0">(</span>obs.<span class="me1">observation</span>.<span class="me1">available_actions</span><span class="br0">)</span><br />     args <span class="sy0">=</span> <span class="br0">[</span><span class="br0">[</span>numpy.<span class="kw3">random</span>.<span class="me1">randint</span><span class="br0">(</span><span class="nu0"></span><span class="sy0">,</span> size<span class="br0">)</span> <span class="kw1">for</span> size <span class="kw1">in</span> arg.<span class="me1">sizes</span><span class="br0">]</span><br />             <span class="kw1">for</span> arg <span class="kw1">in</span> <span class="kw2">self</span>.<span class="me1">action_spec</span>.<span class="me1">functions</span><span class="br0">[</span>function_id<span class="br0">]</span>.<span class="me1">args</span><span class="br0">]</span><br />     <span class="kw1">return</span> actions.<span class="me1">FunctionCall</span><span class="br0">(</span>function_id<span class="sy0">,</span> args<span class="br0">)</span>
  </div>
</div>

The obs object contains valueable information about the game state:

  * Screen (you can select any combination of the 2 items below)
      * Features (shown in Figure 1. above)
      * RGB pixels
  * Minimap (you can select any combination of the 2 items below)
      * Features (shown in Figure 1. above)
      * RGB pixels
  * Player information
  * Control groups
  * Single select
  * Multi select
  * Cargo
  * Build queue
  * Alers
  * Available actions
  * Last actions (only for successful actions)
  * Action result

## Reinforcement Learning – A2C

Our agent has to look at the observations for the current step, choose an action that would best further its goals, and predict a value for the current state.

A state’s value = the sum of all the rewards if you were to start in that state and move forward

Intuitive explanation of A2C: <https://hackernoon.com/intuitive-rl-intro-to-advantage-actor-critic-a2c-4ff545978752>

All A2C architectures have 2 heads: 

  * Actor – responsible for choosing an action, in our case the actor outputs both an action\_id distribution, and 4 continuous values used as arguments for some of the actions (for example the 331/Move\_screen command requires a point (x,y) on the screen as argument)
  * Critic – responsible for deciding how good the actor’s actions are

There are some inputs that have variable sizes, so we are not feeding them to the network just yet.<figure class="wp-block-image">

![My helpful screenshot](/assets/img/posts/2019/04/Architecture-2.svg) <figcaption>Figure 2. Architecture of our 2 head neural network</figcaption></figure> 

The idea is to run the model for a number of time steps (10 in our case), and then train both the actor and critic. 

I will explain the loss function in the next post, as I don’t have a good understanding of it yet.
