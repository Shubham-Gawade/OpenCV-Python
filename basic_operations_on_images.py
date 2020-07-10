import numpy as np
import cv2

img = cv2.imread("photos/messi5.jpg")
img2= cv2.imread("photos/opencv-logo.png")

print(img.shape) #return a tuple of number of rows, columns, and channels
print(img.size) #returns total umber of pixels is accessed
print(img.dtype) #return Image datatype is obtained

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

ball = img[280:340, 330:390] #Intereset of rigion(area which your like to working on)
img[273:333, 100:160]=ball

cv2.imshow("image1",img)

#===========================================================================================

#Resizing
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

#dest_img=cv2.add(img,img2) #you must have image of same size

dest_img=cv2.addWeighted(img,.9,img2,.1,0) #0 -> gamma value
#sum of weight of two image is 0.9(alpha)+0.1(beta)=1

cv2.imshow("image2",dest_img)

cv2.waitKey(0)
cv2.destroyAllWindows()