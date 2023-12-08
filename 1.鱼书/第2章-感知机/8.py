# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/11/28
import numpy as np


def NAND(x1, x2):
    w = np.array([-0.5,-0.5])
    _  = np.sum(np.array([x1, x2]) * w) + (0.8)
    if _> 0:
        return  1
    else:
        return 0

if __name__ == '__main__':
    data = [(0,1),(0,0),(1,0),(1,1)]
    for a, b in data:
        res = NAND(a,b)
        print(a,b,res)
    