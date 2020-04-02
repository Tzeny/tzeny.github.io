---
title: Word Embeddings
layout: wiki_post
base: Wiki
base_url: /wiki
categories:
  - wikiprojects
hidden: true
---

So, I've spent the last 2 days working on understanding word embeddings. There are 2 methods I have tried for this,[Skip Gram]({% post_url /wiki/2019-03-07-neural_networks%}) and[CBOW]({% post_url /wiki/2019-03-07-neural_networks%})

Git
---

Source code for my attempts: [<https://github.com/Tzeny/udacity-deep-learning/blob/master/5_word2vec.ipynb>](https://github.com/Tzeny/udacity-deep-learning/blob/master/5_word2vec.ipynb)

In the git repository above I've also included the embeddings matrix resulted from the trained in the form of a .pickle file.

Example predictions
-------------------

Some examples from the skip-gram training:

` Nearest to one: two, four, seven, eight, three, six, five, nine,`
` Nearest to man: person, woman, boy, chanute, glasgow, programmatical, trudeau, revenge,`
` Nearest to concept: form, idea, locational, testimony, result, definition, tordesillas, nisos,`
