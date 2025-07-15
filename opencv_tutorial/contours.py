import cv2 as cv
import numpy as np

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray,  (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 200, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(img, contours, -1, (0,0,255), 2)
cv.imshow('contours', img)


cv.waitKey(0)