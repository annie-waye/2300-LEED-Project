import matplotlib.pyplot as plt
import numpy as np


def primary_plot(dataframe, axis, title=None):
    """

    :param dataframe:
    :param axis:
    :param title:
    :return:
    """

    ax = dataframe[axis].plot(kind='bar')
    xtl = [item.get_text()[:10] for item in ax.get_xticklabels()]
    # _ = ax.set_xticklabels(xtl)
    plt.xticks(np.arange(0, len(dataframe[axis])), xtl, rotation=22.5)
    plt.ylabel(axis)
    plt.title(title)
    plt.tight_layout()
    plt.show()