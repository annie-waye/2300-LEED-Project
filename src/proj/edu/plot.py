import matplotlib.pyplot as plt


def show(dataframe):
    x = dataframe['Years'].values
    y = dataframe['Percentage'].values

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(x, y, color='red', linewidth=2)

    ax.set_title('Massachusetts Student Population')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage Change')
    ax.set_ybound(-3.5, 3.5)

    plt.show()
    pass
