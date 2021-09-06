import cv2 as cv
import numpy as np
img =cv.imread('Photos/Screenshot from 2021-08-05 09-14-45.png')

cv.imshow('ss',img)
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# canny=cv.Canny(blur,125,175)
# cv.imshow('canny Edges',canny)


ret , thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)


"""
contours list generation
"""
contours,hierachies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours draw',blank)















cv.waitKey(0)