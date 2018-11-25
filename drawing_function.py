#drawing line
import cv2
import numpy as np
import time
img_line = np.zeros((255,255,3),np.int8)
cv2.line(img_line,(0,0),(260,260),(255,0,0),5)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)
cv2.imshow('image',img_line)
cv2.waitKey(0)
#cv2.destroyAllWindows()
# time.sleep(3)
#cv2.destroyAllWindows()
#drawing rectangle
#Create a black image
img_rec = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img_rec,(350,0),(500,128),(0,255,0),3)

# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image',1000,1000)#定义frame的大小
cv2.imshow('image',img_rec)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw circle
#Create a black image
img = np.zeros((512,512,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA) 
cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#定义frame的大小
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()