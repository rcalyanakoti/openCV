import cv2 as cv
import numpy as np

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

#translate image
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

#rotate image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
    
rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

#resize image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resize', resized)

#flip image
flip = cv.flip(img, 1)
cv.imshow('flip', flip)

#crop image
cropped = img[500:600, 800:1000]
cv.imshow('cropped', cropped)

cv.waitKey(0)