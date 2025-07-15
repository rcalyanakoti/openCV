import cv2 as cv
import numpy as np

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


# merged = cv.merge([r, r, r]) is the same thing as cv.imshow('red', r)
merged = cv.merge([b, g, r])
cv.imshow('merged', merged)

cv.waitKey(0)