import cv2 as cv

img =cv.imread('Photos/Screenshot from 2021-08-16 10-00-52.png')


def rescaleFrame(frame,scale=0.2):
    """
    this method will work for imgs , videos live video
    """
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


def changerefe(width,height):
    """
    this one will work for only live video 
    """
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videos/traacker.webm')
rimg=rescaleFrame(img)
cv.imshow('image',rimg,)
cv.waitKey(0)

capture = cv.VideoCapture('Videos/traacker.webm')

while True:
    isTrue, frame= capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('Video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()