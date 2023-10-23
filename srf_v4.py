import cv2
import imutils
import face_recognition
import dlib
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cont = 0
max_frames = 100  # Número máximo de fotogramas a procesar

archivo_txt = "C:/Users/SENA/Documents/JJYG/SRF/srf_base/vector/embeddings.txt"

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=640)

    # Convertir la imagen a escala de grises
    face_image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectamos los rostros en la imagen utilizando face_recognition
    face_locations = face_recognition.face_locations(face_image_gray)

    if face_locations:
        # Procesar todos los rostros detectados
        for face_location in face_locations:
            top, right, bottom, left = face_location

            face_image = face_image_gray[top:bottom, left:right]

            # Calcula los vectores de embedding para el rostro recortado
            face_encodings = face_recognition.face_encodings(face_image)

            for encoding in face_encodings:
                print(encoding)
                with open(archivo_txt, "a") as archivo:
                    # Convertir la lista de números en una cadena
                    embedding_str = " ".join(str(num) for num in encoding)
                    # Escribir la cadena en el archivo
                    archivo.write(embedding_str + "\n")
    else:
        print("No se encontró un rostro")

    cont += 1

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or cont >= max_frames:
        break

cap.release()
cv2.destroyAllWindows()
