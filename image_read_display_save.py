import numpy as np
import cv2
from matplotlib import pyplot as plt
#img = cv2.imread("img1.jpg",cv2.IMREAD_COLOR)
#img2 = cv2.IMREAD_COLOR(0)
# cv2.namedWindow("image",cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
# else:
#     if k == ord('s'):
#         cv2.imwrite("img2.png",img)
#         cv2.destroyAllWindows()
img = cv2.imread("img1.jpg",0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])  #to hide tick values on X and Y axis
plt.show()