#Este algoritmo extre un 'Vector Embedding' de un rostro
import face_recognition

# Carga la imagen que contiene el rostro que deseas analizar
image_path = "imgs/will_smith.jpg"
image = face_recognition.load_image_file(image_path)

# Encuentra todos los rostros en la imagen
face_locations = face_recognition.face_locations(image)

# Si se detecta al menos un rostro en la imagen
if face_locations:
    # Obtén el vector de embedding para el primer rostro detectado
    face_encoding = face_recognition.face_encodings(image)[0]

    # Imprime el vector de embedding
    print("Vector de embedding del rostro:", face_encoding)
else:
    print("No se detectaron rostros en la imagen.")