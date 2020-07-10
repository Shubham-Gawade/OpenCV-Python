import cv2
from matplotlib import pyplot as plt

img = cv2.imread("photos/lena.jpg",-1)
cv2.imshow("Image",img) #It displays image BGR format

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #convert image BGR to RGB

plt.imshow(img)
# plt.xticks([]) #Hide coordinates
# plt.yticks([])
plt.show()  #It displays image RGB format

cv2.waitKey(0)
cv2.destroyAllWindows()