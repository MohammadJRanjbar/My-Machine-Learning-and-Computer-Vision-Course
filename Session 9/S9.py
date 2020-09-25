#thirty one 
#the hough transform half line and finding road line in an image

import cv2 
import numpy as np
import matplotlib.pyplot as plt
def region_of_interest(img,vertices):
    mask= np.zeros_like(img)
    #channel_count=img.shape[2]
    match_mask_color= 255
    cv2.fillPoly (mask , vertices , match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image
def drow_line(img,lines):
    img=np.copy(img)
    blanck_img=np.zeros( (img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blanck_img,(x1,y1),(x2,y2),(0,255,0),3)
    img=cv2.addWeighted(img,0.8,blanck_img,1,0 )
    return img

img=cv2.imread('road.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

height=img.shape[0]
width=img.shape[1]
region_of_interest_vertices=[(0,height),((width+200)/2,(height-100)/2),(width,height)]
gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
canny_image=cv2.Canny(gray_image,100,255)
cropped_image =region_of_interest( canny_image , np.array( [region_of_interest_vertices] , np.int32 ) )
lines=cv2.HoughLinesP(cropped_image, rho=6 , theta=np.pi/16 ,threshold=100,lines=np.array([]),minLineLength=40,maxLineGap=25)
img_with_lines=drow_line(img,lines)

plt.imshow(img_with_lines)
plt.show()

#thirty two
#testing it on video 
def region_of_interest(img,vertices):
    mask= np.zeros_like(img)
    #channel_count=img.shape[2]
    match_mask_color= 255
    cv2.fillPoly (mask , vertices , match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image
def drow_line(img,lines):
    img=np.copy(img)
    blanck_img=np.zeros( (img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blanck_img,(x1,y1),(x2,y2),(0,255,0),3)
    img=cv2.addWeighted(img,0.8,blanck_img,1,0 )
    return img
def process(img):
    height=img.shape[0]
    width=img.shape[1]
    region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)]
    gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    canny_image=cv2.Canny(gray_image,160,255)
    cropped_image =region_of_interest( canny_image , np.array( [region_of_interest_vertices] , np.int32 ) )
    lines=cv2.HoughLinesP(cropped_image, rho=2 , theta=np.pi/16 ,threshold=50,lines=np.array([]),minLineLength=40,maxLineGap=100)
    img_with_lines=drow_line(img,lines)
    return img_with_lines
cap=cv2.VideoCapture('w.mp4')
while(cap.isOpened()):
    _,frame=cap.read()
    frame=process(frame)
    cv2.imshow( "video" , frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

#thirty three
#circle detection
img=cv2.imread("f.jpg")
output=img.copy()
gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
#thie method works better with bullred image
gray=cv2.medianBlur(gray,5)
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=60,param2=30,minRadius=0,maxRadius=0)
detected_circles=np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(255,0,0),1)
    cv2.circle(output,(x,y),1,(255,0,0),1)
cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()


#thirty four 
#face detection
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    _,frame=cap.read()
    img_copy=frame.copy()
    img_copyq=cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img_copy,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('video',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

#thirty five
#eye detecion 
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    _,frame=cap.read()
    img_copy=frame.copy()
    img_copy=cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img_copy,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=img_copy[y:y+h,x:x+w]
        roi_coulor=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_coulor,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('video',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()