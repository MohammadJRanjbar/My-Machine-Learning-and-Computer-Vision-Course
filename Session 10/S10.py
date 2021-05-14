
import cv2 
import numpy as np
'''
img=cv2.imread("f.jpg")
output=img.copy()
gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20, param1=150,param2=30,minRadius=0,maxRadius=0)
detected_circles=np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(255,0,0),1)
    cv2.circle(output,(x,y),1,(255,0,0),1)
cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
'''
img=cv2.imread("s.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)

dst=cv2.cornerHarris(gray,2,3,0.04)

dst=cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow("image",img)
if(cv2.waitKey(0) &0xff==27):
    cv2.destroyAllWindows()
'''
'''
img=cv2.imread("S.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners=np.int0(corners)
for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)
cv2.imshow("image",img)
if(cv2.waitKey(0) &0xff==27):
    cv2.destroyAllWindows()
'''
'''
import numpy as np
import cv2
  
cap = cv2.VideoCapture("D.mp4")
  
# initializing subtractor 
fgbg=cv2.createBackgroundSubtractorKNN(detectShadows=False)
  
while(1):
    ret, frame = cap.read()       
  
    # applying on each frame
    fgmask = fgbg.apply(frame)  
  
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
  
cap.release()
cv2.destroyAllWindows()
'''


import numpy as np
import cv2

cap = cv2.VideoCapture('soccer_mean_shift.mp4')

# take first frame of the video
ret,frame = cap.read()

r,h,c,w = 180,20,300,40  
track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))

roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])

cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret ,frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)

    else:
        break

cv2.destroyAllWindows()
cap.release()

