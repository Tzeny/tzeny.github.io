---
title: Installing Tensorflow on ArchLinux
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

Based on this guide[1]

Installing packages
-------------------

<b>Important note</b>: You should start by installing Bumblebee and making sure it works: ([Arch Linux Wiki Bumblebee](https://wiki.archlinux.org/index.php/Bumblebee)

My package versions:

``` bash
nvidia 396.24-7
python-numpy 1.14.3-1
swig 3.0.12-1
cudnn 7.1.4-1
cuda 9.0.176-4
python 3.6.5-3
python-virtualenv 15.1.0-3
```

``` bash
pacman -S nvidia python-numpy swig cudnn cuda python3 python-virtualenv
```

Then reboot. This should install all necessary packages.

In my case I also had to downgrade CUDA to version 9.x. I used this [AUR Package](https://aur.archlinux.org/packages/downgrade/).

``` bash
sudo downgrade cuda
```

(and select the highest version 9.0.x)

Virtualenv
----------

My PIP packages:

``` bash
absl-py==0.2.2
astor==0.6.2
bleach==1.5.0
gast==0.2.0
grpcio==1.12.1
html5lib==0.9999999
Markdown==2.6.11
numpy==1.14.3
protobuf==3.5.2.post1
six==1.11.0
tensorboard==1.8.0
tensorflow-gpu==1.8.0
termcolor==1.1.0
Werkzeug==0.14.1
```

Next create a new Python3 virtualenv.

``` bash
virtualenv -p python3 tensorflow-env
source tensorflow/bin/activate
```

We'll need to update PIP and install the latest tensorflow-gpu package

``` bash
pip install --upgrade pip

pip install --upgrade tensorflow-gpu
```

Validating our installation
---------------------------

Based on this guide[2]

To validate our installation we'll use the following Python file

``` python
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')

sess = tf.Session()

print(sess.run(hello))
```

I saved it to test.py, and ran it using the command:

``` bash
optirun python test.py
```

(optirun is required to turn on the GPU)

The output should be something similar to this:

``` bash
2018-06-05 09:44:13.468281: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2018-06-05 09:44:13.545180: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:898] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2018-06-05 09:44:13.545552: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1356] Found device 0 with properties:
name: GeForce GTX 1050 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.62
pciBusID: 0000:01:00.0
totalMemory: 3.95GiB freeMemory: 3.89GiB
2018-06-05 09:44:13.545566: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1435] Adding visible gpu devices: 0
2018-06-05 09:44:13.733866: I tensorflow/core/common_runtime/gpu/gpu_device.cc:923] Device interconnect StreamExecutor with strength 1 edge matrix:
2018-06-05 09:44:13.733913: I tensorflow/core/common_runtime/gpu/gpu_device.cc:929]      0
2018-06-05 09:44:13.733919: I tensorflow/core/common_runtime/gpu/gpu_device.cc:942] 0:   N
2018-06-05 09:44:13.734069: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1053] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 3623 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1050 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1)
b'Hello, TensorFlow!'
(tensorflow)
```

If you run it without optirun it will look like this (does not detect GPU):

``` bash
python test.py
2018-06-05 09:11:15.197152: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2018-06-05 09:11:15.375056: E tensorflow/stream_executor/cuda/cuda_driver.cc:406] failed call to cuInit: CUDA_ERROR_UNKNOWN
2018-06-05 09:11:15.375095: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:145] kernel driver does not appear to be running on this host (saber): /proc/driver/nvidia/version does not exist
b'Hello, TensorFlow!'
(tensorflow)
```

<references />

[1] <https://github.com/ddigiorg/AI-TensorFlow/blob/master/install/install-TF_2016-02-27.md>

[2] <https://www.tensorflow.org/install/install_linux#ValidateYourInstallation>
