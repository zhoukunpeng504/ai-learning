# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
# 损失函数的实现：
# 均方误差
# 交叉熵误差
import numpy
import numpy as np


def mean_square_error(y:numpy.ndarray, t:numpy.ndarray):
    return 0.5 * np.sum((y-t)**2)  # 也可以写成 np.square的形式


if __name__ == '__main__':
    y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]) # softmax的输出形式数据
    t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) # one-hot形式数据
    res = mean_square_error(y,t)
    print(res)