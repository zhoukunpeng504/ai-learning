# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/11/27
import time

import numpy as np
from matplotlib import pyplot as plt
x = np.arange(0,10,0.1)
y = np.sin(x)
y1 = np.cos(x)
plt.plot(x,y,label='sin')
plt.plot(x,y1,label='cos',linestyle='-.')
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()


