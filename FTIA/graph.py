"""Programa para la realización de la gráfica usada para la tarea 3 de FTIA"""

import pandas as pd
import matplotlib.pyplot as plt

"""import numpy as np
from scipy.interpolate import interp1d"""

data = pd.read_csv('experimentos.dat', header=0, delim_whitespace=True)
X = data.iloc[:, 0]
A = data.iloc[:, 1]
B = data.iloc[:, 2]
C = data.iloc[:, 3]
D = data.iloc[:, 4]
E = data.iloc[:, 5]
F = data.iloc[:, 6]
plt.plot(X, A, 'ro')
plt.plot(X, B, 'xb')
plt.show()
print(data)