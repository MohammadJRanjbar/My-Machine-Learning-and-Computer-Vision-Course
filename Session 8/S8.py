import cv2
import numpy as np
#twenty nine 
#the hough transform 
img=cv2.imread('s.png',0)
edges=cv2.Canny(img,50,150,apertureSize=3)
cv2.imshow("edges",edges)
lines=cv2.HoughLines(edges,1,np.pi/100,200)
for line in lines:
    rho , theta =line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho 
    y0=b*rho

    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


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
#thirty one 
#the hough transform half line and finding road line in an image
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