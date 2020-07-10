import cv2

img = cv2.imread("photos/lena.jpg",-1) # flag -> 0,1,-1

# 1) cv2.IMREAD_COLOR -> 1 -> loads a color image
# 2) cv2.IMREAD_GRAYSCALE -> 0 -> load image in grayscale mode
# 3) cv2.IMREAD_UNCHANGED -> -1 -> loads image as such including alpha channel (as it is image)

# imread function will not give error if you enter wrong file name

print(img) # print pixels in matrix form

cv2.imshow("image",img) # ( window name , image variable)
k = cv2.waitKey(0)  # no of miliseconds

if k == 27:  # Ascii value of esc key
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("photos/lena_copy.png",img) # ( new file name, image variable)
    cv2.destroyAllWindows()