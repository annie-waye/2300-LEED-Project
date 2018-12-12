'''
Testing script
'''

import numpy as np
from sklearn import datasets

dia = datasets.load_diabetes()
dia_x = dia.data[:, np.newaxis, 2]

print(dia_x)