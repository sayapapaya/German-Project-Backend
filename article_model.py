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
    
    normalized_article_dict = normalize_feature_vectors(article_name_to_feature_vectors)
    return normalized_article_dict


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

############################################################################
### HELPER FUNCTIONS
############################################################################

def normalize_feature_vectors(article_dict):
    """Normalizes article feature vectors, such that the values 
    along each dimension are comparable

    Note that normalization is across dimensions, not for 
    individual feature vectors

    """
    article_names = np.array(article_dict.keys())
    article_fvs = np.array([article_dict[n] for n in article_names])
    
    num_dimensions = len(article_fvs[0])
    
    # find min/max along each dimension
    minima = [min([fv[i] for fv in article_fvs]) for i in range(num_dimensions)]
    maxima = [max([fv[i] for fv in article_fvs]) for i in range(num_dimensions)]

    # normalize each fv
    new_article_fvs = []
    for fv in article_fvs:
        new_fv = np.array([normalize(fv[i], minima[i], maxima[i]) for \
            i in range(num_dimensions)])
        new_article_fvs.append(new_fv)

    normalized_article_dict = {k : v for k,v in zip(article_names, new_article_fvs)}
    return normalized_article_dict

def normalize(val, minimum, maximum):
    """ """
    return float(val - minimum) / (maximum - minimum)




    


