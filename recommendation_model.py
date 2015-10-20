
import article_model
import numpy as np
from sklearn.neighbors import NearestNeighbors

from plot_features_vs_readability import get_goethe_article_names_with_scores


## TODO: UPDATE TO REFLECT WHICH FEATURES SHOW GOOD CORRELATION
def create_feature_vector(article_blob):
    """
    article_blob -- an instance of the class ArticleBlob
    """
    feature_vector = np.array([
        article_blob.get_length_of_longest_sentence(),
        article_blob.get_avg_sentence_length(),
        article_blob.get_avg_word_length(),
        article_blob.proportion_of_sentences_that_contain_past_participle()
    ])
    return feature_vector

def create_feature_vector_dict(article_directory, article_names):
    """
    article_directory -- string path to directory containing articles
    article_names -- list of string names of articles in article directory
    
    return dictionary mapping article names to feature vectors
    """
    article_name_to_feature_vectors = {}

    for article_name in article_names:
        article_path = "".join([article_directory, "/", article_name])
        article_blob = article_model.ArticleBlob(article_model.get_blob(article_path)
        article_name_to_feature_vectors[article_name] = create_feature_vector(article_blob)
    
    return article_name_to_feature_vectors


def find_k_nearest_articles(article_names, articles, user, k):
    """Finds the k articles closest to the user

    article_names -- numpy array of article names
    articles -- numpy matrix where rows are feature vectors representing articles
    user -- numpy feature vector representing user (in same space as articles)
    k -- number of articles to recommend
    
    returns the names of the k articles closest to the user
    """
    nbrs = NearestNeighbors(n_neighbors=k).fit(articles)
    distances, indices = nbrs.kneighbors(user)
    nearest_articles = article_names[indices]
    return nearest_articles



    