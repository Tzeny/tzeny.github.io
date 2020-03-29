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

### <span class="mw-customtoggle-articles">Articles</span>

<div class="mw-collapsible mw-collapsed" id="mw-customcollapsible-articles">
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
-   [1](https://eng.uber.com/deconstructing-lottery-tickets/)
    -   Using a binary mask to zero out many of the model's weights leads to better accuracy
-   [2](https://eng.uber.com/coordconv/)
    -   Introducing coordinates to convolution filters to give CNNs a way to model the coordinate transform task (increased performance in RL, Object detection)

</div>
### <span class="mw-customtoggle-tutguide">Tutorials and Guides</span>

<div class="mw-collapsible mw-collapsed" id="mw-customcollapsible-tutguide">
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

</div>
### <span class="mw-customtoggle-papers">Papers</span>

<div class="mw-collapsible mw-collapsed" id="mw-customcollapsible-papers">
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
    -   An investigation into why Batch Normalization works. It is also compared to L<smth> losses. Apparently it works because it smoothens the optimization landscape; it doesn't have a large impact on ICS.
-   [Verification Of Non Linear Specifications For Neural Networks](https://arxiv.org/pdf/1902.09592.pdf)
    -   Mathematical tools for proving the robustness of a model against adversarial attacks
-   [Going deeper with convolutions](https://www.cc.gatech.edu/~hic/CS7616/Papers/Szegedy-et-al-2014.pdf)
-   [ImageNet Classification with Deep Convolutional Neural Networks](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf)
-   [Practical Recommendations for Gradient-Based Training of Deep Architectures](https://arxiv.org/pdf/1206.5533v2.pdf)
-   [CoupleNet: Paying Attention to Couples with Coupled Attention for Relationship Recommendation](https://arxiv.org/abs/1805.11535)
-   [DARTS: Differentiable Architecture Search](https://arxiv.org/abs/1806.09055)
-   [Learning Cognitive Models using Neural Networks](https://arxiv.org/abs/1806.08065)
-   [Going deeper with convolutions](https://arxiv.org/pdf/1409.4842.pdf)

</div>
### <span class="mw-customtoggle-courbook">Courses and Books</span>

<div class="mw-collapsible mw-collapsed" id="mw-customcollapsible-courbook">
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

</div>
### Tools

-   [Google Colaboratory](/Google_Colaboratory "wikilink") - [go there now](https://colab.research.google.com)
-   [ConvNet Drawer](https://github.com/yu4u/convnet-drawer)
-   [Keras Visualization Toolkit](https://github.com/raghakot/keras-vis)
-   [Tensorboard](/Tensorboard "wikilink")

### Existing work

-   [LeNet5](http://yann.lecun.com/exdb/lenet/)

Internal Resources
------------------

Learning ML

-   [Loss and Accuracy](/Loss_and_Accuracy "wikilink")
-   [Debugging ML algorithms](/Debugging_ML_algorithms "wikilink")
    -   [Bias vs Variance](/Debugging_ML_algorithms#Bias_vs_Variance "wikilink")
    -   [Precision, Recall and F1 score](/Debugging_ML_algorithms#Precision_and_recall "wikilink")
    -   [Cross Entropy](/Debugging_ML_algorithms#Cross_Entropy "wikilink")
    -   [Learning Curve](/Debugging_ML_algorithms#Learning_curve "wikilink")
    -   [Learning rate and number of epochs](/Debugging_ML_algorithms#Learning_rate_and_number_of_epochs "wikilink")

<!-- -->

-   [Reinforcement Learning](/Reinforcement_Learning "wikilink")

<!-- -->

-   [Neural Networks](/Neural_Networks "wikilink")
    -   [Basics](/Neural_Networks#Basics "wikilink")
        -   [Simple Neural Network](/Neural_Networks#Simple_network "wikilink")
        -   [Data Preprocessing](/Neural_Networks#Data_preprocessing "wikilink")
        -   [Weight Initialization](/Neural_Networks#Weight_initialization "wikilink")
        -   [One hot encoding](/Neural_Networks#One_hot_encoding "wikilink")
        -   [Softmax](/Neural_Networks#Softmax "wikilink")
    -   [Activation Functions](/Neural_Networks#Activation_functions "wikilink")
        -   [Step](/Neural_Networks#Step "wikilink")
        -   [Sigmoid](/Neural_Networks#Sigmoid "wikilink")
        -   [Tanh](/Neural_Networks#Hyperbolic_Tangent.28tanh.29 "wikilink")
        -   [ReLU](/Neural_Networks#ReLU.28rectified_linear_unit.29 "wikilink")
        -   [Softplus](/Neural_Networks#Softplus "wikilink")
        -   [Softmax](/Neural_Networks#Softmax "wikilink")
        -   [Optimization](/Neural_Networks#Optimization.5B10.5D "wikilink")
            -   [(Batch) Gradient Descent](/Neural_Networks#.28Batch.29_Gradient_Descent "wikilink")
            -   [Stochastic Gradient Descent](/Neural_Networks#Stochastic_Gradient_Descent "wikilink")
            -   [Convergence](/Neural_Networks#Convergence "wikilink")
            -   [Online Learning](/Neural_Networks#Online_learning "wikilink")
            -   [Map Reduce and Parallelism](/Neural_Networks#Neural_Networks#Map_Reduce_and_Parallelism "wikilink")
            -   [SGD with Momentum](/Neural_Networks#SGD_with_momentum "wikilink")
            -   [AdaGrad](/Neural_Networks#AdaGrad.5B11.5D "wikilink")
            -   [AdaDelta](/Neural_Networks#AdaDelta.5B12.5D "wikilink")
            -   [RMSProp](/Neural_Networks#RMSProp.5B13.5D "wikilink")
            -   [Adam](/Neural_Networks#Adam.5B14.5D "wikilink")
            -   [Choosing the Best Optimizer](/Neural_Networks#Choosing_the_best_optimizer "wikilink")
    -   [Regularization](/Neural_Networks#Regularization "wikilink")
        -   [Batch Normalization](/Neural_Networks#Batch_Normalization_.5B15.5D "wikilink")
        -   [Local Response Normalization](/Neural_Networks#Local_Response_Normalization.5B17.5D "wikilink")
    -   [Embeddings](/Neural_Networks#Embeddings "wikilink")
        -   [Skip Gram](/Neural_Networks#Skip-gram "wikilink")
        -   [CBOW](/Neural_Networks#CBOW_.28Continuous_bag_of_words.29 "wikilink")
    -   [Architectures](/Neural_Networks#Architectures "wikilink")

<!-- -->

-   [Types of Neural Networks](/Types_of_Neural_Networks "wikilink")
    -   [Recurrent Neural Network](/Types_of_Neural_Networks#Recurrent_neural_network "wikilink")
        -   [LSTM](/Types_of_Neural_Networks#LSTM_-_long_short_term_memory "wikilink")
        -   [GRU](/Types_of_Neural_Networks#GRU_-_gated_recurrent_unit "wikilink")
    -   [Convolutional Neural Networks](/Types_of_Neural_Networks#Convolutional_Neural_Networks "wikilink")
        -   [CNN Visualizations](/CNN_Visualizations "wikilink")
            -   [Activation Maximization](/CNN_Visualizations#Activation_Maximization "wikilink")
            -   [Saliency Maps](/CNN_Visualizations#Saliency_Maps "wikilink")
            -   [Class Activation Maps](/CNN_Visualizations#Class_Activation_Maps "wikilink")
-   [Types of Machine Learning Problems](/Types_of_Machine_Learning_algorithms "wikilink")
    -   [Supervised Learning](/Types_of_Machine_Learning_algorithms#Supervised_Learning "wikilink")
        -   [Regression problems](/Types_of_Machine_Learning_algorithms#Regression_problem "wikilink")
        -   [Classification problems](/Types_of_Machine_Learning_algorithms#Classification_problems "wikilink")
        -   [Support Vector Machines](/Types_of_Machine_Learning_algorithms#Support_vector_machines "wikilink")
        -   [Natural Language Processing](/Types_of_Machine_Learning_algorithms#Natural_Language_Processing "wikilink")
    -   [Unsupervised Learning](/Types_of_Machine_Learning_algorithms#Unsupervised_learning "wikilink")
        -   [Anomaly Detection](/Types_of_Machine_Learning_algorithms#Anomaly_Detection "wikilink")
        -   [Clustering](/Types_of_Machine_Learning_algorithms#Clustering "wikilink")
    -   [Reinforcement Learning](/Types_of_Machine_Learning_algorithms#Reinforcement_learning "wikilink")

<!-- -->

-   [Machine Learning Advice](/Machine_Learning_Advice "wikilink")
    -   [Dataset Management](/Machine_Learning_Advice#Dataset_management "wikilink")
    -   [Pipeline](/Machine_Learning_Advice#Pipeline "wikilink")
    -   [Ceiling Analysis](/Machine_Learning_Advice#Ceiling_analysis "wikilink")
    -   [Increasing Your Dataset Size](/Machine_Learning_Advice#Increasing_your_dataset_size "wikilink")

Tools:

-   [Tensorboard](/Tensorboard "wikilink")

Projects

-   [Iris classifier](/Iris_classifier "wikilink")
-   [MNIST classifier](/MNIST_classifier "wikilink")

Discussion:

-   [Artificial Intelligence Explained](/Artificial_Intelligence_Explained "wikilink")

<!-- -->

-   [Tensorflow vs Keras](/Tensorflow_vs_Keras "wikilink")

Guides:

-   [Installing Tensorflow on ArchLinux](/Installing_Tensorflow_on_ArchLinux "wikilink")
-   [Installing Keras on ArchLinux](/Installing_Keras_on_ArchLinux "wikilink")
-   [Installing Jupyter notebook with a virtualenv kernel](/Installing_Jupyter_notebook_with_a_virtualenv_kernel "wikilink")

