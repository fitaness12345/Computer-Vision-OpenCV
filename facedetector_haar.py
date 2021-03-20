#FACEDETECTION_HAAR.PY

import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0, cv.CAP_DSHOW)
while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar = cv.CascadeClassifier("haar.xml")
    faces = haar.detectMultiScale(frame, scaleFactor=1.1,minNeighbors=3)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), thickness=2)
        cv.imshow("Detected Face", frame)

    if faces.all() <= 1:
        print(f"Number of faces = {len(faces)}")
    else:
        break

    if cv.waitKey(20) & 0xff == ord("q"):
        break
