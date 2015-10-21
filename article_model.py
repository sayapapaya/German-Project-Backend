import numpy as np

import article_blob


def create_feature_vector_dict(article_directory, article_names, 
    create_feature_vector_function):
    """
    article_directory -- string path to directory containing articles
    article_names -- list of string names of articles in article directory
    
    return dictionary mapping article names to feature vectors
    """
    article_name_to_feature_vectors = {}

    for article_name in article_names:
        article_path = "".join([article_directory, "/", article_name])
        an_article_blob = article_blob.ArticleBlob(article_blob.get_blob(article_path))
        article_name_to_feature_vectors[article_name] = create_feature_vector_function(an_article_blob)
    
    return article_name_to_feature_vectors


############################################################################
### CREATE_FEATURE_VECTOR FUNCTIONS
############################################################################

def create_feature_vector(an_article_blob):
    """
    an_article_blob -- an instance of the class ArticleBlob
    """
    feature_vector = np.array([
        an_article_blob.get_length_of_longest_sentence(),
        an_article_blob.get_avg_sentence_length(),
        an_article_blob.get_avg_word_length(),
        an_article_blob.proportion_of_sentences_that_contain_past_participle()
    ])
    return feature_vector