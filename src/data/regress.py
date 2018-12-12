import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model


def lin_reg(ctrain_x, ctest_x, ctrain_y, ctest_y):
    """
    Linear Regression
    :param ctrain_x: trainning data x
    :param ctest_x: test data x
    :param ctrain_y: trainning data y
    :param ctest_y: test data y
    :return: Visual
    """
    reg = linear_model.LinearRegression()   # Linear Regression
    reg.fit(ctrain_x, ctrain_y)             # fit linear model

    cpred_y = reg.predict(ctest_x)          # predict with linear model

    plt.scatter(ctest_x, ctest_y, color='black')            # scatter plot test x vs test y, black markers
    plt.plot(ctest_x, cpred_y, color='red', linewidth=3)    # plot line test x vs predict y, red line

    plt.xticks((np.arange(min(ctest_x)-1, max(ctest_x) + 1, 15.0)))     # tick marks increment by 15
    plt.yticks((np.arange(min(ctest_x)-1, max(ctest_y) + 1, 1.0)))      # tick marks increment by 1

    plt.xlabel('X Axis', fontsize=14)               # Label the x axis
    plt.ylabel('Y Axis', fontsize=14)               # Label the y axis

    plt.show()