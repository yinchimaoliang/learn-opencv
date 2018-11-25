import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("lena.jpg")
px = img[100,100]#返回(100,100)号像素点信息
print(px)
blue = img[100,100,0]#返回(100,100)号像素点b值
print(blue)
img[101,101] = [255,255,255]
print(img[101,101])
print(img.shape)
print(img.size)#返回像素点数目
ball = img[50: 150,50:150]
img[100:200,100:200] = ball
r,g,b=cv2.split(img)#拆分
img=cv2.merge([r,g,b])#合并
cv2.namedWindow("image")
cv2.imshow("image",img)
b = img[:,:,0]
cv2.namedWindow("b")
cv2.imshow("b",b)
cv2.waitKey(0)

img = cv2.imread('lena.jpg')
blue = [255,0,0]
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=blue)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')

plt.show()