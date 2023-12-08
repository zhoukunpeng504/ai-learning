# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/8
# PIL中包含了九种不同模式： 1，L，P，RGB，RGBA，CMYK，YCbCr,I，F  常用的模式如下：
#
# - 1  二值图像，非黑即白
# - L  灰度图像
# - RGB 三原色
# - RGBA  在三原色的基础上增加了一个alpha通道-一般用来控制透明度
#         (0代表完全透明，像素完全不可见。 1代表完全不透明，像素完全可见)
from PIL import Image
import numpy as np


im = Image.open("lena.png")
im1 = im.convert("1")
im_np = np.array(im)
im1_np = np.array(im1)
print(im_np.shape,im1_np.shape)
im1 = Image.fromarray(im1_np)
im1.show()