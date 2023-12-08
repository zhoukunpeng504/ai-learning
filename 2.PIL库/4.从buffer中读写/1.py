# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/12/8
import io
from PIL import Image

buffer = io.BytesIO()
buffer.name = "xxx.png"
with open("lena.png","rb") as f:
    buffer.write(f.read())
im = Image.open(buffer)
im.show()
buffer_w = io.BytesIO()
buffer_w.name = "out.jpg"
im.save(buffer_w)
with open("out.jpg", "wb") as f:
    f.write(buffer_w.getvalue())