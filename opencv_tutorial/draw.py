import cv2 as cv
import numpy as np


blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#Paint image certain color

blank[200:300, 350:400] = 0, 255, 0
cv.imshow('Green', blank)

#Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//4), (0,0,255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3)
cv.imshow("circle", blank)

#Draw a line
cv.line(blank, (0,0),  (blank.shape[1]//2, blank.shape[0]//2), (255,255,255))
cv.imshow('line', blank)

img = cv.imread('photos/orange_sissy.jpg')
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
cv.imshow('text', blank)
cv.imshow('orangeSissy', img)

cv.waitKey(0)