---
title: Tensorboard
layout: wiki_post
base: Wiki
base_url: /wiki
categories:
  - wikitools
hidden: true
category:
  - wikitools
---

[Category:Tools](/Category:Tools "wikilink")

Tensorboard is a tool for visualizing the output from the training of a model with Keras (view example on how to generate log file on the[Examples]({% post_url /wiki/2018-06-25-examples%}) page) or Tensorflow.

` tensorboard --logdir ./logs/`

If you use if like this, you need to place the event files for different training runs in subdirectories of the logs directory.

{% include figure_caption.html url="/assets/img/wiki/Tensorboard.png" description="border,600px" %}
