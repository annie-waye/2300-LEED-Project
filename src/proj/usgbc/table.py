import matplotlib.pyplot as plt
import math

def show(dataframe):

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)

    ax.set_title('LEED Buildings by City')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    lbls = ('City', 'Count')

    cells = dataframe.values[:10]
    tab = ax.table(cellText=cells, colWidths=[.25, .25],
                   colLabels=lbls, loc='center')
    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    tab.scale(1, 1)

    fig.tight_layout()
    plt.show()
    pass
