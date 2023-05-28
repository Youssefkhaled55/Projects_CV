#In This Code we now able to detect any color I want 
#So that I use HSV to define colors I want by HSV map
#After that I make contour around detect code 
#first experment will be by img

import cv2
import numpy as np
import os
import datetime

os.chdir(r'C:\Users\yk406\.anaconda\.spyder-py3')

while(True):
    frame = cv2.imread("pp.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([25,255,55])
    upper = np.array([70,255,255])
    
    mask = cv2.inRange(hsv, lower, upper)  #Threshold the HSV image to get Color blue
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 0.5:
                #compare smaler value to conutour to determine full size of detected area 
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
    
    cv2.imshow("detecting the blue ball", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    k = cv2.waitKey(0)
    if k == 27:
         break
            
cv2.destroyAllWindows()
