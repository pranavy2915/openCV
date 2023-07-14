import cv2

import numpy as np

img=cv2.imread("Resources/priya.jpg")

width,height = 350,450
pts1 = np.float32([[111,219],[287,88],[154,582],[352,640]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)