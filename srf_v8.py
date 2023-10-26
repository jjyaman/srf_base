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

# Leemos la img a la extraeremos su vector embedding
path_image = "C:/Users/SENA/Documents/JJYG/SRF/srf_base/imgs/jjyaman.jpeg"
image = cv2.imread(path_image)

# Confirmamos que la foto se haya leído correctamente
if image is not None:
    
    # Generamos el modelo para determinar si se encuentra un rostro en una imagen
    detector = dlib.get_frontal_face_detector()

    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Corroboramos que la imagen contiene una imagen
    faces = detector(gray)
    if faces is not None:
        
        # Extraemos las coordenadas y dimensiones del rostro
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            
            # Redimensionamos el rostro
            face = cv2.resize(image[y:y + h, x:x + w], (224, 224))

            # Vector embedding con face-recognition
            embedding = face_recognition.face_encodings(face)[0]

            print(embedding)
        
        # Generamos un 'try' para el manejo de las excepciones y errores
        try:
            # Ejecutamos el método que nos retornará un registro de la Base de Datos filtrado por ID y nombre de la tabla
            data = db.select_vector_from_table("visitante", 2244)

            # Corroboramos que el objeto contenga información
            if data:
                # Extraemos el vector, acto seguido se Parsea para mostrarlo en su formato original
                hexadecimal = data[0]
                hexadecimal_string = hexadecimal.decode('utf-8')
                byte_array = bytearray.fromhex(hexadecimal_string)
                embedding_db = struct.unpack("f" * (len(byte_array) // 4), byte_array)
                print("Vector embedding recuperado de la base de datos:")
                
                distancia = np.linalg.norm(embedding - embedding_db)
                # Define un umbral para determinar la similitud
                umbral = 0.7
                
                print(distancia)

                # Compara la distancia con el umbral
                if distancia < umbral:
                    print("Los vectores son similares.")
                else:
                    print("Los vectores son diferentes.")

            else:
                print("No se encontraron vectores en la base de datos.")
        except Exception as e:
            print(f"Error al recuperar el vector de la base de datos: {e}")
else:
    print("No se pudo cargar la imagen.")

cv2.waitKey(0)
cv2.destroyAllWindows()