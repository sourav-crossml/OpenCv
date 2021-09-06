import cv2 as cv
# import numpy as np
# import matplotlib
import numpy as np
import matplotlib.pyplot as plt

img =cv.imread('Photos/1.jpg')
cv.imshow('img',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

"""
grayscale histogram 
"""

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])




plt.figure()
plt.title('grayscale histogrsm')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256] )
plt.show()

cv.waitKey(0)