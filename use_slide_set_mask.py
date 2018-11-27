import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("image")
cv2.createTrackbar('Threshold','image',0,255,nothing)
while (1):
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break;
    threshold = cv2.getTrackbarPos('Threshold','image')
    #print(threshold)
    img1=cv2.imread('img6.jpg')
    img3=cv2.imread('img7.jpg')
    img2 = cv2.resize(img3,(img1.shape[1],img1.shape[0]))
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows,0:cols]

    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,mask = cv2.threshold(img2gray,threshold,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
    #取roi中与mask_inv中不为零的值对应的像素的值，其他值为0
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)

    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows,0:cols] =dst

    cv2.imshow('image',dst)
    #cv2.waitKey(0)