# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:58:45 2020

@author: Mohammad
"""
import cv2
img=cv2.imread('s.jpg',1)


import cv2
import numpy as np
img=np.zeros(img.shape)
cv2.imwrite("MyImage.jpg", img) 

import cv2
img=cv2.imread('s.jpg',1)
cv2.imshow("My Window", img) 
cv2.waitkey(0)  
cv2.destroyAllWindows()  

import cv2
cap = cv2.VideoCapture("video.mp4")

while(cap.isOpened()):

    ret , frame =cap.read()
    cv2.imshow("Image",frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()



cap = cv2.VideoCapture(0)
while(cap.isOpened()):

    ret , frame =cap.read()
    print(cap.get(cv2.CAP_PROP_CONTRAST))
    cv2.imshow("imageE",frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()



import cv2
img=np.zeros(img.shape)
img=cv2.line(img,(0 , 0 ), (255,255), (0,0,255),10)

import cv2
img=np.zeros(img.shape)
img=cv2.arrowedLine(img,(220 , 20 ), (255,255), (0,255,0),10)

import cv2
img=np.zeros(img.shape)
img=cv2.rectangle(img,(255,255),(300,300),(255,0,0),-1)


import cv2
img=np.zeros(img.shape)
img=cv2.circle(img,(300,300),63,(12,232,123),4)


import cv2
img=np.zeros(img.shape)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,"Hello",(400,400), font ,4 , (244,244,244) ,1 , cv2.LINE_AA)



cv2.imshow("imageE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_CONTRAST,50)
cap.set(3,1000)
cap.set(4,1000)

while(cap.isOpened()):

    ret , frame =cap.read()
    print(cap.get(cv2.CAP_PROP_CONTRAST))
    cv2.imshow("imageE",frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import datetime
cap = cv2.VideoCapture(0)
W=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
H=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
font=cv2.FONT_HERSHEY_SIMPLEX
while(cap.isOpened()):

    ret , frame =cap.read()
    date=str(datetime.datetime.now())
    cv2.putText(frame , date, (10,50) , font , 1 , (0,255,255) , 3 )
    cv2.imshow("imageE",frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()



