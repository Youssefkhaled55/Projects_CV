#New made Code used to get coordinate and color RGB from video capture 
#And Show up real time and day
import cv2
import numpy as np
import datetime

events = [i for i in dir(cv2) if 'EVENT' in  i]
print(events)
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
color = (0,255,0)
line_width = 2
radius = 5
point = (0,0) 
def click_event(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
      print(x,', ',y)
    font = cv2.FONT_HERSHEY_SIMPLEX
    strXY = str(x) + ', '+ str(y)
    cv2.putText(frame, strXY, (x, y),font, 1, (255,255,0), 2)
    point = (x,y)
    cv2.imshow('Frame', frame)
    if event == cv2.EVENT_RBUTTONDOWN: 
     blue = frame[y, x, 0]
     green = frame[y, x, 1]
     red = frame[y, x, 2]
     print(blue,', ' ,green,', ',red)
     font = cv2.FONT_HERSHEY_SIMPLEX
     strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
     cv2.putText(frame, strBGR, (x, y), font, 1, (0, 255, 255), 2)
     cv2.imshow('Frame', frame)
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click_event)
while(True):
 ret, frame = cap.read()
 if ret == True:
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: '+ str(cap.get(3)) + 'Height: ' + str(cap.get(4))
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, text, (10, 20), font, 0.5, (0, 255, 255), 2)
    frame = cv2.putText(frame, datet, (10, 40), font, 0.5, (0, 255, 255), 2)
    frame = cv2.resize(frame, (0,0), fx=1,fy=1)
    cv2.circle(frame, point, radius, color, line_width)
    cv2.imshow("Frame",frame)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
       break
cap.release()
cv2.destroyAllWindows()
