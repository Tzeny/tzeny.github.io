---
title: Jupyter Notebook
layout: wiki_post
base: Wiki
base_url: /wiki
categories:
  - wikimisc
hidden: true
---

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

It is easily installed in python by running:

``` bash
python3 -m pip install jupyter
```


Kernels


A guide for installing your own kernals can be found here:[Installing Jupyter notebook with a virtualenv kernel]({% post_url /wiki/2018-06-13-installing_jupyter_notebook_with_a_virtualenv_kernel%})


Extensions


To control Jupyter extensions, the best thing to do is to install the [nbextensions_configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator):

``` bash
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```
