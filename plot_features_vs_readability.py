from extract_features import *

import os
import matplotlib.pyplot as plt



def get_goethe_article_names_with_scores(goethe_directory):
    """
    returns a dictionary mapping goethe article names (as listed in 
        the directory) to goethe scores (A1 = 0, A2 = 1, ... , C2 = 5)
    """

    # retrieve article names for specified goethe directory
    article_directory = goethe_directory
    article_names = [name for name in os.listdir(article_directory) if \
        name.endswith(".txt")]

    # retrieve 'official' scores for goethe articles
    unique_goethe_levels = sorted(list(set([a[:2] for a in article_names])))
    goethe_level_scores = {goethe_level: index for index, goethe_level in \
        enumerate(unique_goethe_levels)}
    article_scores = {article: goethe_level_scores[article[0:2]] for \
                                        article in article_names}
    return article_scores

# retrieve metric values for each article
def get_metrics_for_articles(article_directory, article_names, metric_function):
    """
    article_directory - path to the directory where articles are located
    article_names - a list of the article names in the directory 
        to compute the metric for 
    metric_function - a function that takes a blob and returns
        a numeric metric

    returns a dictionary mapping article names to corresponding numeric 
        metrics given by metric_function
    """

    article_metrics = {}
    for article_name in article_names:
        article_path = "".join([article_directory, "/", article_name])
        blob = get_blob(article_path)
        article_metrics[article_name] = metric_function(blob)
    return article_metrics



goethe_directory = "goethe_articles"
metric_function = get_avg_word_length


article_scores = get_goethe_article_names_with_scores(goethe_directory)
article_metrics = get_metrics_for_articles(goethe_directory, 
                            article_scores.keys(), metric_function)
article_names = article_scores.keys()

# plot features vs scores in scatter plot
x = np.array([article_metrics[article_name] for article_name in article_names])
y = np.array([article_scores[article_name] for article_name in article_names])

plt.scatter(x, y)


# fig = plt.figure()
# fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

# # ax = fig.add_subplot(111)
# # fig.subplots_adjust(top=0.85)
# fig.set_title('axes title')

# fig.set_xlabel('xlabel')
# fig.set_ylabel('ylabel')

plt.show()



