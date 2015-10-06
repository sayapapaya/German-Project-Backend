
# coding: utf-8

# In[33]:

import numpy as np
from textblob_de import TextBlobDE as TextBlob
from textblob_de import PatternParser
from textblob_de.lemmatizers import PatternParserLemmatizer
import nltk


# In[25]:

# read text and create blob object
file_path = "Articles/Aschenputtel"
f = open(file_path)
article = f.read().decode('utf-8')
blob = TextBlob(article, parser=PatternParser(pprint=True, lemmata=True))


# In[26]:

# extract average number of words per sentence
sentences = blob.sentences
average_sentence_length = np.mean(np.array([len(sentence.words) for sentence in sentences]))
average_sentence_length


# In[27]:

# extract average word length
words = blob.words
average_word_length = np.mean(np.array([len(word) for word in words]))
average_word_length


# In[28]:

# count number of words with each part of speech tag
tags = blob.tags
number_of_tags = float(len(tags))
unique_tags = set([t[1] for t in tags])
number_of_each_tag = {pos: sum([1 for t in tags if t[1] == pos]) for pos in unique_tags}
relative_frequency_of_each_tag = {k : v / number_of_tags for k, v in number_of_each_tag.items()}
relative_frequency_of_each_tag


# For more on POS tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html 
# If used as feature, combine certain dimensions, and make dimensions be .e.g. relative frequency of nouns or verbs etc.?
# 

# In[40]:

# blob.noun_phrases
# blob.parse()


# Lemmatizing entire text or single words below:

# In[45]:

_lemmatizer = PatternParserLemmatizer()
# _lemmatizer.lemmatize(article)
print words
print words[0]
print _lemmatizer.lemmatize(words[0])


# In[42]:

a = 2
b = 3
a + b


# In[ ]:




# In[ ]:



