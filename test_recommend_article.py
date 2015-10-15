import numpy as np
import recommend_article
import user_model
from plot_features_vs_readability import get_goethe_article_names_with_scores


def test_get_centroid():

    test_articles = np.array([
        np.array([1, 2, 3]), 
        np.array([0, 1, 2]),
        np.array([-1, 3, 4])
        ])

    user = recommend_article.get_centroid(test_articles)
    
    assert user[0] == 0.0
    assert user[1] == 2.0
    assert user[2] == 3.0


def test_initialize():

    test_articles = np.array([
        np.array([1, 2, 3]), 
        np.array([0, 1, 2]),
        np.array([-1, 3, 4])
        ])

    user = user_model.initialize(test_articles)
    print user
    assert user[0] == 0.0
    assert user[1] == 2.0
    assert user[2] == 3.0    



# goethe_directory = "goethe_articles"
# article_names_with_scores = get_goethe_article_names_with_scores(goethe_directory)
# goethe_article_names = article_names_with_scores.keys()

# articles = np.matrix(recommend_article.create_all_feature_vectors_of_articles(
#     goethe_directory, goethe_article_names))

# user = user_model.get_centroid(articles)
# k = 2

# article_names = np.array(article_names_with_scores.keys())
# recommended = recommend_article.recommend_k_articles(article_names, articles, user, k)
