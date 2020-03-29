---
title: Installing Keras on ArchLinux
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

Guide based on [Keras documentation](https://keras.io/).

Installing additional PIP packages
----------------------------------

Switch into our tensorflow virtualenv, and install the following packages:

HDF5 and h5py (required if you plan on saving Keras models to disk). graphviz and pydot (used by visualization utilities to plot model graphs).

``` bash
sudo pacman -S graphviz
```

``` bash
pip install pydot h5py
```

Install Keras
-------------

Afterwards, just run

``` bash
pip install keras
```

And then try to

``` bash
import keras
```

If it works it should output a line saying 'Using TensorFlow backend'.
