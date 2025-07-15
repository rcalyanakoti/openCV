import cv2 as cv

# reading images

img = cv.imread('photos/orange_sissy.jpg')

cv.imshow('orangeSissy', img)

# reading videos

capture = cv.VideoCapture('videos/turtles.MOV')

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)