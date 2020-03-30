---
title: Artificial Intelligence
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

To keep things easy this page will act as an index for all AI related resources.

External Resources
------------------

-   [Machine Learning Tutorials](https://machinelearningmastery.com)
-   [Machine Learning Getting Started Ideas](https://machinelearningmastery.com/start-here/#getstarted)
-   [Machine Learning Resources](https://medium.com/machine-learning-in-practice/my-curated-list-of-ai-and-machine-learning-resources-from-around-the-web-9a97823b8524)
-   [Top 100 Data Science Resources](https://www.mastersindatascience.com/top-100-data-science-resources/)
-   [Learn Math Fast](https://github.com/llSourcell/learn_math_fast)

News:

-   [Inside AI](https://inside.com/ai)

Contests:

-   [Kaggle Competitions](https://www.kaggle.com/competitions)

### Articles


-   [Deep Learning Performance with AutoAugment](https://ai.googleblog.com/2018/06/improving-deep-learning-performance.html?m=1%7CImproving)
    -   Augmenting computer vision datasets by generating new images based on existing data in the set
-   [Deep Reinforcement Learning Doesn't Work Yet](https://www.alexirpan.com/2018/02/14/rl-hard.html) - February 14th, 2018
    -   Examples of why RL is hard to put into practice, the state of the industry, DeepRL
-   [The Evolution and Core Concepts of Deep Learning & Neural Networks](https://www.analyticsvidhya.com/blog/2016/08/evolution-core-concepts-deep-learning-neural-networks/) - August 2016
    -   Good primer on NN
-   [AI at Google: our principles](https://blog.google/topics/ai/ai-principles/amp/)
    -   Google's principles for AI development
-   [Understanding the backward pass through Batch Normalization Layer](https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html)
    -   Good explanation of how the derivative of the Batch Normalization layer is computed
-   [A Beginner’s Guide to Recurrent Networks and LSTMs](https://deeplearning4j.org/lstm.html)
    -   Good explanation of LSTMs and GRUs, plus an intuition of backpropagation through time
-   [Optimization techniques comparison in Julia: SGD, Momentum, Adagrad, Adadelta, Adam](https://int8.io/comparison-of-optimization-techniques-stochastic-gradient-descent-momentum-adagrad-and-adadelta/)
    -   Short explanations and performance comparison for SGD, SGD with momentum, AdaGrad, AdaDelta and Adam optimizers
-   [googlenet in keras](https://joelouismarino.github.io/blog_posts/blog_googlenet_keras.html)
    -   An implementation of GoogLeNet in Keras
-   [Learning Rate Schedules and Adaptive Learning Rate Methods for Deep Learning](https://towardsdatascience.com/learning-rate-schedules-and-adaptive-learning-rate-methods-for-deep-learning-2c8f433990d1)
    -   Compares different methods of adjusting the learning rate of a NN dynamically
-   [Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
    -   Data augmentation in Keras; use VGG16 as a base for our image classifier
-   [Profiling Top Kagglers: Martin Henze (AKA Heads or Tails), World's First Kernels Grandmaster](http://blog.kaggle.com/2018/06/19/tales-from-my-first-year-inside-the-head-of-a-recent-kaggle-addict/)
    -   The journey to becoming a Kaggle Kernel grandmaster, with lots of tips
-   [Machine learning mega-benchmark: GPU providers (part 2)](https://rare-technologies.com/machine-learning-benchmarks-hardware-providers-gpu-part-2/)
    -   Comparison of Cloud GPU compute providers
-   [Learning from humans: what is inverse reinforcement learning?](https://thegradient.pub/learning-from-humans-what-is-inverse-reinforcement-learning/)
    -   Inverse reinforcement learning: given a policy or a set of data about an expert performing a task, try to extract a reward function
    -   Apprenticeship learning: given an expert policy, use it as a baseline from which to improve
-   [Retro Contest: Results](https://blog.openai.com/first-retro-contest-retrospective/)
    -   Short presentation of the winners of a reinforcement learning contest (they attempted to generalize from previous knowledge)
-   [CNNs from different viewpoints](https://medium.com/impactai/cnns-from-different-viewpoints-fab7f52d159c)
    -   Short post describing how to view CNNs as matrix multiplications or dense neural nets; informative
-   1(https://eng.uber.com/deconstructing-lottery-tickets/)
    -   Using a binary mask to zero out many of the model's weights leads to better accuracy
-   2(https://eng.uber.com/coordconv/)
    -   Introducing coordinates to convolution filters to give CNNs a way to model the coordinate transform task (increased performance in RL, Object detection)


### Tutorials and Guides


Tutorials:

-   [A Guide to TF Layers: Building a Convolutional Neural Network](https://www.tensorflow.org/tutorials/layers)
-   [Introduction to CNN Keras - Acc 0.997 (top 8%)](https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)
    -   A guide to a small but powerful CNN with a 99.671% accuracy on MNIST; uses data augmentation techniques
-   [A Guide to TF Layers: Building a Convolutional Neural Network](https://www.tensorflow.org/tutorials/layers)
    -   Tutorial about building CNNs in Tensorflow

Guides

-   [Tutorial: Optimizing Neural Networks using Keras (with Image recognition case study](https://www.analyticsvidhya.com/blog/2016/10/tutorial-optimizing-neural-networks-using-keras-with-image-recognition-case-study/)
    -   Widen your net, deepen your net, add dropout layers, change activation function, change network arhitecture
-   [A guide to convolution arithmetic for deep learning](https://arxiv.org/pdf/1603.07285v1.pdf)
-   [Which GPU(s) to Get for Deep Learning](http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/)
    -   Basically aim for a GTX 1080/1080Ti if you can afford it, if not go for a GTX 1070
-   [TF Estimators](https://www.tensorflow.org/programmers_guide/estimators)
    -   Amongst other things you can convert Keras models to TF estimators
-   [Understanding and Coding Inception Module in Keras](https://becominghuman.ai/understanding-and-coding-inception-module-in-keras-eb56e9056b4b)


### Papers


-   [Generative Temporal Models with Spatial Memory for Partially Observed Environments](https://arxiv.org/abs/1804.09401)
    -   [Videos of the agent in action](https://drive.google.com/file/d/1WLiyLRDUIMuOWtJEDIUxrTQCOOykeCE0/view)
    -   Generative Temporal Model with Spatial Memory, an action-conditioned generative model that uses a scalable non-parametric memory to store spatial and visual information; DND memory
    -   The agent learns an environment then can predict how the environment will look like after a number of time steps (hundreds) and moves
-   [Synthesizing Programs for Images using Reinforced Adversarial Learning](https://arxiv.org/abs/1804.01118)
    -   [Video of demonstration](https://www.youtube.com/watch?v=iSyvwAwa7vk&feature=youtu.be)
    -   Using GANs to train a RL one a cluster of machines; the algorithm learns to understand the creation of and recreate images it sees (drawing the digits of the MNIST dataset, characters from the POLIGLOT dataset) and even reconstruct 3D scenes
-   [Backdrop: Stochastic Backpropagation](https://arxiv.org/abs/1806.01337)
    -   Backdrop, a flexible and simple-to-implement method, intuitively described as dropout acting only along the backpropagation pipeline
-   [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
    -   Study of the quality of vector representations of words derived by various models on a collection of syntactic and semantic language tasks
-   [Rethinking the Inception Architecture for Computer Vision](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.pdf)
    -   Ideas for reducing computational complexity of CNNs, different Inception architectures
-   [Curiosity-driven Exploration bySelf-supervised Prediction](https://pathak22.github.io/noreward-rl/)
    -   RL with intrinsic curiosity reward manages to learn how to play Mario without extrinsic rewards, is able to generalize knowledge well; uses an Intrinsic Curiosity Module
-   [L2 Regularization versus Batch and Weight Normalization](https://arxiv.org/abs/1706.05350)
    -   These neural networks use L2 regularization, also called weight decay, ostensibly to prevent overfitting. However, we show that L2 regularization has no regularizing effect when combined with normalization
-   [Understanding the difficulty of training deep feedforward neural networks](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf)
-   [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
    -   ResNet architecture
-   [Wide Residual Networks](https://arxiv.org/abs/1605.07146)
    -   Wide ResNet architecture
-   [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](http://arxiv.org/abs/1502.03167)
-   [How Does Batch Normalization Help Optimization?](https://arxiv.org/pdf/1805.11604.pdf)
    -   An investigation into why Batch Normalization works. It is also compared to L losses. Apparently it works because it smoothens the optimization landscape; it doesn't have a large impact on ICS.
-   [Verification Of Non Linear Specifications For Neural Networks](https://arxiv.org/pdf/1902.09592.pdf)
    -   Mathematical tools for proving the robustness of a model against adversarial attacks
-   [Going deeper with convolutions](https://www.cc.gatech.edu/~hic/CS7616/Papers/Szegedy-et-al-2014.pdf)
-   [ImageNet Classification with Deep Convolutional Neural Networks](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf)
-   [Practical Recommendations for Gradient-Based Training of Deep Architectures](https://arxiv.org/pdf/1206.5533v2.pdf)
-   [CoupleNet: Paying Attention to Couples with Coupled Attention for Relationship Recommendation](https://arxiv.org/abs/1805.11535)
-   [DARTS: Differentiable Architecture Search](https://arxiv.org/abs/1806.09055)
-   [Learning Cognitive Models using Neural Networks](https://arxiv.org/abs/1806.08065)
-   [Going deeper with convolutions](https://arxiv.org/pdf/1409.4842.pdf)


### Courses and Books


Courses:

-   [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) - taught by AndrewNG
    -   ML course, presents the mathematics and concepts behind supervised and unsupervised learning algorithms, and has a good introduction to neural networks
    -   Great primer into machine learning
-   [Udacity Deep Learning](https://eu.udacity.com/course/deep-learning--ud730)
    -   Tensorflow Deep Learning course
    -   Good course for introducing a number of advanced concepts, but I feel it doesn't spend enough time on some of them
    -   Has a lot of good assignments in Tensorflow
-   [Udemy Zero to Deep Learning](https://www.udemy.com/zero-to-deep-learning/)
    -   Keras Deep Learning course
    -   Good course with many interesting assigments; provides an intro to data preprocessing and augmentation as well

Books:

-   [Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach%7CArtificial)
-   [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python)


### Tools

-  [Google Colaboratory]({% post_url /wiki/2018-10-05-google_colaboratory%}) - [go there now](https://colab.research.google.com)
-   [ConvNet Drawer](https://github.com/yu4u/convnet-drawer)
-   [Keras Visualization Toolkit](https://github.com/raghakot/keras-vis)
-  [Tensorboard]({% post_url /wiki/2018-09-23-tensorboard%})

### Existing work

-   [LeNet5](http://yann.lecun.com/exdb/lenet/)

Internal Resources
------------------

Learning ML

-  [Loss and Accuracy]({% post_url /wiki/2019-01-10-loss_and_accuracy%})
-  [Debugging ML algorithms]({% post_url /wiki/2019-02-15-debugging_ml_algorithms%})
    -  [Bias vs Variance]({% post_url /wiki/2019-02-15-debugging_ml_algorithms%})
    -  [Precision, Recall and F1 score]({% post_url /wiki/2019-02-15-debugging_ml_algorithms%})
    -  [Cross Entropy]({% post_url /wiki/2019-02-15-debugging_ml_algorithms%})
    -  [Learning Curve]({% post_url /wiki/2019-02-15-debugging_ml_algorithms%})
    -  [Learning rate and number of epochs]({% post_url /wiki/2019-02-15-debugging_ml_algorithms%})



-  [Reinforcement Learning]({% post_url /wiki/2019-04-26-reinforcement_learning%})



-  [Neural Networks]({% post_url /wiki/2019-03-07-neural_networks%})
    -  [Basics]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Simple Neural Network]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Data Preprocessing]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Weight Initialization]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [One hot encoding]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Softmax]({% post_url /wiki/2019-03-07-neural_networks%})
    -  [Activation Functions]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Step]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Sigmoid]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Tanh]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [ReLU]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Softplus]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Softmax]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Optimization]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [(Batch) Gradient Descent]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [Stochastic Gradient Descent]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [Convergence]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [Online Learning]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [Map Reduce and Parallelism]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [SGD with Momentum]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [AdaGrad]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [AdaDelta]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [RMSProp]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [Adam]({% post_url /wiki/2019-03-07-neural_networks%})
            -  [Choosing the Best Optimizer]({% post_url /wiki/2019-03-07-neural_networks%})
    -  [Regularization]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Batch Normalization]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Local Response Normalization]({% post_url /wiki/2019-03-07-neural_networks%})
    -  [Embeddings]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [Skip Gram]({% post_url /wiki/2019-03-07-neural_networks%})
        -  [CBOW]({% post_url /wiki/2019-03-07-neural_networks%})
    -  [Architectures]({% post_url /wiki/2019-03-07-neural_networks%})



-  [Types of Neural Networks]({% post_url /wiki/2018-06-21-types_of_neural_networks%})
    -  [Recurrent Neural Network]({% post_url /wiki/2018-06-21-types_of_neural_networks%})
        -  [LSTM]({% post_url /wiki/2018-06-21-types_of_neural_networks%})
        -  [GRU]({% post_url /wiki/2018-06-21-types_of_neural_networks%})
    -  [Convolutional Neural Networks]({% post_url /wiki/2018-06-21-types_of_neural_networks%})
        -  [CNN Visualizations]({% post_url /wiki/2019-01-30-cnn_visualizations%})
            -  [Activation Maximization]({% post_url /wiki/2019-01-30-cnn_visualizations%})
            -  [Saliency Maps]({% post_url /wiki/2019-01-30-cnn_visualizations%})
            -  [Class Activation Maps]({% post_url /wiki/2019-01-30-cnn_visualizations%})
-  [Types of Machine Learning Problems]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
    -  [Supervised Learning]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
        -  [Regression problems]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
        -  [Classification problems]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
        -  [Support Vector Machines]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
        -  [Natural Language Processing]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
    -  [Unsupervised Learning]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
        -  [Anomaly Detection]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
        -  [Clustering]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})
    -  [Reinforcement Learning]({% post_url /wiki/2019-02-22-types_of_machine_learning_algorithms%})



-  [Machine Learning Advice]({% post_url /wiki/2018-06-18-machine_learning_advice%})
    -  [Dataset Management]({% post_url /wiki/2018-06-18-machine_learning_advice%})
    -  [Pipeline]({% post_url /wiki/2018-06-18-machine_learning_advice%})
    -  [Ceiling Analysis]({% post_url /wiki/2018-06-18-machine_learning_advice%})
    -  [Increasing Your Dataset Size]({% post_url /wiki/2018-06-18-machine_learning_advice%})

Tools:

-  [Tensorboard]({% post_url /wiki/2018-09-23-tensorboard%})

Projects

-  [Iris classifier]({% post_url /wiki/2018-07-01-iris_classifier%})
-  [MNIST classifier]({% post_url /wiki/2018-07-01-mnist_classifier%})

Discussion:

-  [Artificial Intelligence Explained]({% post_url /wiki/2019-01-08-artificial_intelligence_explained%})



-  [Tensorflow vs Keras]({% post_url /wiki/2018-06-05-tensorflow_vs_keras%})

Guides:

-  [Installing Tensorflow on ArchLinux]({% post_url /wiki/2018-06-05-installing_tensorflow_on_archlinux%})
-  [Installing Keras on ArchLinux]({% post_url /wiki/2018-06-05-installing_keras_on_archlinux%})
-  [Installing Jupyter notebook with a virtualenv kernel]({% post_url /wiki/2018-06-13-installing_jupyter_notebook_with_a_virtualenv_kernel%})

