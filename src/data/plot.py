import pandas as pd
import matplotlib.pyplot as plt

def primary_plot(dataframe, axis):
    ax = dataframe[axis].plot(kind='bar')
    xtl = [item.get_text()[:10] for item in ax.get_xticklabels()]
    _ = ax.set_xticklabels(xtl)
    plt.tight_layout()
    plt.show()