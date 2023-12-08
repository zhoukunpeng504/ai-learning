# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/4
import numpy
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20.0,20.0,0.01)
y = np.array([i if i>0 else 0   for i in x])
print(y)
plt.plot(x,y)
plt.show()