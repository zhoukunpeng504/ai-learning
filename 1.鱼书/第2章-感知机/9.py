# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/11/28
import numpy as np


def AND(x1, x2):
    w = np.array([0.5,0.5])
    b = -0.8
    x = np.array([x1,x2])
    res = np.sum(w*x) + b
    if res >0:
        return  1
    else:
        return 0


def NAND(x1, x2):
    w = np.array([-0.5,-0.5])
    _  = np.sum(np.array([x1, x2]) * w) + (0.8)
    if _> 0:
        return  1
    else:
        return 0


def OR(x1, x2):
    w = np.array([0.5, 0.5])
    _  = np.sum(np.array([x1,x2]) * w) + -0.4
    if _>0:
        return  1
    else:
        return 0

def XOR(x1, x2):
    _1 = NAND(x1,x2)
    _2 = OR(x1,x2)
    return AND(_1,_2)


if __name__ == '__main__':
    data = [(0,1),(0,0),(1,0),(1,1)]
    for a, b in data:
        res = XOR(a,b)
        print(a,b,res)