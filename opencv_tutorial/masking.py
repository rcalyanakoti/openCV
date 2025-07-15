import cv2 as cv
import numpy as np

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (500,50), (1000,1000), 255, -1)
circle = cv.circle(blank.copy(), (600,600), 400, 255, -1)
mask = cv.bitwise_xor(rectangle, circle)

# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked_image', masked)

cv.waitKey(0)