#In This Code we now able to detect any color I want 
#So that I use HSV to define colors I want by HSV map
#After that I make contour around detect code 
#second experment will be by video
#Try to input time, date, coordiantes and RGB range
import cv2
import numpy as np
import datetime

events = [i for i in dir(cv2) if 'EVENT' in  i]
print(events)
# Specifying upper and lower ranges of color to detect in hsv format
lower = np.array([25,255,55])
upper = np.array([70,255,255]) # (These ranges will detect Yellow)
# Capturing webcam footage
webcam = cv2.VideoCapture(0)
print(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(webcam.get(3))
print(webcam.get(4))
while True:
    success, video = webcam.read() # Reading webcam footage
    if success == True:
     font = cv2.FONT_HERSHEY_SIMPLEX
     text = 'Width: '+ str(webcam.get(3)) + 'Height: ' + str(webcam.get(4))
     datet = str(datetime.datetime.now())
     video = cv2.putText(video, text, (10, 50), font, 1, (0, 0, 0), 2)
     video = cv2.putText(video, datet, (10, 100), font, 1, (0, 0, 0), 2)
     img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format
     mask = cv2.inRange(img, lower, upper) # Masking the image to find our color
     mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
     res = cv2.bitwise_and(video, video, mask=mask)
    # Finding position of all contours
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 0.1:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    cv2.imshow("mask image", mask) # Displaying mask image
    cv2.imshow("window", video) # Displaying webcam image
    cv2.imshow("res", res) #Display recognized color with masking
    cv2.waitKey(1)




    