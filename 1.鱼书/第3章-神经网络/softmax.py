# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/4
import numpy as np

def softmax(y):
    _ = np.exp(y)
    return _ / np.sum(_)
y_1 = softmax(np.array([999,888,1200]))
print(y_1)