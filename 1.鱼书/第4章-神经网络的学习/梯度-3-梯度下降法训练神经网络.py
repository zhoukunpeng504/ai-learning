# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/9
# 梯度下降法，训练神经网络
import numpy as np
cp = None
try:
    import cupy as cp
except:
    pass

import os
current_dir = os.path.dirname(__file__)
current_dir = os.path.abspath(current_dir)
import sys
sys.path.append(os.path.join(current_dir, 'dataset'))
import mnist


def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y


def number_grad(func, x:np.ndarray):
    # 支持多维数组的梯度计算函数
    grad = np.zeros_like(x)
    d = 1e-4
    if x.ndim >1:
        for index_i,i in enumerate(x):
            for index_j,j in enumerate(i):
                temp =x[index_i][index_j]
                x[index_i][index_j] = temp +d
                _x = func(x)
                x[index_i][index_j] = temp - d
                _y = func(x)
                grad[index_i,index_j] = (_x-_y)/(2*d)
                x[index_i][index_j] = temp
    else:
        for i in range(x.size):
            temp = x[i]
            x[i] = temp + d
            _a = func(x)
            x[i] = temp - d
            _b = func(x)
            x[i] = temp
            grad[i] = (_a - _b) / (2 * d)
    return grad


def softmax(y):
    y = y - np.max(y)
    _ = np.exp(y)
    return _ / np.sum(_)


def cross_entropy_error(y:np.ndarray, t:np.ndarray):
    # mini-batch版本交叉熵误差函数
    if y.ndim == 1:
        y = y.reshape(1,y.shape[0])
        t = t.reshape(1,t.shape[0])
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))/y.shape[0]


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x, params=None):
        _params = params or self.params
        W1, W2 = _params['W1'], _params['W2']
        b1, b2 = _params['b1'], _params['b2']
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        return y

    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        grads = {}
        grads['W1'] = number_grad(loss_W, self.params['W1'])
        grads['b1'] = number_grad(loss_W, self.params['b1'])
        grads['W2'] = number_grad(loss_W, self.params['W2'])
        grads['b2'] = number_grad(loss_W, self.params['b2'])
        return grads


if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, one_hot_label = True)
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    iters_num = 10000
    batch_size = 100
    learning_rate = 0.1
    train_loss_list = []
    for i in range(10000):
        data_index = np.random.choice(x_train.shape[0],batch_size)
        x_batch = x_train[data_index]
        t_batch = t_train[data_index]
        grad = net.numerical_gradient(x_batch, t_batch)
        for key in ('W1', 'b1', 'W2', 'b2'):
            net.params[key] -= learning_rate * grad[key]
        loss = net.loss(x_batch, t_batch)
        train_loss_list.append(loss)
        print(loss)
