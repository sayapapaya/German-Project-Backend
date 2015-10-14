
import extract_features
import numpy as np

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
    """
    feature_vectors = []

    for article_name in article_names:
        article_path = "".join([article_directory, "/", article_name])
        blob = extract_features.get_blob(article_path)
        feature_vectors.append(create_feature_vector(blob))
    
    return np.array(feature_vectors)


def get_centroid(articles):
    """ """
    article_centroid = np.mean(articles, axis=0)
    return article_centroid

git


# goethe_directory = "goethe_articles"
# article_names_with_scores = get_goethe_article_names_with_scores(goethe_directory)
# goethe_article_names = article_names_with_scores.keys()

# articles = create_all_feature_vectors_of_articles(goethe_directory, goethe_article_names)