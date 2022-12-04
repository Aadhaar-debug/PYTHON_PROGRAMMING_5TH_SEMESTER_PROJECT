# this module is used to plot the mean score of each game in a bar graph.

import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores):
    
    # it will start by displaying an empty figure on screen using display().
    # and next it clears any output that was previously displayed on screen using clear_output(wait=True).
    
    display.clear_output(wait=True)
    
    # Then it displays a new figure called gcf() which stands for graphics context frame.
    
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
