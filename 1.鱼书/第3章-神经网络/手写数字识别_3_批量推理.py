# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/8
import os
import sys
current_dir = os.path.dirname(__file__)
current_dir = os.path.abspath(current_dir)
sys.path.append(current_dir)
import numpy as np
from dataset import mnist
import pickle


def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

def softmax(y):
    y = y - np.max(y)
    _ = np.exp(y)
    return _ / np.sum(_)

def get_data():
    (x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True,
                                                            normalize=True) # 有助于提高经度
    return x_test,t_test


def get_net():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
        return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

if __name__ == '__main__':
    x_test,t_test = get_data()
    net = get_net()
    right = 0
    batch_size = 100
    for i in range(0, len(x_test), batch_size):
        res = predict(net, x_test[i:i + batch_size])
        res = np.argmax(res, axis=1)
        right += np.sum(res == t_test[i:i+batch_size])
    print(right/len(x_test))

