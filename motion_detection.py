import cv2
import numpy as np

cam=cv2.VideoCapture(0)
ret,frame1=cam.read()
ret,frame2=cam.read()
while cam.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=5)
    cons,hierar=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for con in cons:
        (x,y,w,h)=cv2.boundingRect(con)
        #print(x,y,w,h)
        if cv2.contourArea(con)<700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.drawContours(frame1,cons,-1,(0,255,0),2)
    cv2.imshow("VIDEO",frame1)
    frame1=frame2
    ret,frame2=cam.read()
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()    