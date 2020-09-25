#nineteen 
#edge detection methods
img=cv2.imread("s.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#better for both horizontal and vertical edge detection
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,1,0)
#better for vertical edge detection
sobelX=np.uint8(np.absolute(sobelX))
#better for horizontal edge detection
sobelY=np.uint8(np.absolute(sobelY))
soblecombine=cv2.bitwise_or(sobelX,sobelY)
Images=[img,lap,sobelX,sobelY,soblecombine]
titles=['orginal Image',"Laplacian","SobelX","SobelY","soblecombine"]
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(Images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


#twenty
########canny edge detection
###################it has less noise than others 
img=cv2.imread("s.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#better for both horizontal and vertical edge detection
canny=cv2.Canny(img,100,200)
#better for both horizontal and vertical edge detection
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,1,0)
#better for vertical edge detection
sobelX=np.uint8(np.absolute(sobelX))
#better for horizontal edge detection
sobelY=np.uint8(np.absolute(sobelY))
soblecombine=cv2.bitwise_or(sobelX,sobelY)
Images=[img,lap,sobelX,sobelY,soblecombine,canny]
titles=['orginal Image',"Laplacian","SobelX","SobelY","soblecombine","canny"]
for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(Images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

#twenty one 
##########
########### Lowering or enhanicing image resolution
img=cv2.imread('s.jpg')
#it will reduce the image resolution
lr=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr)
hr=cv2.pyrUp(lr2)
cv2.imshow("hr",hr)
cv2.imshow("lr",lr)
cv2.imshow("lr2",lr2)
cv2.imshow("imageE",img)
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow("Gassian Layer",layer)
lp=[layer]
for i in range(5,0,-1):
    G_E=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],G_E)
    cv2.imshow(str(i),laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()


#twenty one 
##########
########### Lowering or enhanicing image resolution
img=cv2.imread('s.jpg')
#it will reduce the image resolution
#lr=cv2.pyrDown(img)
#lr2=cv2.pyrDown(lr)
#hr=cv2.pyrUp(lr2)
#cv2.imshow("hr",hr)
#cv2.imshow("lr",lr)
#cv2.imshow("lr2",lr2)
#cv2.imshow("imageE",img)
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow("Gassian Layer",layer)
lp=[layer]
for i in range(5,0,-1):
    G_E=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],G_E)
    cv2.imshow(str(i),laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#twenty two 
####################
##############using the pyrimad laplacian and gaussion to blend together 
img=cv2.imread('s.jpg')
img2=cv2.imread('r.jpg') 

img=cv2.resize(img  ,(512,512) )
img2=cv2.resize(img2, (512,512) )

combined=np.concatenate( (img[:,:256] ,img2[:,256:]),axis=1 )
cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.imshow("img3",combined)
#the line between them is still visible


#for first image finding layers
img_copy=img.copy()
gp_img=[img_copy]
for i in range(6):
    img_copy=cv2.pyrDown(img_copy)
    gp_img.append(img_copy)


#generate gaussin for second image
img2_copy=img2.copy()
gp_img2=[img2_copy]
for i in range(6):
    img2_copy=cv2.pyrDown(img2_copy)
    gp_img2.append(img2_copy)    

#generate laplacian pyramid for first image
img_copy=gp_img[5]
lp_img=[img_copy]
for i in range(5,0,-1):   
    g_e=cv2.pyrUp(gp_img[i])
    laplacian=cv2.subtract(gp_img[i-1],g_e)
    lp_img.append(laplacian)
#generate laplacian pyramid for first image
img2_copy=gp_img2[5]
lp_img2=[img2_copy]
for i in range(5,0,-1):   
    g_e2=cv2.pyrUp(gp_img2[i])
    laplacian2=cv2.subtract(gp_img2[i-1],g_e2)
    lp_img2.append(laplacian2)
img_img2_pyrimad=[]
n=0
for I1,I2 in zip (lp_img,lp_img2):
    n=+1
    cols,rows,ch=I1.shape
    laplacian= np.concatenate( (I1[:,0:int(cols/2)] ,I2[:,int(cols/2):]),axis=1 )
    img_img2_pyrimad.append(laplacian)
reconstruct_img=img_img2_pyrimad[0]
for i in range(1,6):
    reconstruct_img=cv2.pyrUp(reconstruct_img)
    reconstruct_img=cv2.add(img_img2_pyrimad[i],reconstruct_img)
cv2.imshow("reconstruct_img",reconstruct_img)
cv2.waitKey(0)
cv2.destroyAllWindows()