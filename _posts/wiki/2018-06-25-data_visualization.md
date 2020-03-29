---
title: Data Visualization
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

Structured data
---------------

{% include figure_caption.html url="/assets/img/wiki/Plots.png" description="Different kinds of plots; the bottom row uses a different dataset than the other rows" %} Visualizing data can help us get insights into it. Depending on the type of data you want to visualize, you may do so in different ways:

-   For 1D data, like a temperature measurement or the number of hits on a webpage we use <b>line plots</b>
-   For 2D data, like the weight and height of a person we use <b>scatter plots</b>
-   To see the distribution of your data you can use <b>histograms</b>
-   To see how much of our data falls into a certain category we can use <b>cumulative plots</b> or <b>pie plots</b>
-   To see the spread of our data we can use <b>box plots</b>
-   To see the estimated kernel(probability) density of our variables we can use <b>kernel density estimation plots</b>
-   To represent the relationship between 2 numerical variables we can use a <b>Hexbin plot</b>

Unstructured data
-----------------

Examples: images, sound, text

{% include figure_caption.html url="/assets/img/wiki/Sound-plot.png" description="border|400px" %}

On the left we have a spectogram of the sound, created using a Fast Fourier Transform.

Image data visualization with Matplotlib
----------------------------------------

``` python
plt.figure(figsize=(16, 16))

from random import randint

rnd = randint(0, len(X_orig)-16)

j = 0
for i in range(rnd, rnd+16):
    img = np.array(X_orig.iloc[i])
    img = img.reshape(28,28)

    plt.subplot(4, 4, j+1)
    j=j+1
    s = 'L: ' +str(y_orig.iloc[i])
    plt.gca().set_title(s)
    plt.imshow(img)

plt.tight_layout()
```
