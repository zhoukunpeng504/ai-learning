# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/4
import numpy as np

def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

def get_network()->dict:
    network = {}
    w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b1 = np.array([0.1, 0.2, 0.3])
    w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    b2 = np.array([0.1, 0.2])
    w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    b3 = np.array([0.1, 0.2])
    network["w1"] = w1
    network['b1'] = b1
    network['w2'] = w2
    network['b2'] = b2
    network['w3'] = w3
    network['b3'] = b3
    return network

def forward(x, network):
    w1,w2,w3 = network['w1'], network['w2'], network['w3']
    b1,b2,b3 = network['b1'], network['b2'], network['b3']
    # 第一层
    z1 = sigmoid(x @ w1 + b1)
    # 第二层
    z2 = sigmoid(z1 @ w2 + b2)
    # 第三层
    y = z3 = z2 @ w3 + b3
    return y

x = np.array([1.0,0.5]) # 输入
net = get_network()
y = forward(x,net)
print(y)