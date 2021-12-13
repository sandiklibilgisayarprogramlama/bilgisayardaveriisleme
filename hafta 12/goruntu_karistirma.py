# python -m pip install opencv-python

import cv2

im1 = cv2.imread("yuz.jpeg",cv2.IMREAD_GRAYSCALE)
#im2 = cv2.imread("aku_logo.png")
#dst = cv2.addWeighted(im1,0.8,im2,0.2,0)
cv2.imshow('dst',im1)
cv2.waitKey(0)
