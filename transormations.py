import cv2 as cv
import numpy as np
img=cv.imread('Photos/Screenshot from 2021-08-15 12-01-33.png')

cv.imshow('img',img)

"""
translataion
"""
# def translate(img,x,y):
    # transMat= np.float32([[1,0,x],[0,1,y]])
    # dimensions=(img.shape[1],img.shape[0])
    # return cv.warpAffine(img,transMat,dimensions)

"""
left-->
up-->
right-->
Down-->
"""
# translated=translate(img,100,100)
# cv.imshow('Transalted',translated)

"""
rotaion
"""
# def rotate(img,angle,rotPoint=None):
    # (height,width)=img.shape[:2]
    # if rotPoint is None:
        # rotPoint=(width//2,height//2)
    # rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    # dimensions=(width,height)
    # return cv.warpAffine(img,rotMat,dimensions)

# rotated=rotate(img,45)
# rotated=rotate(img,-90)

# rotated1=rotate(rotated,-45)

# cv.imshow('rotated',rotated)
"""
resizing

"""

# resized=cv.resize(img,(500,500),interpolation=cv.INNER_CUBIC)
# cv.imshow('resized',resized)

"""
flipiing
"""
# flip=cv.flip(img,0)  
# flip=cv.flip(img,1)  

# cv.imshow('flip',flip)

"""
cropping
"""
cropped=img[200:400,300:400]
cv.imshow('cropped',cropped)




cv.waitKey(0)