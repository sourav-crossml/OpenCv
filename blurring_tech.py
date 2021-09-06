import cv2 as cv
import numpy as np

img =cv.imread('Photos/1.jpg')
cv.imshow('img',img)

"""
averaging
"""
average=cv.blur(img,(3,3))
cv.imshow('average blur',average)


"""
Gaussion Bur 
"""
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('gaussion',gauss)

"""
median blur
"""
median=cv.medianBlur(img,3)
cv.imshow('median blur',median)

"""
bilateral bluring
"""
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)



cv.waitKey(0)