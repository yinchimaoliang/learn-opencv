import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# #
# # while(1):
# #     #获取每一帧
# #     ret,frame = cap.read()
# #     #转换到HSV
# #     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# #     #设定蓝色的阀值
# #     lower_blue = np.array([110,50,255])
# #     upper_blue = np.array([130,255,255])
# #     #根据阀值构建掩模
# #     mask = cv2.inRange(hsv,lower_blue,upper_blue)
# #     #对原图和掩模进行位运算
# #     res = cv2.bitwise_and(frame,frame,mask=mask)
# #     #显示图像
# #     cv2.imshow('frame',frame)
# #     cv2.imshow('mask',mask)
# #     cv2.imshow('res',res)
# #     k = cv2.waitKey(5)&0xFF
# #     if k == 27:
# #         break
# # #关闭窗口
# # cv2.destroyAllWindows()

green=np.uint8([[[0,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green )