import cv2 as cv
import numpy as np

img=cv.imread("photos/gradient.png",0)

#Binary Thresholding
_, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# if value of pixel < thresold value(127) -> 0 (black)
# if value of pixel > thresold value(127) -> 255 (white)

#Thresholding Binary Inverse
_, th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

#Thresh Trunk
_, th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
#After threshold will keep as it is

#Thresh tozero
_, th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
#when pixel value < threshold value then it is set to 0 (black)

#Thresh tozero inverse
_, th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
#when pixel value > threshold value then it is set to 0 (black)

cv.imshow("Image",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)
cv.imshow("th4",th4)
cv.imshow("th5",th5)

cv.waitKey(0)
cv.destroyAllWindows()