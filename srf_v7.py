import dlib
import cv2
import imutils
import face_recognition
import numpy as np
from deepface import DeepFace
from database import sql_request

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = dlib.get_frontal_face_detector()

cont = 0

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        
        # Redimensionamos el rostro
        face = cv2.resize(frame[y:y + h, x:x + w], (224, 224))

        # Vector embedding con face-recognition
        embedding = face_recognition.face_encodings(face)[0]

        # Vector embedding con deepface
        #embedding = DeepFace.extract_faces(face)[0]

        print(embedding)
        cont +=1
        
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or cont >= 10:
        break

cap.release()
cv2.destroyAllWindows()