import numpy as np
import cv2

import numpy as np
# import cv2
#
# cap = cv2.VideoCapture("video1.mp4")
# # cap.set(3,100)
# # cap.set(4,100)
# cap.set(3,640)
# cap.set(4,360)
# while (True):
#     # capture frame-by-frame
#     ret, frame = cap.read()
#
#     # our operation on the frame come here
#     #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # display the resulting frame
#     resImg1 = cv2.resize(frame, (300, 300), interpolation=cv2.INTER_CUBIC)
#     cv2.imshow('frame', resImg1)#更改视频流大小
#     if cv2.waitKey(25) & 0xFF == ord('q'):  # 按q键退出
#         break
# # when everything done , release the capture
# cap.release()
# cv2.destroyAllWindows()


#保存视频
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)#使画面上下颠倒

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()