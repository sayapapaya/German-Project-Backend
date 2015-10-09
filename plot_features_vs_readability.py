from extract_features import *

import os
import matplotlib.pyplot as plt



goethe_directory = "goethe_articles"

# retrieve article names for specified goethe directory
article_directory = goethe_directory
article_names = [name for name in os.listdir(article_directory) if name.endswith(".txt")]

# retrieve 'official' scores for goethe articles
unique_goethe_levels = sorted(list(set([a[:2] for a in article_names])))
goethe_level_scores = {goethe_level: index for index, goethe_level in \
    enumerate(unique_goethe_levels)}
article_scores = {article: goethe_level_scores[article[0:2]] for \
                                    article in article_names}

# retrieve metric values for each article
article_metrics = {}
for article_name in article_names:
    article_path = "".join([article_directory, "/", article_name])
    blob = get_blob(article_path)
    article_metrics[article_name] = get_length_of_article(blob)


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



