# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/4
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pl


x = np.arange(-10,10,0.1)
y = (x>0).astype(int)
plt.plot(x,y)
plt.show()