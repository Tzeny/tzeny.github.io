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

-   [Miscellaneous](/Miscellaneous "wikilink")
    -   [Averages](/Averages "wikilink")

<!-- -->

-   [Calculus](/Calculus "wikilink")
    -   [Derivatives](/Calculus#Derivatives "wikilink")

<!-- -->

-   [Linear Algebra](/Linear_Algebra "wikilink")
    -   [Vectors](/Linear_Algebra#Vectors "wikilink")
        -   [Linear Combinations of Vectors](/Linear_Algebra#Linear_combination_of_vectors "wikilink")
        -   [Basis](/Linear_Algebra#Basis "wikilink")
            -   [Changing basis](/Linear_Algebra#Changing_bases "wikilink")
        -   [Eigenvectors](/Linear_Algebra#Eigenvectors "wikilink")
            -   [Eigenbasis](/Linear_Algebra#Eigenbasis "wikilink")
    -   [Linear Transformations](/Linear_Algebra#Linear_transformations "wikilink")
        -   [Matrix Multiplication as Composition](/Linear_Algebra#Matrix_multiplications_as_compositions "wikilink")
        -   [Space Orientation](/Linear_Algebra#Space_orientation "wikilink")
        -   [Column Space](/Linear_Algebra#Column_space "wikilink")
        -   [Rank](/Linear_Algebra#Rank "wikilink")
        -   [Null Space / Kernel](/Linear_Algebra#Null_space.2FKernel "wikilink")
        -   [Determinants](/Linear_Algebra#Determinants "wikilink")
        -   [Inverse](/Linear_Algebra#Inverse "wikilink")
        -   [Non Square Matrices](/Linear_Algebra#Non_Square_Matrices "wikilink")
        -   [Cross Product](/Linear_Algebra#Cross_product "wikilink")
            -   [2D Space](/Linear_Algebra#2D_space "wikilink")
            -   [3D Space](/Linear_Algebra#3D_space "wikilink")
        -   [Dot Product](/Linear_Algebra#Dot_product "wikilink")
        -   [Duality](/Linear_Algebra#Duality "wikilink")
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

Exponentially weighted moving average [thumb|Exponentially weighted moving average](/File:Ewma.png "wikilink") *S*<sub>*t*</sub> = *Y*<sub>1</sub> for *t* = 1

*S*<sub>*t*</sub> = *α* \* *Y*<sub>*t*</sub> + (1 − *α*)\**S*<sub>*t* − 1</sub> for *t* > 1
