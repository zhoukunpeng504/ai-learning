# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
# y=x1**2 + x2**2 在某点的梯度
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

def grad_dec(fun, init_x:np.ndarray, lr=0.001, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = number_grad(fun, x)
        x -= lr*grad
    return x

if __name__ == '__main__':
    func = lambda x:(x[0]**2+x[1]**2)
    res = grad_dec(func, np.array([-3.0, 4.0]), 10, 100)
    print(res)