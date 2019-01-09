# STEP:1. This step is to sharpen blurry images before we start recognizing them

# How to sharpen an image using OpenCV
# this step can be repeated multiple times till you achieve the desired result

import cv2
import numpy as np

#Linux window/threading setup code.
cv2.startWindowThread()
cv2.namedWindow("Original")
cv2.namedWindow("Sharpen")

#Load source / input image as grayscale, also works on color images...
imgIn = cv2.imread("../HandWriting-Recognition/new_data/test/test.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", imgIn)

#Create the identity filter, but with the 1 shifted to the right!
kernel = np.zeros( (9,9), np.float32)
kernel[4,4] = 2.0   #Identity, times two!

#Create a box filter:
boxFilter = np.ones( (9,9), np.float32) / 81.0

#Subtract the two:
kernel = kernel - boxFilter


#Note that we are subject to overflow and underflow here...but I believe that
# filter2D clips top and bottom ranges on the output, plus you'd need a
# very bright or very dark pixel surrounded by the opposite type.

custom = cv2.filter2D(imgIn, -1, kernel)
cv2.imshow("Sharpen", custom)
cv2.imwrite("../HandWriting-Recognition/new_data/test/test_sharpen.png", custom)


cv2.waitKey(0)

