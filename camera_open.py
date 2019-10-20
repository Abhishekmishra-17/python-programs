import numpy as np
import cv2
cap=cv2.VideoCapture(1) # replace 1 to 0,1,2,-1 as your camera permission
while(True):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('img',gray)
    if cv2.waitKey(27) & 0xFF==ord('q'):# press "q" to quit the frame
        break
cap.release()
cv2.destroyAllWindows()

