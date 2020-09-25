# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:52:40 2020

@author: Mohammad
"""

#fifteen 
#############matplotlib
from matplotlib import pyplot as plt
import cv2
img=cv2.imread("s.jpg")
cv2.imshow("img",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#sixteen
###########subplotss
img=cv2.imread("s.jpg",0)
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
titles=["Image","THRESH_BINARY"
,"THRESH_BINARY_inverse"
,"THRESH_TRUNC",
"THRESH_TOZERO","THRESH_TOZERO_INV"]

images=[img,th1,th2,th3,th4,th5]
for i in range(6):
    #first argument is rows and second is number of column
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
#cv2.imshow("Image",img)
#cv2.imshow("THRESH_BINARY",th1)
#cv2.imshow("THRESH_BINARY_inverse",th2)
#cv2.imshow("THRESH_TRUNC",th3)
#cv2.imshow("THRESH_TOZERO",th4)
#cv2.imshow("THRESH_TOZERO_INV",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()



#eighteen 
##smoothing images or bluring and filters using open cv 
img=cv2.imread("s.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#removing the noise from the image
kernel=np.ones((5,5),np.float32)/25
#low pass filter helps removing the noise 
#high pass filter helps to find the edges
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
#Gassian filter the center are more weighted and corner are less weighted
Gbl=cv2.GaussianBlur(img,(5,5),0)
#it will replace a value with neighbor value it is good for salt and pepper noise 
MF=cv2.medianBlur(img,3)
#
bilaterfilter = cv2.bilateralFilter(img,9,75,75)
Images=[img,dst,blur,Gbl,MF,bilaterfilter]
titles=['orginal Image',"2D convolve","blur","GaussianBlur","Median blur","bilaterfilter"]
for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(Images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

##########################################################################################
#seventeen
#morphological transformation
#some where around after matplotlib 03:37:
img=cv2.imread("f.jpg",0)
ret,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
#the bigger the kernal is the better the result
kernal=np.ones((5,5),np.uint8)
dialation=cv2.dilate(mask,kernal,iterations=5)
#some size wil increase after dialation 
#next morphological transformation is erosion 
#erode the corner of the image 
erosion=cv2.erode(mask,kernal,iterations=5)
#opening is a combination of erosion and dilation it will first do the erosion and then dialation
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal )
#opening is a combination of dialation and erosion it will first do the dialation and then erosion
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal )
#closing
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal )
#top hat is the difference of orginal image and the opening image
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal )
titles=["Image","Maks","dialation","erosion",'opening','closing',"Gradient","top hat"]
Images=[img,mask,dialation,erosion,opening,closing,mg,th]
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(Images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()