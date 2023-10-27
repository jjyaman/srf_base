import dlib
import cv2
import face_recognition
import struct
import numpy as np
from db_mysql import DataBaseMySQL

# Creamos la instancia para la realizar la conexión a la Base de Datos
db = DataBaseMySQL()

# Establecemos la conexión con la Base de Datos
db.connect()

# Iniciamos la captura de frames en tiempo real
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Determinamos si se encuentra una cara en el frame capturado
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    