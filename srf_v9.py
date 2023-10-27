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

# Extraemos los registros de la Base de Datos
data = db.select_column_from_table('rostro', 'visitante')

# Creamos una lista que va a almacenar todos los vectores embedding

# Iniciamos la captura de frames en tiempo real
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Determinamos si se encuentra una cara en el frame capturado
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
     # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    if faces is not None:

        # Extraemos las coordenadas y dimensiones del rostro
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            
            # Redimensionamos el rostro
            face = cv2.resize(frame[y:y + h, x:x + w], (224, 224))

            # Vector embedding con face-recognition
            embedding = face_recognition.face_encodings(face)[0]

            

    else:
        print("No se detecto ningún rostro")

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

# Cerramos la conexión con la Base de Datos
db.disconnect()

# Liberamos la fuente de vídeo y cerramos las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()



    