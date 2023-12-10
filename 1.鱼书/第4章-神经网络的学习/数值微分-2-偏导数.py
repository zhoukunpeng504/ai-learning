# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
# y=x1**2 + x2**2对x1的偏导数和对x2的偏导数
import numpy as np

def number_diff(fun, x):
    d = 1e-4
    return (fun(x+d)-fun(x-d))/(2*d)


if __name__ == '__main__':
    func = lambda x1,x2:(x1**2+x2**2)
    # 在(3,4)处 关于x1的偏导数
    res_1 = number_diff(lambda x1:func(x1,4),3)
    # 在(3,4)处 关于x2的偏导数
    res_2 = number_diff(lambda x2: func(3, x2),4)
    print(res_1, res_2)