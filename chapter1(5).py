import cv2

import numpy
import numpy as np

img = cv2.imread('Resources/google.jpg')
print(img.shape)
img2 = cv2.imread('Resources/priya.jpg')
print(img2.shape)
img3 = cv2.resize(img2,(400,400))
print(img3.shape)
hor = np.hstack((img , img, img))
ver = np.vstack((hor , hor, hor))

# cv2.imshow("Horizontal",hor)
cv2.imshow("Vertical",ver)
cv2.waitKey(0)