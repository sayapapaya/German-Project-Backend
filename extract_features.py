

import numpy as np
from textblob_de import TextBlobDE as TextBlob
from textblob_de import PatternParser
from textblob_de.lemmatizers import PatternParserLemmatizer
import nltk

from pattern.de import gender, MALE, FEMALE, NEUTRAL, parse, split


# read text and create blob object
file_name = "Articles/Aschenputtel"
def get_blob(file_path):
    f = open(file_path)
    article = f.read().decode('utf-8')
    blob = TextBlob(article, parser=PatternParser(pprint=True, lemmata=True))
    return blob

# extract average number of words per sentence
def get_avg_sentence_length(blob):
    sentences = blob.sentences
    average_sentence_length = np.mean(np.array([len(sentence.words) for sentence in sentences]))
    return average_sentence_length

# extract average word length
def get_avg_word_length(blob):
    words = blob.words
    average_word_length = np.mean(np.array([len(word) for word in words]))
    return average_word_length

# count number of words with each part of speech tag
# uses only Penn Treebank tags
def get_relative_frequency_of_pos_tags(blob):
    tags = blob.tags
    number_of_tags = float(len(tags))
    unique_tags = set([t[1] for t in tags])
    number_of_each_tag = {pos: sum([1 for t in tags if t[1] == pos]) for pos in unique_tags}
    relative_frequency_of_each_tag = {k : v / number_of_tags for k, v in number_of_each_tag.items()}
    return relative_frequency_of_each_tag

def get_avg_number_of_tag_per_sentence(blob, tag_string):
    """
    Returns average number of occurences of a given tag per sentence in a blob object
    blob -- a blob object
    tag_string -- a string specifying the Penn Treebank POS tag

    """
    sentences = blob.sentences
    number_of_nouns_per_sentence = []
    for s in sentences[0:5]:
        tags = s.tags
        number_nouns = len([t for t in tags if t[1] == tag_string])
        number_of_nouns_per_sentence.append(number_nouns)

    avg_number_nouns_per_sentence = np.mean(np.array(number_of_nouns_per_sentence))
    return avg_number_nouns_per_sentence




# For more on POS tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html 
# If used as feature, combine certain dimensions, and make dimensions be .e.g. relative frequency of nouns or verbs etc.? 

# blob.noun_phrases
# blob.parse()


# Lemmatizing entire text or single words below:
# _lemmatizer = PatternParserLemmatizer()
# _lemmatizer.lemmatize(article)


