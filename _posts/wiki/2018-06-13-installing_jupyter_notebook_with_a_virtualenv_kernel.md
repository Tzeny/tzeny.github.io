---
title: Installing Jupyter notebook with a virtualenv kernel
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

Based on a StackOverflow answer1.Kernels are computation units for Jupyter notebook. I wanted to create a kernel that uses the python interpreter in my virtual environment. I will be assuming you have virtualenv-wrapper.

In my case I made a new virtual environment jupyter3:

``` bash
cd ~
#first we will generate a list of all our packages in the tensorflow environment
workon tensorflow
pip freeze > requirements.txt

deactivate

#next we will create the Jupyter virtualenv
mkvirtualenv -p python3 jupyter3
workon jupyter3

pip install -r requirements.txt #I generated this with pip freeze > requirements.txt from the tensorflow virtualenv
pip install jupyter ipykernel
rm requirements.txt #we no longer need this file

ipython kernel install --name "jupyter3_Python_3" --user

which python #note this down as we will need to replace this in the kernel.json

nano ~/local/share/jupyter/kernels/jupyter3_python_3/kernel.json
```

Override the “/usr/bin/python” with the path resulted when you ran which; in my case it was “/home/tzeny/Other/Virtualenvs/jupyter3/bin/python”.

Note: Add optirun to argv before the python path to enable GPU support.

    #~/local/share/jupyter/kernels/jupyter3_python_3/kernel.json
    {
     "argv": [
      "optirun", #this is only required for GPU support
      "/home/tzeny/Other/Virtualenvs/jupyter3/bin/python",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}"
     ],
     "display_name": "jupyter3_Python_3",
     "language": "python"
    }

Save and exit. Now to test your kernel, start jupyter-notebook, create a new file, from the Kernel menu button select our new kernel jupyter3_python_3, and try to import keras.

{% include figure_caption.html url="/assets/img/wiki/Jupyter_kernel.png" description="border" %}

When you ran the program you should see no errors.

1. [https://stackoverflow.com/questions/33496350/execute-python-script-within-jupyter-notebook-using-a-specific-virtualenv](https://stackoverflow.com/questions/33496350/execute-python-script-within-jupyter-notebook-using-a-specific-virtualenv)
