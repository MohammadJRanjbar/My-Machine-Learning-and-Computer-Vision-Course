# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:30:32 2020

@author: Mohammad
"""

import cv2

#five
##using event to detect clicking and giving the cordinates
events = [ i for i in dir(cv2) if 'EVENT' in i ]
#print(events)
def click_event(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        #print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        data=str(x)+','+str(y)
        cv2.putText(frame , data, (x,y) , font , 1 , (0,255,255) , 3 )
        cv2.imshow("image",frame)
    if(event==cv2.EVENT_RBUTTONDOWN):
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        data=str(blue)+','+str(green)+','+str(red)
        cv2.putText(frame , data, (x,y) , font , 1 , (0,255,255) , 3 )
        cv2.imshow("image",frame)


#frame=np.zeros((512,512,3),np.uint8)
frame=cv2.imread("s.jpg")
cv2.imshow("image",frame)
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()


#six
#### a simple drawing fucntion on windows
events = [ i for i in dir(cv2) if 'EVENT' in i ]
#print(events)
def click_event(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        cv2.circle(frame,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if(len(points)>=2):
            cv2.line(frame,points[-1],points[-2],(0,0,255),5)
        cv2.imshow("image",frame)


frame=np.zeros((512,512,3),np.uint8)
#frame=cv2.imread("s.jpg")
cv2.imshow("image",frame)
points=[]
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()


#seven
#click will give you the image colors
events = [ i for i in dir(cv2) if 'EVENT' in i ]
#print(events)
def click_event(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]
        cv2.circle(frame,(x,y),3,(0,0,255),-1)
        img=np.zeros((512,512,3),np.uint8)
        img[:]=[blue,green,red]
        cv2.imshow("color",img)


#frame=np.zeros((512,512,3),np.uint8)
frame=cv2.imread("s.jpg")
cv2.imshow("image",frame)
points=[]
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()



###############################################################################


import cv2
img=cv2.imread("s.jpg")
b,g,r=cv2.split(img)

import cv2
img=cv2.imread("s.jpg")
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

import cv2
img=cv2.imread("s.jpg")
Head=img[400:600,400:600]
img[200:400,100:300]=Head

import cv2
img=cv2.imread("s.jpg")
img=cv2.resize(img,(512,512))

import cv2
img=cv2.imread("s.jpg")
img2=cv2.imread("r.jpg")
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst =cv2.add(img,img2)
cv2.imshow("image",dst)

import cv2
img=cv2.imread("s.jpg")
img2=cv2.imread("r.jpg")
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst2 =cv2.addWeighted(img,1,img2,1,6,0)
cv2.imshow("image2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#########eight
import cv2
#roi = region of interest 
#coping and pasting regions on image
#adding two images together
img=cv2.imread("s.jpg")
img2=cv2.imread("r.jpg")
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
#coping parts
Head=img[400:600,400:600]
img[200:400,100:300]=Head
#adding two images toghter
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst =cv2.add(img,img2)
cv2.imshow("image",dst)
#adding weighted 
dst2 =cv2.addWeighted(img,1,img2,1,6,0)
cv2.imshow("image2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''


########################################################################
####nine
#bitwase opration
import cv2 
import numpy as np
img1=np.zeros((250,500,3),np.uint8)

img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=np.zeros((250,500,3),np.uint8)

img2=cv2.rectangle(img2,(0,0),(250,500),(255,255,255),-1)

#and
img3=cv2.bitwise_and(img2,img1)
#or
img4=cv2.bitwise_or(img2,img1)
#xor
img5=cv2.bitwise_xor(img2,img1)
#not1
img6=cv2.bitwise_not(img1)
#Not2
img7=cv2.bitwise_not(img2)

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("image3",img3)
cv2.imshow("image4",img4)
cv2.imshow("image5",img5)
cv2.imshow("image6",img6)
cv2.imshow("image7",img7)

cv2.waitKey(0)
cv2.destroyAllWindows()
###########################################################################
#ten 
#using trackbars as a switch or as a horizontal slider
def nothing(x):
    print(x)
img=np.zeros((250,500,3),np.uint8)
cv2.namedWindow("Image")
#making trackbar (horizontal slider)
cv2.createTrackbar('B',"Image",0,255,nothing)
cv2.createTrackbar('G',"Image",0,255,nothing)
cv2.createTrackbar('R',"Image",0,255,nothing)
switch='0:OFF \n 1:ON'
cv2.createTrackbar(switch,"Image",0,1,nothing)

while(1):
    cv2.imshow("Image",img)
    k=cv2.waitKey(1) & 0xFF
    if(k==27):
        break
    b=cv2.getTrackbarPos('B',"Image")
    g=cv2.getTrackbarPos('G',"Image")
    r=cv2.getTrackbarPos('R',"Image")
    s=cv2.getTrackbarPos(switch,"Image")
    if(s==0):
        img[:]=[b,g,r]
    else:
        pass
cv2.destroyAllWindows()


import cv2
img=cv2.imread("s.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#eleven 
#using trackbars as a switch or as a horizontal slider
def nothing(x):
    print(x)

cv2.namedWindow("Image")
#making trackbar (horizontal slider)
cv2.createTrackbar('Current_pose',"Image",100,200,nothing)
switch='Color/gray'
cv2.createTrackbar(switch,"Image",0,1,nothing)

while(1):
    img=cv2.imread("s.jpg")
    
    cp=cv2.getTrackbarPos('Current_pose',"Image")
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(cp),(50,150),font,4,(0,0,255),10)
    k=cv2.waitKey(1) & 0xFF
    if(k==27):
        break
    
    s=cv2.getTrackbarPos(switch,"Image")
    if(s==0):
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img=cv2.imshow("Image",img)
cv2.destroyAllWindows()


