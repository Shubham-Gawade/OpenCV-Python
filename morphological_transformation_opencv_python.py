#Morphological transformation are some simple operations based on the image shape

#A structuring element or A kernel tells you how to chane the value of any given pixel by combining it
# with differnt amounts of the neighboring pixels

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("photos/smarties.png",cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((3,3),np.uint8)

#Dilation -> remove black dots from balls
dilation = cv2.dilate(mask,kernal,iterations=2)

#erosion -> reduce the size of kernel
erosion = cv2.erode(mask,kernal,iterations=2)

#opening -> first perform erosion then perform dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

titles = ["image","mask","dilation","erosion","opening","closing"]
images = [img,mask,dilation,erosion,opening,closing]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()