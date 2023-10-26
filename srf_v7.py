import dlib
import cv2
import imutils
import face_recognition
import struct
from db_mysql import DataBaseMySQL
#from deepface import DeepFace

# Creamos la instancia para la realizar la conexión a la Base de Datos
db = DataBaseMySQL()

# Establecemos la conexión con la Base de Datos
db.connect()

# Iniciamos la captura de frames en tiempo real
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Determinamos si se encuentra una cara en el frame capturado
detector = dlib.get_frontal_face_detector()

# Creamos una variable, la cual tendrá la función de determinar la cantidad de frames a capturar
cont = 0

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    #frame = imutils.resize(frame, width=640)

    # Convertimos la imagen a escala de grises
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

        # Convertimos el vector embedding en un array de bytes
        byte_array = bytearray(struct.pack("f" * len(embedding), *embedding))
        
        #Trasladamos el array de bytes a un formato hexadecimal
        hexadecimal = byte_array.hex()
        
        cont +=1

    # Insertando un registro en la Base de Datos
    #data = db.insert_into_vector("visitante", hexadecimal)
    
    # Seleccionando un registro de la Base de Datos
    #data = db.select_vector_from_table("visitante", 1128)
    
    try:
        data = db.select_vector_from_table("visitante", 1128)
        
        if data:
            hexadecimal = data[0]
            hexadecimal_string = hexadecimal.decode('utf-8')
            byte_array = bytearray.fromhex(hexadecimal_string)
            embedding = struct.unpack("f" * (len(byte_array) // 4), byte_array)
            print("Vector embedding recuperado de la base de datos:")
            print(embedding)
        else:
            print("No se encontraron vectores en la base de datos.")
    except Exception as e:
        print(f"Error al recuperar el vector de la base de datos: {e}")
    

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or cont == 1:
        break

# Cerramos la conexión con la Base de Datos
db.disconnect()

cap.release()
cv2.destroyAllWindows()