# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:11:47 2020

@author: Mohammad
"""

##########Twelve
import cv2 
import numpy as np
#HSV (Hue saturation value )
# color detection using hsv colors 
def nothing(x):
    print(x)
cap=cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
#making trackbar (horizontal slider)
cv2.createTrackbar('LH',"Tracking",0,360,nothing)
cv2.createTrackbar('LS',"Tracking",0,360,nothing)
cv2.createTrackbar('LV',"Tracking",0,360,nothing)
cv2.createTrackbar('UH',"Tracking",255,255,nothing)
cv2.createTrackbar('US',"Tracking",255,255,nothing)
cv2.createTrackbar('UV',"Tracking",255,255,nothing)
cv2.namedWindow("Image")
while(1):
    #img=cv2.imread("s.jpg")
    ret,img=cap.read()
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lb=cv2.getTrackbarPos('LH',"Tracking")
    lg=cv2.getTrackbarPos('LS',"Tracking")
    lr=cv2.getTrackbarPos('LV',"Tracking")

    ub=cv2.getTrackbarPos('UH',"Tracking")
    ug=cv2.getTrackbarPos('US',"Tracking")
    ur=cv2.getTrackbarPos('UV',"Tracking")
    l_b=np.array([lb,lg,lr])
    u_b=np.array([ub,ug,ur])

    mask=cv2.inRange(imghsv,l_b,u_b)

    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Image",img)
    cv2.imshow("Image2",res)
    cv2.imshow("Image3",mask)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
###########################
import cv2
#thirtheen
#theresholding
img=cv2.imread("s.jpg")
#if the value is lower it will asign to zero if higher it will asign to one 
#so it is only zero or one
ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#inverse of binary threshold
ret,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#in the given range 200 till 255 the image value will remain the same if it is under the 200 if it is above all the rest will be like 200  
ret,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
#under the 200 it will become zero above that it will remain the same
ret,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
#reverse of the above 
ret,th5=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Image",img)
cv2.imshow("THRESH_BINARY",th1)
cv2.imshow("THRESH_BINARY_inverse",th2)
cv2.imshow("THRESH_TRUNC",th3)
cv2.imshow("THRESH_TOZERO",th4)
cv2.imshow("THRESH_TOZERO_INV",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()

#fortheen
###########adaptive threshold
import cv2
img=cv2.imread("s.jpg",0)
th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,11)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,11)

cv2.imshow("img",img)
cv2.imshow("T1",th1)
cv2.imshow("T2",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()