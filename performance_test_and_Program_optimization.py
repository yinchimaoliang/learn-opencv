import cv2
import numpy as np
cv2.setUseOptimized(False)
img1 = cv2.imread('lena.jpg')

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)