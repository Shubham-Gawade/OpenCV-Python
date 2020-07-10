import numpy as np
import cv2 as cv

def nothing(x):
    pass

#Create a black image, a window
img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("image")

cv.createTrackbar("Blue","image",0,255,nothing) #(window name, image name, starting value, end value,callback function)
cv.createTrackbar("Green","image",0,255,nothing)
cv.createTrackbar("Red","image",0,255,nothing)

switch='0 : OFF\n 1 : ON'
cv.createTrackbar(switch,"image",0,1,nothing)

while(1):
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

    b=cv.getTrackbarPos("Blue","image")
    g = cv.getTrackbarPos("Green", "image")
    r = cv.getTrackbarPos("Red", "image")
    s=cv.getTrackbarPos(switch,"image")

    if s == 0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv.destroyAllWindows()