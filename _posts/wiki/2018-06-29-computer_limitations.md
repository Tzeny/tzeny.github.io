---
title: Computer Limitations
layout: wiki_post
base: Wiki
base_url: /wiki
categories:
  - wikimisc
hidden: true
---

Mathematics in real life is continuous, not so on a computer. Article based on FastAI Computational Linear Algebra course1.

Course page
-----------

Source: [<https://tzeny.ddns.net:4430/Tzeny/fastai_numerical-linear-algebra/blob/master/nbs/1.%20Why%20are%20we%20here.ipynb>](https://tzeny.ddns.net:4430/Tzeny/fastai_numerical-linear-algebra/blob/master/nbs/1.%20Why%20are%20we%20here.ipynb)

Floats
------

{% include figure_caption.html url="/assets/img/wiki/Float_scale_gap.png" description="800px,Gaps between floating point numbers depending on the interval in which the numbers reside" %} Floating point numbers have a maximum and a minimum: 1.79 \* 10308and as small as 2.23 \* 10−308.

There are uneven gaps between numbers.

### Machine epsilon

The error between 1 and the next larger number: *ϵ**m**a**c**h**i**n**e* = 2−53 ≈ 1.11 \* 10−16 (as defined by IEEE)

I will stop maintaing course notes for this course as the Jupyter Notebooks are more than adequate.

1. [https://www.youtube.com/watch?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY&v=8iGzBMboA0I](https://www.youtube.com/watch?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY&v=8iGzBMboA0I)
