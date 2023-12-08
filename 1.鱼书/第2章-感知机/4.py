# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/11/28

def NAND(x1, x2):
    _  = x1 * -0.5 + x2*-0.5
    if _>-0.8:
        return  1
    else:
        return 0

if __name__ == '__main__':
    data = [(0,1),(0,0),(1,0),(1,1)]
    for a, b in data:
        res = NAND(a,b)
        print(a,b,res)
    