---
title: Cifar10 Classifier
layout: wiki_post
base: Wiki
base_url: /wiki
categories:
  - wikiprojects
hidden: true
---



This is my attempt at classifying images in the cifar10 dataset. It's based around 3[inception modules]({% post_url /wiki/2018-06-21-types_of_neural_networks%}).

Accuracy
--------

| Architecture                                              | Accuracy on test set                     |
|-----------------------------------------------------------|------------------------------------------|
| c2, c2, mp, c2,c2,mp,f,d,d                                | xx                                       |
| c2, ap, c2, ap, c2, ap, f, d, d, do                       | 64.28 %, 60.22 %                         |
| data-normalized, c2, ap, c2, ap, c2, ap, f, d, d, do      | 65.83 %                                  |
| data-normalized-gray, c2, ap, c2, ap, c2, ap, f, d, d, do | 62.91 %                                  |
| inception-module                                          | 62.82 % (stopped becuase of overfitting) |
| inception dense drop                                      | 62.89 %                                  |
| inception inception drop                                  | 74.18 %                                  |
| inceptionx3 dense drop                                    | 77.61 %                           |
| nceptionx3 dense drop dense drop dense                    | 77.25 %                                  |

Git
---

[<https://github.com/Tzeny/udemy-zero-to-deep-learning/blob/master/course/Cifar10.ipynb>](https://github.com/Tzeny/udemy-zero-to-deep-learning/blob/master/course/Cifar10.ipynb)
