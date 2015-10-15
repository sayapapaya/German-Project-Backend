import numpy as np
import user_model


def test_get_centroid():

    test_articles = np.array([
        np.array([1, 2, 3]), 
        np.array([0, 1, 2]),
        np.array([-1, 3, 4])
        ])

    user = user_model.get_centroid(test_articles)
    
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
    assert user[0] == 0.0
    assert user[1] == 2.0
    assert user[2] == 3.0    


