
import numpy as np
from textblob_de import TextBlobDE as TextBlob
from textblob_de import PatternParser
from textblob_de.lemmatizers import PatternParserLemmatizer
import nltk

<<<<<<< HEAD
from pattern.de import gender, MALE, FEMALE, NEUTRAL,parse,split
from pattern.de import conjugate, SUBJUNCTIVE, PRESENT,INFINITIVE,SG,PAST,PL



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

def get_avg_number_of_tags_in_tag_set_per_sentence(blob, tag_string_set):
    """ TODO:
    -- Katrine rewrite to take function / be cleaner code

    """


    """
    Returns average number of occurences of words with tags that exist in 
    the tag_string_set per sentence in a blob object. 

    For example,
    sentence = "John ate the apple."
    tag_string_set = set("NN", "NNP")
    number of occurences of words in the sentence that have tags in the
        tag_string_set are two ("John" and "apple")

    blob -- a blob object
    tag_string -- a set of strings, each string specifying the Penn Treebank POS tag

    """

    sentences = blob.sentences
    number_of_nouns_per_sentence = []
    for s in sentences:
        number_nouns = len([t for t in s.tags if t[1] in tag_string_set])
        number_of_nouns_per_sentence.append(number_nouns)

    avg_number_nouns_per_sentence = np.mean(np.array(number_of_nouns_per_sentence))
    return avg_number_nouns_per_sentence

def get_avg_number_of_nouns_per_sentence(blob):
    noun_tags = set(["NN", "NNS", "NNP", "NNPS"])
    return get_avg_number_of_tags_in_tag_set_per_sentence(blob, noun_tags)

def get_avg_number_of_verbs_per_sentence(blob):
    verb_tags = set(["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"])
    return get_avg_number_of_tags_in_tag_set_per_sentence(blob, verb_tags)


def count_words_that_meet_criteria(blob, criteria_function):
    """
    Saya implements
    & also implements ratio of past tense among verbs,

    """

    pass

def count_sentences_that_meet_criteria(blob, criteria_function):
    """
    Katrine implements
    & criteria_function that 

    """
    sentences = blob.sentences
    count = len([s for s in sentences if criteria_function(s)])
    return count


def if_sentence_contains_past_participle(sentence):
    
    """
    Katrine TODO
    """
    words = sentence.words
    pass

def get_number_unique_lemmas(blob):
    """
    Saya TODO

    """

def get_length_of_longest_sentence(blob):
    """
    Katrine TODO
    
    """

def get_length_of_article(blob):
    """

    """
    return len(blob.words)


# For more on POS tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html 
# If used as feature, combine certain dimensions, and make dimensions be .e.g. relative frequency of nouns or verbs etc.? 

# blob.noun_phrases
# blob.parse()


# Lemmatizing entire text or single words below:
# _lemmatizer = PatternParserLemmatizer()
# _lemmatizer.lemmatize(article)

#helper function for finding subjunctive conjugation
#pass in a verb and check if it is subjunctive
def check_if_subjunctive(word):
    _lemmatizer = PatternParserLemmatizer()
    lemma =  _lemmatizer.lemmatize(word)[0][0]
    if conjugate(lemma, PRESENT, 1, SG, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PRESENT, 2, SG, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PRESENT, 3, SG, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PRESENT, 1, PL, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PRESENT, 2, PL, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PRESENT, 3, PL, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PAST, 1, SG, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PAST, 2, SG, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PAST, 3, SG, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PAST, 1, PL, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PAST, 2, PL, mood=SUBJUNCTIVE) == word:
        return True
    elif conjugate(lemma, PAST, 3, PL, mood=SUBJUNCTIVE) == word:
        return True
    else:
        return False
    
