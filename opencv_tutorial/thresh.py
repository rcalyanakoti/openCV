import cv2 as cv

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Simple Threshold
threshold, thresh = cv.threshold(gray, 175, 255, cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)

#Invert Simple Threshold
threshold, thresh_inv = cv.threshold(gray, 175, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded_inv', thresh_inv)

#Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 7)
cv.imshow('adaptive', adaptive_thresh)

cv.waitKey(0)