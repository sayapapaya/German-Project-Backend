import numpy as np
import recommend_article
import user_model
from plot_features_vs_readability import get_goethe_article_names_with_scores



goethe_directory = "goethe_articles"
article_names_with_scores = get_goethe_article_names_with_scores(goethe_directory)
goethe_article_names = article_names_with_scores.keys()

articles = np.matrix(recommend_article.create_all_feature_vectors_of_articles(
    goethe_directory, goethe_article_names))

user = user_model.get_centroid(articles)
k = 2

article_names = np.array(article_names_with_scores.keys())
recommended = recommend_article.recommend_k_articles(article_names, articles, user, k)
print recommended
