import matplotlib.pyplot as plt
from sklearn import linear_model


def lin_reg(train_x, test_x, train_y, test_y):
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
    test_data = dataframe[dataframe.index % 5 != 0]
    return test_data


def train(dataframe):
    train_data = dataframe[dataframe.index % 5 == 0]
    return train_data


def axes(dataframe, feature):
    x = dataframe.index.values.reshape(-1, 1)
    y = dataframe[feature].values.reshape(-1, 1)
    xy = [x, y]
    return xy
