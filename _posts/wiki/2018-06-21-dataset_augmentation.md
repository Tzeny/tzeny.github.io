---
title: Dataset Augmentation
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

{% include figure_caption.html url="/assets/img/wiki/Data-augmentation.jpg" description="Dataset augmentation examples" %} To train large ML models we need a lot of data. To that end we could collect more labels, but that is expensive and slow or we can automatically augment our data set.

For an image data set we could:

-   scale the image
-   move it around
-   skew the image
-   make occlusions in the image
-   change the colours
-   rotate the image
-   add noise (not always effective unless you expect to see noise in the real test set)
-   zoom the image

``` python
from keras.preprocessing.image import ImageDataGenerator

generator = ImageDataGenerator(rescale = 1./255,
                               width_shift_range=0.1,
                               height_shift_range=0.1,
                               rotation_range = 20,
                               shear_range = 0.3,
                               zoom_range = 0.3,
                               horizontal_flip = True)

train = generator.flow_from_directory('../data/generator',
                                      target_size = (128, 128),
                                      batch_size = 32,
                                      class_mode = 'binary')

img, label = train.next()
```
