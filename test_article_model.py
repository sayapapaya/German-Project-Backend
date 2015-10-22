import os
import numpy as np

import article_model

def read_articles_in_directory(article_directory):
    article_names = [name for name in os.listdir(article_directory) if \
            name.endswith(".txt")]

    article_dict = article_model.create_feature_vector_dict(
        article_directory, article_names, article_model.create_feature_vector)

    return article_dict

article_directory = "goethe_articles"

def test_normalize_feature_vectors():
    article_dict = {
        "A": np.array([0, 10, 100]),
        "B": np.array([1, 11, 101]),
        "C": np.array([2, 12, 102]),
    }
    normalized = article_model.normalize_feature_vectors(article_dict)

    expected_A = np.array([0.0, 0.0, 0.0])
    expected_B = np.array([0.5, 0.5, 0.5])
    expected_C = np.array([1.0, 1.0, 1.0])

    assert(all(x in normalized["A"] for x in expected_A))
    assert(all(x in normalized["B"] for x in expected_B))
    assert(all(x in normalized["C"] for x in expected_C))
