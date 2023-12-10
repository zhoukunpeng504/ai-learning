# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
# y=x1**2 + x2**2对x1的偏导数和对x2的偏导数
# 本实现只兼容 一维数组
import numpy as np

def number_grad(fun, x:np.ndarray):
    d = 1e-4
    grad = np.zeros_like(x)
    for i in range(x.size):
        temp = x[i]
        x[i] = temp+d
        _a = fun(x)
        x[i] = temp-d
        _b = fun(x)
        x[i] = temp
        grad[i] = (_a-_b)/(2*d)
    return grad


if __name__ == '__main__':
    func = lambda x:(x[0]**2+x[1]**2)
    res = number_grad(func, np.array([1.0,2.0]))
    print(res)