# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/4
import numpy as np

def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

x = np.array([1.0,0.5]) # 输入
# 第一层
w1= np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b1 = np.array([0.1,0.2,0.3])
z1 = sigmoid(x@w1 + b1)
print(z1, z1.shape)
# 第二层
w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
z2 = sigmoid(z1@w2+b2)
# 第三层
w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])
y = z3 = z2@w3 + b3
print(y)