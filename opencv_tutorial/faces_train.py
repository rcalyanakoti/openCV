import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir("/Users/ritikacalyanakoti/Projects/opencv_tutorial/faces"):
    people.append(i)

people.remove('.DS_Store')
print(people)
DIR = r'/Users/ritikacalyanakoti/Projects/opencv_tutorial/faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        imgs = os.listdir(path)
        imgs.remove('.DS_Store')

        for img in imgs:
            img_path = os.path.join(path, img)
            if img_path.lower().endswith('.avif'):
                continue

            img_array = cv.imread(img_path)

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training done -----------------")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the recognizer on the features and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)