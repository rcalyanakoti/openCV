import cv2 as cv

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('originalImage', img)

#Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Add blur
blur = cv.GaussianBlur(img, (21,21), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Make edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

#dilating an image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilate', dilated)

#eroding
erode = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('erode', erode)

#resize
resized = cv.resize(img, (500,500))
cv.imshow('resize', resized)

#crop
cropped = img[200:500 ,200:500]
cv.imshow('crop', cropped)

cv.waitKey(0)