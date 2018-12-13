import matplotlib.pyplot as plt
from sklearn import linear_model


def lin_reg(train_x, test_x, train_y, test_y):
    """

    :param train_x: tranning data for x
    :param test_x:  testing data for x
    :param train_y: tranning data for y
    :param test_y: testing data for y
    :return: plotted
    """
    reg = linear_model.LinearRegression()
    reg.fit(train_x, train_y)

    pred_y = reg.predict(test_x)

    plt.scatter(test_x, test_y, color='black')
    plt.plot(test_x, pred_y, color='red', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()
    pass


def test(dataframe):
    """

    :param dataframe: desired data
    :return: chosen test data
    """
    test_data = dataframe[dataframe.index % 5 != 0]
    return test_data


def train(dataframe):
    """

    :param dataframe: desired data
    :return: chosen train data
    """
    train_data = dataframe[dataframe.index % 5 == 0]
    return train_data


def axes(dataframe, feature):
    """

    :param dataframe: desired data
    :param feature: select feature
    :return:
    """
    x = dataframe.index.values.reshape(-1, 1)
    y = dataframe[feature].values.reshape(-1, 1)
    xy = [x, y]
    return xy
