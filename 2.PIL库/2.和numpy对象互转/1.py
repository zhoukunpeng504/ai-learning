# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/8
from PIL import Image
import numpy as np

im = Image.open("lena.png")
im_np = np.array(im)
im = Image.fromarray(im_np)
print(im_np,im_np.shape)
im.show()