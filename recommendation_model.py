import numpy as np

from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier



def recommend_k_articles(all_articles, user, k, recommendation_function):
    """Recommends k articles from all_articles that the user has not yet read
    applying the recommendation function
    Note that there must be at least k articles in all_articles that the
    user has not yet read

    all_articles -- a dict of article names to article feature vectors
    user -- a UserRep instance
    k -- an int, the number of articles to recommend
    recommendation_function(user_feature_vector, list_of_article_names, 
        list_of_corresponding_article_feature_vectors, k) -- returns names
        of articles to recommend

    Returns names of k recommended articles
    """
    read_articles = user.get_read_articles().keys()
    unread_article_dict = {k:v for k,v in all_articles.items() if k not in read_articles}
    user_fv = user.get_feature_vector()
    unread_article_names = np.array(unread_article_dict.keys())
    unread_article_fvs = np.array([unread_article_dict[n] for n in unread_article_names])
    
    recommended_article_names = recommendation_function(
        user_fv, unread_article_names, unread_article_fvs, k)

    return recommended_article_names


def knn_classification_based_on_read_articles(all_articles, user_ratings, k):
    """
    all_articles -- a dict of article names to article feature vectors
    user_ratings -- a dict of article names to user ratings
    k -- the number of neighbors to base the k-nearest-neighbors classification on

    Returns a dictionary of article names to predicted user ratings
        where existing user ratings of articles override any prediction
    """

    neigh = KNeighborsClassifier(n_neighbors=k)
    
    read_article_names = user_ratings.keys()
    read_article_fvs = np.array([all_articles[n] for n in read_article_names])
    article_labels = np.array([user_ratings[n] for n in read_article_names])

    neigh.fit(read_article_fvs, article_labels)

    classified_articles = {k : neigh.predict(v)[0] for k,v in all_articles.items()}
    classified_articles.update(user_ratings)
    
    return classified_articles


############################################################################
### RECOMMENDATION FUNCTIONS
############################################################################

def find_k_nearest_articles(user_fv, article_names, article_fvs, k):
    """Finds the k articles closest to the user

    article_names -- numpy array of article names
    articles -- numpy matrix where rows are feature vectors representing articles
    user -- numpy feature vector representing user (in same space as articles)
    k -- number of articles to recommend
    
    returns the names of the k articles closest to the user
    """
    nbrs = NearestNeighbors(n_neighbors=k).fit(article_fvs)
    distances, indices = nbrs.kneighbors(user_fv)
    nearest_articles = article_names[indices]
    return nearest_articles
    


    