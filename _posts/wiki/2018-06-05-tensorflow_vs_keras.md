---
title: Tensorflow vs Keras
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

Tensorflow
----------

TensorFlow™ is an open source software library for high performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices. Originally developed by researchers and engineers from the Google Brain team within Google’s AI organization, it comes with strong support for machine learning and deep learning and the flexible numerical computation core is used across many other scientific domains.

Keras
-----

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

Comparison
----------

For comparison I will use data from some posts written by more informed people than myself[1][2]

Keras is geared towards ease of use, while maintaining the ability to create complex models.

Tensorflow, although harder to learn provides much more control over your model, has a debugger and many more options.

But as we all know that Keras is going to be integrated in TF, it is wiser to build your network using tf.contrib.Keras and insert anything you want in the network using pure TensorFlow [3]. In short,

`tf.contrib.Keras + tf = All you ever gonna need`

Also, apparently Keras is already integrated into Tensorflow[4]

<references />

[1] <https://medium.com/implodinggradients/tensorflow-or-keras-which-one-should-i-learn-5dd7fa3f9ca0>

[2] <https://www.quora.com/What-is-the-difference-between-keras-and-tensorflow>

[3]

[4] <http://www.fast.ai/2017/01/03/keras/>
