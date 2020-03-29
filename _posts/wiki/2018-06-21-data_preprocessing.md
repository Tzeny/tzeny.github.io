---
title: Data Preprocessing
layout: post
base: Wiki
base_url: /wiki
hidden: true
---

Data preprocessing is a data mining technique that involves transforming raw data into an understandable format. Real-world data is often incomplete, inconsistent, and/or lacking in certain behaviors or trends, and is likely to contain many errors. Data preprocessing is a proven method of resolving such issues. Data preprocessing prepares raw data for further processing.[1]

Data preprocessing in Python
----------------------------

In python we can use the [Pandas library](https://pandas.pydata.org/) to preprocess data.

``` python
import pandas as pd

df = pd.read_csv('../data/titanic-train.csv')

df.head() #shows the head of the loaded dataset

df.info() #number of entries for each feature and feature type

df.describe() #see information about the numerical features
```

See [Panda examples from Udemy course](https://tzeny.ddns.net:4430/Tzeny/udemy-zero-to-deep-learning/blob/master/course/2%20Data.ipynb)

### IMDB dataset

We'll want to build a reverse dictionary and pad our data (make all reviews have the same length)

``` python
from keras.datasets import imdb

(X_train, y_train), (X_test, y_test) = imdb.load_data('/tmp/imdb.npz',
                                                      num_words=None,
                                                      skip_top=0,
                                                      maxlen=None,
                                                      start_char=1,
                                                      oov_char=2,
                                                      index_from=3)

max(idx.values())#number of different words

rev_idx = {v+3:k for k,v in idx.items()}
rev_idx[0] = 'padding_char'
rev_idx[1] = 'start_char'
rev_idx[2] = 'oov_char'
rev_idx[3] = 'unk_char'

#transform review from indices to words
example_review = ' '.join([rev_idx[word] for word in X_train[0]])
print(example_review)

from keras.preprocessing.sequence import pad_sequences

#this type of padding preserves the last maxlen datapoints
X_train_pad = pad_sequences(X_train, maxlen=maxlen)
X_test_pad = pad_sequences(X_test, maxlen=maxlen)
```

### One hot encoding

``` python
from keras.utils import np_utils

uniques, ids = np.unique(y, return_inverse=True)
y_code = np_utils.to_categorical(ids, len(uniques))
```

### Train set split

``` python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X.values, y_cat, test_size=0.2)
```

### Normalization

#### Standard normalization

We want our data to have μ(mean)=0 and σ(Xi)=σ(Xj) for any j!=i (variance).

``` python
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

#for training data and unseen data
train = ss.fit_transform(train)#learn a set of scaling/shifting operations to fit the data in a standard distribution with mean 0 and variance 1
test = ss.transform(test)#apply the same operations to previously unseen test data
```

#### MinMax normalization

We'll scale our data to fit on a scale from 0.0 to 1.0

``` python
from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler()

#for training data and unseen data
train = mms.fit_transform(train)#learn a set of scaling/shifting operations to fit the data in the [0,1] range
test = mms.transform(test)#apply the same operations to previously unseen test data
```

[1] <https://www.techopedia.com/definition/14650/data-preprocessing>
