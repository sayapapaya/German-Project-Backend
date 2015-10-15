import numpy as np

### function: K() is to get a gain as some function of the score
### @param S - score assigned by user for some article {1,2,3,4,5}
## @ param case

def K(S, case):
    k = 0
    if case == 1:
        if S > 3:
            k = 0
        elif S == 3:
            k = 0.5 
        elif S ==2:
            k = 0.7
        elif S == 1:
            k = 0.9
    elif case == 2:
        if S<3:
            k =0
        elif S ==3:
            k = 0.5
        elif S ==4:
            k = 0.7
        elif S == 5:
            k = 0.9
        
    return k # currently case 2 just returns 0, which means that if a == u
                #then the model wont change



def getCase(u, a, S):
    """Helper function to determine which direction to nudge the user in.
    
    u -- user feature value along a specific dimension
    a -- article feature value along a specific dimension
    S -- score user gave to article

    returns 0, 1, or 2 to be used in function K(S, case)
    """
    if u == a:
        return 0
    elif u > a:
        return 1
    elif u < a:
        return 2
    
def update_user_in_one_dimension(u, a, S):
    """Nudges the user along one dimension given an article score

    u -- current user value along the dimension
    a -- article value along dimension
    S -- score given to the article by the user

    returns updated value for user along dimension
    """

    k = K(S, getCase(u, a, S))
    u = u + k * (u - a)
    return u


def update_user_given_one_article(user, article, S):
    """
    user -- numpy feature vector representing user (in same space as article)
    article -- numpy feature vector representing article
    S -- score given to the article by the user

    returns updated feature vector for the user
    """

    # ensure that article is also represented as 1D array, not 1d matrix
    article = np.reshape(article, user.shape)

    new_user_rep = []
    for u_i, a_i in zip(user, article):
        new_user_rep.append(update_user_in_one_dimension(u_i, a_i, S))

    return np.array(new_user_rep)

def update_user_given_many_articles(user_ratings, article_dict, user):
    """
    user_ratings -- dict mapping article names to user scores
    article_dict -- dict mapping article names to article feature vectors
    S -- numpy array of scores given to the articles by the user

    returns updated feature vector for the user
    """
    user_rated_article_names = np.array(user_ratings.keys())
    user_rated_article_feature_vectors = np.array(
        [article_dict[article_name] for article_name in user_ratings.keys()])

    scores = np.array([user_ratings[article_name] for article_name in \
        user_rated_article_names])

    for article, S in zip(user_rated_article_feature_vectors, scores):
        updated_user = update_user_given_one_article(user, article, S)

    return updated_user



def get_centroid(articles):
    """ """
    article_centroid = np.array(np.mean(articles, axis=0)).flatten()
    return article_centroid


### Test code below before using ###

#param articles is a nxm matrix with m is the number of features n is number of articles
#param scores is a row vector of scores for each article
# def create_user_model(articles,scores):
#     numFeatures = articles.shape[1] 
#     numArticles = articles.shape[0]
#     userModel = initialize(articles)
#     for i in range(0,numArticles):
#         article = np.array(articles[i,:]) #row vector corresponding to article features
#         for j in range(0,numFeatures):
#             u = userModel[j]
#             a = article[j]
#             S = scores[j]
#             u_new = update(u,a,S)

#             userModel[j] = u_new
    
#     return userModel

# Code below seems to find avg value for each vector instead?
#initializes the user vector (currently by using centroid of all the articles)
def initialize(articles):
    numFeatures = articles.shape[1] 
    numArticles = articles.shape[0]
    initialModel = np.zeros(numFeatures)
    for j in range(0,numFeatures):
        featureScore = np.mean(articles[j][:])
        initialModel[j] = featureScore
    return initialModel

