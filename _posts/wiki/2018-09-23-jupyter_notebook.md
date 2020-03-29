---
title: Jupyter Notebook
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

It is easily installed in python by running:

``` bash
python3 -m pip install jupyter
```

<h2>
Kernels

</h2>
A guide for installing your own kernals can be found here: [Installing Jupyter notebook with a virtualenv kernel](/Installing_Jupyter_notebook_with_a_virtualenv_kernel "wikilink")

<h2>
Extensions

</h2>
To control Jupyter extensions, the best thing to do is to install the [nbextensions_configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator):

``` bash
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```
