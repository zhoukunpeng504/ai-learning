# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
import numpy
import numpy as np


def cross_entropy_error(y:numpy.ndarray, t:numpy.ndarray):
    # mini-batch版本交叉熵误差函数
    if y.ndim == 1:
        y = y.reshape(1,y.shape[0])
        t = t.reshape(1,t.shape[0])
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))/y.shape[0]

def mean_square_error(y:numpy.ndarray, t:numpy.ndarray):
    if y.ndim == 1:
        y = y.reshape(1,y.shape[0])
        t = t.reshape(1,t.shape[0])
    return 0.5 * np.sum((y-t)**2)/y.shape[0]


if __name__ == '__main__':
    y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
    t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    res = cross_entropy_error(y,t)
    res_1 = mean_square_error(y,t)
    print(res, res_1)