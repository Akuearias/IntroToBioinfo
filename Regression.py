from math import dist

import vel as vel
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np


iris = load_iris()
iris_title = list(iris.keys())
iris_data = list(iris.values())
iris_num_info = iris_data[0]
reg_database = []
for info in iris_num_info:
    reg_database.append(info[0:2])

reg_database = np.array(reg_database)
reg_database_col1, reg_database_col2 = [], []

for i in reg_database:
    reg_database_col1.append(i[0])
    reg_database_col2.append(i[1])

reg_database_col1 = np.array(reg_database_col1)
reg_database_col2 = np.array(reg_database_col2)

slope, intercept = np.polyfit(reg_database_col1, reg_database_col2, 1)

reg_predict = slope * reg_database_col1 + intercept

# Plot the data and the fit
fig, ax = plt.subplots()
ax.plot(reg_database_col1, reg_database_col2, marker = 'o', ls = '', markersize = 0.5, label = 'Data')
ax.plot(reg_database_col1, reg_predict, color = 'firebrick', label = 'Fit')
ax.set(xlabel = 'X', ylabel = 'Y', title = 'QWERTY')
ax.legend()
ax.grid(color = 'lightgray', alpha = 0.7)
plt.show()
