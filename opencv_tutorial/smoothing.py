import cv2 as cv

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

#Averaging
average = cv.blur(img, (21, 21))
cv.imshow('Average blur', average)

#Gaussian blurring
gaussian = cv.GaussianBlur(img, (21,21), 0)
cv.imshow('Gaussian Blur', gaussian)

#Median blurring
median = cv.medianBlur(img, 21)
cv.imshow('Median', median)

#Bilateral blurring
bilateral = cv.bilateralFilter(img, 50, 500, 500)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)