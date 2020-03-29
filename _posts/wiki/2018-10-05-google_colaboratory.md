---
title: Google Colaboratory
layout: post
base: Wiki
base_url: /wiki
hidden: true
---


When you log in and connect to the Colaboratory runtime, you will get your own virtual machine with a K80 GPU (not always entirely yours, read below) and a Jupyter notebook environment. You can use it to your heart's content for up to 12 hours. Or until you close your browser window. Be warned, sometimes the runtime can disconnect randomly.

For more information check out the [Google Colaboratory FAQ](https://research.google.com/colaboratory/faq.html)

Tips and tricks
===============

-   Notebook stuck on initializing: click on 'Runtime' tab, click on 'Restart runtime...' [1]
-   If you start a line in Jupyter Notebook with '!', the line will execute as a command on the virtual machine supporting the runtime. Example:
        !pwd

Getting your own GPU[2]:
------------------------

So, if you want to use Google Colaboratory you should be aware that you may end up being not so lucky and share a K80 with somebody else. The main disadvantage of this is that you won't have the full RAM of the GPU available and Tensorflow might throw out of resources exceptions. To see how much ram you have available run this script.

``` python
!ln -sf /opt/bin/nvidia-smi /usr/bin/nvidia-smi
!pip install gputil
!pip install psutil
!pip install humanize
import psutil
import humanize
import os
import GPUtil as GPU
GPUs = GPU.getGPUs()
# XXX: only one GPU on Colab and isn’t guaranteed
gpu = GPUs[0]
def printm():
 process = psutil.Process(os.getpid())
 print("Gen RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " | Proc size: " + humanize.naturalsize( process.memory_info().rss))
 print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
printm()
```

If you're lucky and you get access to the full card you'll see something like this:

` Gen RAM Free: 11.6 GB  | Proc size: 666.0 MB`
` GPU RAM Free: 11439MB | Used: 0MB | Util  0% | Total 11439MB`

If you see RAM usage, that means that you are sharing the card with someone. Since by default Tensorflow allocates almost 100% of the GPU's memory this is a problem. To get a new instance and a new chance to get you own GPU, run the following command in a cell:

` !kill -9 -1`

Then wait 30-60 seconds and reconnect and check with the above script if you got your own GPU.

Making sure you're training on the GPU[3]
-----------------------------------------

This code trains a sample model on the GPU.

``` python
import tensorflow as tf

with tf.device('/gpu:0'):
  model.fit(X_train, y_train, epochs=10,batch_size=128, verbose=1)
```

File transfer to Google Colaboratory
====================================

Although the first method described below seems more involved, I think it's the best one as I have had problems with the second method in the past.

Mounting a Google Drive folder inside your Jupyter Noteook[4]
-------------------------------------------------------------

Mount your Google Drive inside the Notebook.

``` python
import os
from google.colab import drive
drive.mount('/gdrive')
os.symlink('/gdrive/My Drive', 'my_drive')

!ls -l my_drive
```

Saving Data[5] using the Google Colaboratory Python library
-----------------------------------------------------------

To download data you can also use the files library provided by Google.

``` python
from keras.models import model_from_json

#save model and weights
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

from google.colab import files

files.download('model.json')
files.download('model.h5')
```

Loading Data[6] using the Google Colaboratory Python library
------------------------------------------------------------

You can also upload your own files using the same library.

``` python
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

from keras.models import model_from_json

# load model and weights
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

model = loaded_model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```

[1] <https://stackoverflow.com/questions/49090430/notebook-stuck-on-initializing-when-using-gpu-backend>

[2] <https://stackoverflow.com/questions/48750199/google-colaboratory-misleading-information-about-its-gpu-only-5-ram-available>

[3] <https://stackoverflow.com/questions/40690598/can-keras-with-tensorflow-backend-be-forced-to-use-cpu-or-gpu-at-will>

[4] <https://github.com/googlecolab/colabtools/issues/276>

[5] <https://stackoverflow.com/questions/50166987/how-to-download-tensorflow-trained-model-on-google-colab>

[6] <https://colab.research.google.com/notebooks/io.ipynb#scrollTo=vz-jH8T_Uk2c>
