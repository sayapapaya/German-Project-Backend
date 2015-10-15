
import numpy as np
from textblob_de import TextBlobDE as TextBlob
from textblob_de import PatternParser
from textblob_de.lemmatizers import PatternParserLemmatizer
import nltk

from pattern.de import gender, MALE, FEMALE, NEUTRAL,parse,split
from pattern.de import conjugate, SUBJUNCTIVE, PRESENT,INFINITIVE,SG,PAST,PL



# read text and create blob object
def get_blob(file_path):
    f = open(file_path)
    article = f.read().decode('utf-8')
    blob = TextBlob(article, parser=PatternParser(pprint=True, lemmata=True))
    return blob

def get_length_of_article(blob):
    """Returns number of words in Blob object"""
    return len(blob.words)


def get_length_of_longest_sentence(blob):
    """Returns the number of words in the longest sentence in the Blob."""
    sentence_lengths = [len(s.words) for s in blob.sentences]
    return max(sentence_lengths)


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
    """
    """
    tags = blob.tags
    number_of_tags = float(len(tags))
    unique_tags = set([t[1] for t in tags])
    number_of_each_tag = {pos: sum([1 for t in tags if t[1] == pos]) for pos in unique_tags}
    relative_frequency_of_each_tag = {k : v / number_of_tags for k, v in number_of_each_tag.items()}
    return relative_frequency_of_each_tag



def count_words_in_blob_if_tag_meets_criteria(blob, tag_criteria_function):
    """

    """
    word_tags_that_meet_critera = [word_tag for word_tag in blob.tags if \
        tag_criteria_function(word_tag[1])]

    return len(word_tags_that_meet_critera)


def count_sentences_that_meet_criteria(blob, criteria_function):
    """Counts number of sentences in a blob that meets a criteria.

    blob - a Blob object
    criteria_function - a function that takes a Sentence object
        and returns True if the Sentence meets a criteria
    """

    count = len([s for s in blob.sentences if criteria_function(s)])
    return count



#############################################

def get_relative_frequency_of_nouns(blob):
    number_nouns_in_blob = count_words_in_blob_if_tag_meets_criteria(
        blob, is_noun)
    return float(number_nouns_in_blob) / len(blob.words)

# def get_avg_number_of_verbs_per_sentence(blob):
#     number_verbs_in_blob = count_words_in_blob_if_tag_meets_criteria(
#         blob, is_verb)
#     number_sentences_in_blob = float(len(blob.sentences))

#     return number_verbs_in_blob / number_sentences_in_blob    

def get_relative_frequency_of_verbs(blob):
    number_verbs_in_blob = count_words_in_blob_if_tag_meets_criteria(
        blob, is_verb)
    return float(number_verbs_in_blob) / len(blob.words)

def proportion_of_sentences_that_contain_past_participle(blob):
    count = count_sentences_that_meet_criteria(blob, if_sentence_contains_past_participle)
    return float(count) / len(blob.sentences)


def get_proportion_of_unique_lemmas(blob):
    lemmas = blob.words.lemmatize()
    return len(set(lemmas)) / float(len(blob.words))


def get_reflexive_count(blob):
    """TODO
    """
    pass




#############################################
### CRITERIA FUNCTIONS
#############################################

def is_noun(tag_string):
    result = True if tag_string in POS_tags.noun_tags else False
    return result

def is_verb(tag_string):
    result = True if tag_string in POS_tags.verb_tags else False
    return result

def if_sentence_contains_past_participle(sentence):
    """Returns True if the sentence contains a word that is a 
    past participle verb 

    sentence - a Sentence object
    """
    tags = [word_tag[1] for word_tag in sentence.pos_tags]
    result = True if POS_tags.past_participle_tag in tags else False
    return result


#function for finding subjunctive conjugation
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


def check_if_reflexive(word):
    pass
    
## check if verb is a particular tag


## check

class POS_tags:
    noun_tags = set(["NN", "NNS", "NNP", "NNPS"]) 
    verb_tags = set(["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"])
    past_participle_tag = "VBN"


#making lookup table for word frequency class

def make_frequency_dict(path):
    filepath = path#'germanWordList_03.csv'
    wordDict = {}
    f = open(filepath,'r')
    for line in f:
        split =  line.split(",")
        word = (split[0]).lower()
        temp = float(split[1])
        if word in wordDict:
            val = float(wordDict[word])
            if val >0:
                num = (temp*val)/(val+temp)
            else:
                num = temp
        else:
            num = temp
        wordDict[word]= num
    return wordDict

    
## scoring based on frequency class

def get_frequency_class_score_of_lemmas(blob):
    frequencies = make_frequency_dict('germanWordList_03.csv')
    lemmas = blob.words.lemmatize()
    totalFrequency = 0.0
    for lemma in lemmas:
        totalFrequency += frequencies[lemma.lower()]
        
    return float(totalFrequency/len(lemmas))

def get_frequency_class_score_unique_lemmas(blob):
    lemmaList = {}
    frequencies =  make_frequency_dict('germanWordList_03.csv')
    lemmas = blob.words.lemmatize()
    totalFrequency = 0.0
    numWords = 0
    for lemma in lemmas:
        if lemma.lower() not in lemmaList:
            lemmaList[lemma.lower()]
            totalFrequency += frequencies[lemma.lower()]
            numWords +=1
    return float(totalFrequency/numWords)

    
