import cv2
import matplotlib.pyplot as plt
import numpy as np
'''
#twenty three
##finding edges using contours
img=cv2.imread('s.jpg') 
img=cv2.resize(img  ,(512,512) )
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imggray,127,255,0)
contours , hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("number of contours  " + str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,0),1)
cv2.imshow("image",img)
cv2.imshow("Image Gray",imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#twenty four
#simple motion detection 
cap=cv2.VideoCapture(0)
ret,frame1 = cap.read()
ret,frame2 = cap.read()
while(cap.isOpened()):
    diff=cv2.absdiff(frame1,frame2)
    Gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blured=cv2.GaussianBlur(Gray,(5,5),0)
    ret,thresh=cv2.threshold(blured,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=5)
    contours , hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours: 
        (x,y,w,h)=cv2.boundingRect(contour)
        if (cv2.contourArea(contour)<10000):
            pass
        else:
            frame1=cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame1,"Status : {}".format("movment"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    
    #cv2.drawContours(frame1,contours,-1,(0,255,0),1)
    cv2.imshow("frame",frame1)
    frame1=frame2
    ret,frame2 = cap.read()
    if(cv2.waitKey(40)==27):
        break
cv2.destroyAllWindows()
cap.release() 

#twenty five 
#simple  geometric shape detection
img=cv2.imread('s.png') 
#img=cv2.resize(img  ,(512,512) )
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(imggray,240,255,cv2.THRESH_BINARY)
contours , hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours: 
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)  
        cv2.drawContours(img,[approx],0,(0,255,0),5,)
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        if(len(approx)==3):
            cv2.putText(img,"triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        elif(len(approx)==4):
            (x,y,w,h)=cv2.boundingRect(contour)
            if(float(w)/h>=0.95 and float(w)/h<=1.05):
                cv2.putText(img,"square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            else:
                cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        elif(len(approx)==5):
            cv2.putText(img,"pentagon",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        elif(len(approx)==10):
            cv2.putText(img,"star",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        else:
            cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
#twenty six
###########Histogram
#img=np.zeros((200,200),np.uint8)

#cv2.rectangle(img,(0,100),(200,200),(255,255,255),-1)
#cv2.rectangle(img,(0,50),(100,100),127,-1)
#plt.hist(img.ravel(),256,[0,256])

img=cv2.imread('f.jpg') 
b,g,r=cv2.split(img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("Image",img)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#twenty seven 
#using cv2 hsitogram method
img=cv2.imread('f.jpg',0) 
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#twenty eight 
######template matching 
####06:24
#### based on thereshold finds a location and if that was available there is a matrix and we can locate the picture
###thershold finds the brightest point
img=cv2.imread('s.jpg') 
img_smaller=cv2.imread('s2.jpg',0) 
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
res=cv2.matchTemplate(img,img_smaller,cv2.TM_CCORR_NORMED)
thershold=0.99
loc=np.where(res > thershold)
w,h= img_smaller.shape[::-1]
print(loc)
for pt in zip(*loc[::-1]): 
    cv2.rectangle(img,pt, (pt[0]+w,pt[1]+h) , (0,0,255) , 2)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()