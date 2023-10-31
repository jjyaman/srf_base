import dlib
import cv2
import face_recognition
import struct
from db_mysql import DataBaseMySQL
from scipy.spatial.distance import cosine

#****************************************************************************************************#
# Este algoritmo determina si existe un rostro en tiempo real, si encuentra un rostro, 
# extrae su vector 'embedding' y realiza una búsqueda en la base de datos para determinar 
# la identidad de la persona, finalmente imprime el nombre de la persona identificada
#****************************************************************************************************#

# Creamos la instancia para la realizar la conexión a la Base de Datos
db = DataBaseMySQL()

# Establecemos la conexión con la Base de Datos
db.connect()

# Extraemos los registros de la Base de Datos. Establecemos los parámetros
data = db.select_all_register_from_table('rostro', 'nombre_completo', 'visitante')

# Determinamos un umbral para realizar la similitud de cosenos
umbral = 0.9

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
    
    # Generamos un try-exception para manejar las errores
    try:

        # Extraemos las coordenadas y dimensiones del rostro capturado en tiempo real
        for face in faces:
        
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            
            # Redimensionamos el rostro
            face = cv2.resize(frame[y:y + h, x:x + w], (224, 224))

            # Vector embedding con face-recognition
            embedding = face_recognition.face_encodings(face)[0]

        
            if embedding is not None:

                # Iteramos sobre los registros de la base de datos
                for i in data:
                    
                    # Transformamos el vector 'embedding' de la base de datos a su formato normal
                    hexadecimal = i[0].decode('utf-8')
                    byte_array = bytearray.fromhex(hexadecimal)
                    embedding_db = struct.unpack("f" * (len(byte_array) // 4), byte_array)

                    # Determinamos la similitud de los cosenos
                    similarity = 1 - cosine(embedding, embedding_db)
                    
                    # Si la similitud de los cosenos es superior al umbral imprimimos el nombre de la persona
                    if similarity > umbral:
                        print("¡Rostro encontrado! Similitud de coseno:", similarity)
                        print(f"{i[1]}")
                        input()

    except Exception as e:
        print(f"Error al identificar un rostro: {e}")

    #cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

# Cerramos la conexión con la Base de Datos
db.disconnect()

# Liberamos la fuente de vídeo y cerramos las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()