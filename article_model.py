
import numpy as np
from textblob_de import TextBlobDE as TextBlob
from textblob_de import PatternParser
from textblob_de.lemmatizers import PatternParserLemmatizer
import nltk

from pattern.de import gender, MALE, FEMALE, NEUTRAL,parse,split
from pattern.de import conjugate, SUBJUNCTIVE, PRESENT,INFINITIVE,SG,PAST,PL

import POS


def get_blob(file_path):
    """Reads file and returns corresponding Blob object
    file_path -- path to file, file must be encoded with utf-8
    """
    f = open(file_path)
    article = f.read().decode('utf-8')
    blob = TextBlob(article, parser=PatternParser(pprint=True, lemmata=True))
    return blob


class ArticleBlob(blob):

    def __init__(self, blob):
        self.blob = blob
        self.frequency_dict_filepath = 'germanWordList_03.csv'

    def get_length_of_article(self):
        """Returns number of words in the Blob"""
        return len(self.blob.words)

    def get_length_of_longest_sentence(self):
        """Returns the number of words in the longest sentence in the Blob"""
        sentence_lengths = [len(s.words) for s in self.blob.sentences]
        return max(sentence_lengths)

    def get_avg_sentence_length(self):
        """Returns the average number of words per sentence in the Blob"""
        sentences = self.blob.sentences
        average_sentence_length = np.mean(np.array([len(sentence.words) for sentence in sentences]))
        return average_sentence_length

    def get_avg_word_length(self):
        """Returns the average number of characters in each word in the Blob"""
        words = self.blob.words
        average_word_length = np.mean(np.array([len(word) for word in words]))
        return average_word_length

    def get_relative_frequency_of_nouns(self):
        """Returns the relative frequency of nouns in the Blob"""
        number_nouns_in_blob = count_words_in_blob_if_tag_meets_criteria(
            self.blob, is_noun)
        return float(number_nouns_in_blob) / len(se;f.blob.words)

    def get_relative_frequency_of_verbs(self):
        """Returns the relative frequency of verbs in the Blob"""      
        number_verbs_in_blob = count_words_in_blob_if_tag_meets_criteria(
            self.blob, is_verb)
        return float(number_verbs_in_blob) / len(self.blob.words)

    def proportion_of_sentences_that_contain_past_participle(self):
        """Returns the proportion of sentences containing past participle"""
        count = count_sentences_that_meet_criteria(self.blob, 
            if_sentence_contains_past_participle)
        return float(count) / len(self.blob.sentences)

    def get_proportion_of_unique_lemmas(self):
        """Returns the proportion of unique lemmas among all words"""
        lemmas = self.blob.words.lemmatize()
        return len(set(lemmas)) / float(len(self.blob.words))

    def get_proportion_of_sentences_that_use_reflexive(self):
        """TODO"""
        """Returns the proportion of sentences using reflexive"""
        pass

    def get_frequency_class_score_of_lemmas(blob):
        """Returns an aggregate score of the Blob based on the frequency classes
        of all the words in the blob"""
        frequencies = make_frequency_dict(self.frequency_dict_filepath)
        lemmas = blob.words.lemmatize()
        totalFrequency = 0.0
        for lemma in lemmas:
            totalFrequency += frequencies[lemma.lower()]
        return float(totalFrequency/len(lemmas))

    def get_frequency_class_score_unique_lemmas(blob):
        """Returns an aggregate score of the Blob based on the frequency classes
        of the unique lemmas in the blob"""   
        lemmaList = {}
        frequencies = make_frequency_dict(self.frequency_dict_filepath)
        lemmas = blob.words.lemmatize()
        totalFrequency = 0.0
        numWords = 0
        for lemma in lemmas:
            if lemma.lower() not in lemmaList:
                lemmaList[lemma.lower()]
                totalFrequency += frequencies[lemma.lower()]
                numWords +=1
        return float(totalFrequency / numWords)

#############################################
### Helper functions to find relative frequencies and proportions
#############################################

def count_words_in_blob_if_tag_meets_criteria(blob, tag_criteria_function):
    """Helper function to count number of words in a blob whose tag
    satisfies a certain criteria function
    
    blob -- a Blob object
    tag_criteria_function -- takes a POS tag string and returns a boolean

    """
    word_tags_that_meet_critera = [word_tag for word_tag in blob.tags if \
        tag_criteria_function(word_tag[1])]
    return len(word_tags_that_meet_critera)


def count_sentences_that_meet_criteria(blob, criteria_function):
    """Helper function to count number of sentences in a blob that
    satisfy a certain criteria function

    blob - a Blob object
    criteria_function - takes a Sentence object and returns a boolean
    
    """
    count = len([s for s in blob.sentences if criteria_function(s)])
    return count


#############################################
### CRITERIA FUNCTIONS
#############################################

def is_noun(tag_string):
    result = True if tag_string in POS.POS_tags.noun_tags else False
    return result

def is_verb(tag_string):
    result = True if tag_string in POS.POS_tags.verb_tags else False
    return result

def if_sentence_contains_past_participle(sentence):
    """Returns True if the sentence contains a word that is a 
    past participle verb 

    sentence - a Sentence object

    """
    tags = [word_tag[1] for word_tag in sentence.pos_tags]
    result = True if POS.POS_tags.past_participle_tag in tags else False
    return result

def if_sentence_uses_reflexive(sentence):
    """Returns True if the sentence uses reflexive

    sentence - a Sentence object

    """
    raise NotImplementedError("Have not yet implemented if_sentence_uses_reflexive") 

def check_if_subjunctive(word):
    """Returns true if a word is subjuntive, False otherwise

    word -- a Blob Word object that is a verb
    TODO: must the word be a verb? Saya?
    TODO: write tests for this

    """
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

#############################################
### OTHER HELPER FUNCTIONS
#############################################

def make_frequency_dict(path):
    """Helper function to help with get_frequency_class_score functions

    path -- path to a file that maps words to their corresponding
        frequency class 
    Returns a lookup table for word frequency class

    """
    filepath = path#'germanWordList_03.csv'
    wordDict = {}
    f = open(filepath,'r')
    for line in f:
        split =  line.split(",")
        word = (split[0]).lower()
        temp = float(split[1])
        if word in wordDict:
            val = float(wordDict[word])
            if val > 0:
                num = (temp * val) / (val + temp)
            else:
                num = temp
        else:
            num = temp
        wordDict[word]= num
    return wordDict





################ OUTDATED ####################

# count number of words with each part of speech tag
# uses only Penn Treebank tags
# def get_relative_frequency_of_pos_tags(blob):
#     """
#     """
#     tags = blob.tags
#     number_of_tags = float(len(tags))
#     unique_tags = set([t[1] for t in tags])
#     number_of_each_tag = {pos: sum([1 for t in tags if t[1] == pos]) for pos in unique_tags}
#     relative_frequency_of_each_tag = {k : v / number_of_tags for k, v in number_of_each_tag.items()}
#     return relative_frequency_of_each_tag


# def get_avg_number_of_verbs_per_sentence(blob):
#     number_verbs_in_blob = count_words_in_blob_if_tag_meets_criteria(
#         blob, is_verb)
#     number_sentences_in_blob = float(len(blob.sentences))

#     return number_verbs_in_blob / number_sentences_in_blob    




