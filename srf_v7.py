import dlib
import cv2
import os
import face_recognition
import struct
from db_mysql import DataBaseMySQL
#from deepface import DeepFace

path_dir = "C:/Users/SENA/Documents/JJYG/SRF/srf_base/imgs"
name_dir = "data"
path_imgs = os.path.join(path_dir, name_dir)
if not os.path.exists(path_imgs):
    os.makedirs(path_imgs)  

# Este algoritmo busca que por medio de la lectura de los rostros que se identifiquen en tiempo real, busque en la Base de Datos un rostro que sea igual y muestre la información relacionada a ese rostro que se encuentra en la Base de Datos. Todo esto por medio de los vectores 'embeddings'.

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
    
    # Imutils, utilizado para redimensionar una imagen
    #frame = imutils.resize(frame, width=640)

    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    if faces is not None:

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

            # Variables para crear el registro
            num_doc = int(input("Ingrese el número de documento: "))
            name = input("Ingrese el nombre completo: ")
            last_name = input("Ingrese los apellidos: ")
            genero = input("Ingrese el género: ")

            # Insertando un registro en la Base de Datos
            data = db.insert_into_vector("visitante", num_doc, name, last_name, hexadecimal, genero)

        # Guardamos el rostro capturado en una carpeta llamada 'data'
        cv2.imwrite(path_imgs + '/rostros_{}.jpg'.format(num_doc), gray)

    else:
        print("No se encontro un rostro")
    
    
    # Generamos un 'try' para el manejo de las excepciones y errores
    # try:
    #     # Ejecutamos el método que nos retornará un registro de la Base de Datos filtrado por ID y nombre de la tabla
    #     data = db.select_vector_from_table("visitante", 1128)

    #     # Corroboramos que el objeto contenga información
    #     if data:
    #         # Extraemos el vector, acto seguido se Parsea para mostrarlo en su formato original
    #         hexadecimal = data[0]
    #         hexadecimal_string = hexadecimal.decode('utf-8')
    #         byte_array = bytearray.fromhex(hexadecimal_string)
    #         embedding = struct.unpack("f" * (len(byte_array) // 4), byte_array)
    #         print("Vector embedding recuperado de la base de datos:")
    #         print(embedding)
    #     else:
    #         print("No se encontraron vectores en la base de datos.")
    # except Exception as e:
    #     print(f"Error al recuperar el vector de la base de datos: {e}")
    

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or cont == 1:
        break

# Cerramos la conexión con la Base de Datos
db.disconnect()

# Liberamos la fuente de vídeo y cerramos las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()