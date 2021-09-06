import cv2 as cv

# img=cv.imread('Photos/Screenshot from 2021-08-05 09-16-43.png')

# cv.imshow('ss',img)
# cv.waitKey(0)

capture = cv.VideoCapture('Videos/traacker.webm')

while True:
    isTrue, frame= capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()