import numpy as np

class UserRep:

    def __init__(self, all_articles, read_articles=None, feature_vector=None):
        """
        Class to model user, tracking current representation of user in feature space
        and which articles user had read and given what ratings, as well as
        including functions to update the user rep with new user ratings.

        all_articles -- map of article names to article feature vectors
        read_articles -- map of article names to user ratings of article
        feature_vector -- current user rep in feature space

        """

        # map of article names to article feature vectors
        self.all_articles = all_articles

        # set read_articles
        if read_articles is None:
            self.read_articles = {}
        else:
            self.read_articles = read_articles

        # initialize user feature vector
        if feature_vector is None:
            self.feature_vector = self.initialize()
        else:
            self.feature_vector = feature_vector

    def get_feature_vector(self):
        """Returns the current feature vector representation of the user"""
        return self.feature_vector

    def get_read_articles(self):
        """Returns a dictionary of article names (of read articles) and 
        corresponding user ratings"""
        return self.read_articles

    def initialize(self):
        """Places the user at the centroid of all articles"""
        article_centroid = np.array(np.mean(self.all_articles.values(), axis=0)).flatten()
        return article_centroid

    def update_user(self, user_ratings):
        """
        user_ratings -- dict mapping article names to user scores
        article_dict -- dict mapping article names to article feature vectors
        S -- numpy array of scores given to the articles by the user

        mutates the user instance and returns updated feature vector for the user
        """

        # update read_articles with new ratings
        self.read_articles.update(user_ratings)

        # update user feature vector given new ratings
        user_rated_article_names = np.array(user_ratings.keys())
        user_rated_article_feature_vectors = np.array(
            [self.all_articles[article_name] for article_name in user_ratings.keys()])

        scores = np.array([user_ratings[article_name] for article_name in \
            user_rated_article_names])

        for article, S in zip(user_rated_article_feature_vectors, scores):
            self.feature_vector = update_user_given_one_article(self.feature_vector, article, S)




#########################################################
### HELPER FUNCTIONS TO UPDATE USER
#########################################################

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
        k = K(S, getCase(u_i, a_i, S))
        u_i_new = u_i + k * (u_i - a_i)
        new_user_rep.append(u_i_new)

    return np.array(new_user_rep)


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
    
