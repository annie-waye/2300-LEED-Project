import matplotlib.pyplot as plt
import numpy as np


def primary_plot(df, axis, title=None, rotation_angle=0):
    """

    :param dataframe:
    :param axis:
    :param title:
    :return:
    """
    # nelements = len(dataframe[axis]) if len(axis) == 1 else len(dataframe[axis[0]])
    ax = df[axis].plot(kind='bar')
    xtl = [item.get_text()[:10] for item in ax.get_xticklabels()]
    # _ = ax.set_xticklabels(xtl)
    plt.xticks(np.arange(0, len(df)), xtl, rotation=rotation_angle)
    plt.legend(axis)
    # plt.ylabel(axis)
    plt.title(title)
    plt.tight_layout()
