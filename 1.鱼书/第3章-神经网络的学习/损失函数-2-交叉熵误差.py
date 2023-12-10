# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
# 损失函数的实现：
# 均方误差
# 交叉熵误差
import numpy
import numpy as np


def cross_entropy_error(y:numpy.ndarray, t:numpy.ndarray):
    # 交叉熵误差函数
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))


if __name__ == '__main__':
    y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
    t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    res = cross_entropy_error(y,t)
    print(res)