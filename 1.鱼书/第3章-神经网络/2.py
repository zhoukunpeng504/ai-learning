# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/4
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20.0,20.0,0.1)
def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y
y = sigmoid(x)
plt.plot(x,y)
plt.show()