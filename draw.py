import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
"""
painting a certain color on image 
"""
# blank[200:300,200:300]=0,0,255
# cv.imshow('green',blank)

"""
Draw a Rectangle
"""
# cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
"""
to fill in the rectangle
"""
# cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
"""
for giving shape to respect to screen
"""
# cv.rectangle(blank,(0,0),(blank.shape[1]//1,blank.shape[0]//2),(0,250,0),thickness=2)

# cv.imshow('rectangle',blank)

"""
to draw a circle
"""
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
# cv.imshow('circle',blank)

"""
to draw a line
"""
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.imshow('line',blank)

"""
to put text on image
"""
cv.putText(blank,"hello",(225,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,225),2)
cv.imshow('text',blank)






# img=cv.imread('Photos/Screenshot from 2021-08-05 09-16-43.png')

# cv.imshow('ss',img)
cv.waitKey(0)