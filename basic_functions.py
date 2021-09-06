import cv2 as cv

img =cv.imread('Photos/Screenshot from 2021-08-05 09-14-45.png')

cv.imshow('ss',img)
"""
to make image black and whit
"""
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

"""
to make image blur
"""
# blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

"""
edge cascade
"""
# canny= cv.Canny(img,125,175)
# cv.imshow('canny',canny)

"""
dilating the image
"""
# dilated=cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('dilated',dilated)

"""
Eroding
"""
# eroded=cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('eroding',eroded)

"""
resize image
"""

# resize= cv.resize(img,(500,500),interpolatiom=cv.INNER_CUBIC)
# cv.imshow('resize',resize)

"""
croping
"""
cropped= img[50:200,200:400]
cv.imshow('cropped',cropped)





cv.waitKey(0)