---
title: Mathematics
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

External Resources
------------------

Articles:

-   [The top 10 algorithms](https://www.cs.fsu.edu/~lacher/courses/COT4401/notes/cise_v2_i1/guest.pdf)
    -   A quick overview of some of the most important algorithms out there
-   [Fast Randomized SVD](https://research.fb.com/fast-randomized-svd/)

Papers:

-   [The Augmented Lagrange Multiplier Method for Exact Recovery of Corrupted Low-Rank Matrices](https://arxiv.org/pdf/1009.5055.pdf)
-   [Robust Principal Component Analysis?](https://arxiv.org/pdf/0912.3599.pdf)

Courses:

-   [Essence of linear algebra by 3Blue1Brown](https://www.youtube.com/watch?v=kjBOesZCoqc&t=0s&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=2)
-   [Computational Linear Algebra](http://www.fast.ai/2017/07/17/num-lin-alg/)

Internal Resources
------------------

-  [Miscellaneous]({% post_url /wiki/2018-07-03-interesting_miscellaneous%})
    -  [Averages]({% post_url /wiki/2019-02-28-averages%})



-  [Calculus]({% post_url /wiki/2019-01-10-calculus%})
    -  [Derivatives]({% post_url /wiki/2019-01-10-calculus%})



-  [Linear Algebra]({% post_url /wiki/2018-07-03-linear_algebra%})
    -  [Vectors]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Linear Combinations of Vectors]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Basis]({% post_url /wiki/2018-07-03-linear_algebra%})
            -  [Changing basis]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Eigenvectors]({% post_url /wiki/2018-07-03-linear_algebra%})
            -  [Eigenbasis]({% post_url /wiki/2018-07-03-linear_algebra%})
    -  [Linear Transformations]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Matrix Multiplication as Composition]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Space Orientation]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Column Space]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Rank]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Null Space / Kernel]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Determinants]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Inverse]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Non Square Matrices]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Cross Product]({% post_url /wiki/2018-07-03-linear_algebra%})
            -  [2D Space]({% post_url /wiki/2018-07-03-linear_algebra%})
            -  [3D Space]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Dot Product]({% post_url /wiki/2018-07-03-linear_algebra%})
        -  [Duality]({% post_url /wiki/2018-07-03-linear_algebra%})
-   Computational Linear Algebra
    -   Introduction of the course; presentation of the problems we are trying to solve - [Course 1: Why are we here?](https://github.com/fastai/numerical-linear-algebra/blob/master/nbs/1.%20Why%20are%20we%20here.ipynb)
    -   The problem of trying to assign a topic to a post; different approaches; how to speed them up - [Course 2: Topic modelling with SVD and NMF](https://github.com/fastai/numerical-linear-algebra/blob/master/nbs/2.%20Topic%20Modeling%20with%20NMF%20and%20SVD.ipynb)
    -   SVD and NMF in depth; calculating smaller SVD (maintains high accuracy while speeding up compute significantly - [Course 3: Topic modelling with SVD and NMF](https://github.com/fastai/numerical-linear-algebra/blob/master/nbs/2.%20Topic%20Modeling%20with%20NMF%20and%20SVD.ipynb)
    -   PCA, decomposing matrices into sparse matrices and low rank matrices to help with tasks such as background removal - [Course 4: Background Removal with Robust PCA](https://github.com/fastai/numerical-linear-algebra/blob/master/nbs/3.%20Background%20Removal%20with%20Robust%20PCA.ipynb)

Minimizing a function multiplied by a constant
----------------------------------------------

Let's say we have an optimization problem.

$\\underset{u}{min}(u-5)^2+1 => u=5$

If we multiply it all by some constant, the result does not change.

$\\underset{u}{min} 10\*((u-5)^2+1) => \\underset{u}{min} 10(u-5)^2+10 => u=5$

EWMA
----

Exponentially weighted moving average{% include figure_caption.html url="/assets/img/wiki/Ewma.png" description="Exponentially weighted moving average" %} *S**t* = *Y*1 for *t* = 1

*S**t* = *α* \* *Y**t* + (1 − *α*)\**S**t* − 1 for *t* > 1
