import cv2

cap = cv2.VideoCapture(0) # device index -> 0 or -1
#multiple camera -> 1 for first camera and 2 for second camera

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi" , fourcc , 20.0 , (640,480))
# (name of your output file, fourcc code , frame per second , size of video)

while (cap.isOpened()):  # it will return false if file path is wrong

    ret , frame = cap.read() # read() return two values 1) true or false if frame is available or not 2) frame variable

    if ret == True:
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # provide property id -> width
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # change frame to gray

        cv2.imshow("frame",gray)

        if cv2.waitKey(1) & 0xFF == ord('q'): # mask for 64 bit machine
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()