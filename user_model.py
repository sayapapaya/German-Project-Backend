import numpy as np

### function: K() is to get a gain as some function of the score
### @param S - score assigned by user for some article {1,2,3,4,5}
## @ param case

def K(S,case):
    k = 0
    if case ==1:
        if S>3:
            k =0
        elif S ==3:
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



# funciton : getCase is to figure out which direction we want to nudge the user
def getCase(u,a,S):
    if u==a:
        return 0
    elif u > a:
        return 1
    elif u < a:
        return 2
    
#updates the user in some direction
def update(u,a,S):
    k = K(S,getCase)
    u = u +k*(u-a)
    return u

#initializes the user vector (currently by using centroid of all the articles)
def initialize(articles):
    numFeatures = articles.shape[1] 
    numArticles = articles.shape[0]
    initialModel = np.zeros(numFeatures)
    for j in range(0,numFeatures):
        featureScore = np.mean(articles[j][:])
        initialModel[j] = featureScore
    return initialModel


#param articles is a nxm matrix with m is the number of features n is number of articles
#param scores is a row vector of scores for each article
def create_user_model(articles,scores):
    numFeatures = articles.shape[1] 
    numArticles = articles.shape[0]
    userModel = initialize(numFeatures)
    for i in range(0,numArticles):
        article = articles[:,i] #row vector corresponding to article features
        for j in range(0,numFeatures):
            u = userModel[j]
            a = article[j]
            S = scores[j]
            u_new = update(u,a,S)
            userModel[j] = u_new
    
    return userModel
    
    
