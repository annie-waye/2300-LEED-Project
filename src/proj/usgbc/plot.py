import matplotlib.pyplot as plt
import numpy as np


def show(dataframe):
    x = dataframe['Date'].values
    y1 = dataframe['Construction'].values
    y2 = dataframe['Validation'].values
    y3 = dataframe['Certification'].values

    fig = plt.figure()

    ax = plt.subplot(2, 2, 1)
    ax.set_title('Mean Construction by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    plt.plot(x, y1)

    ax = plt.subplot(2, 2, 2)
    ax.set_title('Mean Validation by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.set_ylim([-.2, 6.2])
    plt.plot(x, y2)

    ax = plt.subplot(2, 2, 3)
    ax.set_title('Mean Certification by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    plt.plot(x, y3)

    fig.tight_layout()
    plt.show()

    pass


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
