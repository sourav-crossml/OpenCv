import cv2 as cv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

img =cv.imread('Photos/1.jpg')

# cv.imshow('ss',img)

# plt.imshow(img)
# plt.show()




""" 
bgr to grayspace
"""
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

"""
bgr to hsv
"""
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)


"""
bgr to l*a*b
"""
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('lab',lab)
"""
bgr to rgb
"""
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


"""
hsv to bgr
"""
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv_bgr)
# plt.imshow(rgb)
"""
hsv to lab
"""
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab to bgr',lab_bgr)
plt.show()
cv.waitKey(0)