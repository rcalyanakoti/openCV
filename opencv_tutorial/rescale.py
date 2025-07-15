import cv2 as cv

# img = cv.imread('photos/orange_sissy')
# cv.imshow('orangeSissy', img)



def rescaleFrame(frame, scale=0.75):
    #works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #works only for live videos
    capture.set(3, width)
    capture.set(4, height)

#reading videos

capture = cv.VideoCapture('videos/turtles.MOV')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('videoResized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)