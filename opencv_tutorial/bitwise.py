import cv2 as cv
import numpy as np

img = cv.imread('photos/orange_sissy.jpg')
cv.imshow('orangeSissy', img)

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)


cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

# bit_and = cv.bitwise_and(cv.resize(img, (100,100), interpolation=cv.INTER_AREA), cv.resize(cv.imread('photos/pink_sissy.jpg'), (100,100), interpolation=cv.INTER_AREA))
# cv.imshow('bit_and', bit_and)

#bitwise OR

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

#bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not', bitwise_not)



cv.waitKey(0)