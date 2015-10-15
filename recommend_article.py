
import extract_features
import numpy as np
from sklearn.neighbors import NearestNeighbors

from plot_features_vs_readability import get_goethe_article_names_with_scores




## TODO: UPDATE TO REFLECT WHICH FEATURES SHOW GOOD CORRELATION
def create_feature_vector(blob):
    """
    """
    feature_vector = np.array([
        extract_features.get_length_of_article(blob),
        extract_features.get_length_of_longest_sentence(blob),
        extract_features.get_avg_sentence_length(blob),
        extract_features.get_avg_word_length(blob),
        extract_features.get_relative_frequency_of_nouns(blob),
        extract_features.get_relative_frequency_of_verbs(blob),
        extract_features.proportion_of_sentences_that_contain_past_participle(blob)
    ])

    return feature_vector


def create_all_feature_vectors_of_articles(article_directory, article_names):
    """
    article_directory -- string path to directory containing articles
    article_names -- list of string names of articles in article directory
    
    return numpy array containing feature vectors in same order as
        articles appear in article_names
    """
    feature_vectors = []

    for article_name in article_names:
        article_path = "".join([article_directory, "/", article_name])
        blob = extract_features.get_blob(article_path)
        feature_vectors.append(create_feature_vector(blob))
    
    return np.array(feature_vectors)


def recommend_k_articles(article_names, articles, user, k):
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
    