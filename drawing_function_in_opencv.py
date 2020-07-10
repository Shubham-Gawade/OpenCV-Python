import numpy as np
import cv2

#img = cv2.imread("lena.jpg",1)

img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img, (0,0) , (255,255) , (0,0,255) , 10)
# image , starting coordinate of point 1, ending coordinate of point 2 , color , thickness in number
# (255,0,0) -> (blue,green,red)

img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),10)

img = cv2.rectangle(img,(384,0,),(510,128),(0,0,255),5)

#img = cv2.rectangle(img,(384,0,),(510,128),(0,0,255),-1) # filled rectangle

img  = cv2.circle(img,(447,63),63,(0,255,0),-1)

font =  cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "MyEditor", (10,490),  font , 3 , (0,255,255) , 10 , cv2.LINE_AA)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

