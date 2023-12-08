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
from PIL import Image

(x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True,
                                                        normalize=False)
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000,)
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000,)

print(t_train.dtype,t_train.shape,t_train[:10])