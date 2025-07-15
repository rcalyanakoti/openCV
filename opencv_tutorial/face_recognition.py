import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['monica', 'joey', 'phoebe', 'rachel', 'chandler']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('/Users/ritikacalyanakoti/Projects/opencv_tutorial/validate/val_phoebs.webp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

#Detect face in image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label is {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (40,40), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('detected face', img)

cv.waitKey(0)