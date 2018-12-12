import matplotlib.pyplot as plt
from sklearn import datasets, linear_model


def lin_reg(ctrain_x, ctest_x, ctrain_y, ctest_y):
    reg = linear_model.LinearRegression()
    reg.fit(ctrain_x, ctrain_y)

    cpred_y = reg.predict(ctest_x)

    plt.scatter(ctest_x, ctest_y, color='black')
    plt.plot(ctest_x, cpred_y, color='red', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()