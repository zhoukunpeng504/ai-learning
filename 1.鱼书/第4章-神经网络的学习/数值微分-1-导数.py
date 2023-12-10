# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
import numpy as np


def number_diff(fun, x):
    d = 1e-4
    return (fun(x+d)-fun(x-d))/(2*d)


if __name__ == '__main__':
    fun = lambda x:(0.01*x**2 + 0.1*x)
    res = number_diff(fun,np.array([1,2,3])) # 求函数在 1  2 3 这三处的导数
    print(res)