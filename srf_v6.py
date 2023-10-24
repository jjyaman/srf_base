# # Este algoritmo extrae el vector numérico de la representación facial de una imagen
# import face_recognition
# import cv2
# from deepface import DeepFace

# # Carga la imagen.
# image = cv2.imread("imgs/will_smith.jpg")

# # Convierte la imagen a escala de grises.
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Función para extraer el recorte del rostro de una imagen
# def get_face_from_image(image, face_coordinates):
#     (x, y, w, h) = face_coordinates
#     image = cv2.equalizeHist(image[y:y+h, x:x+w])
#     return image[y:y+h, x:x+w]

# # Cargar el detector facial DNN
# face_cascade = cv2.dnn.readNetFromCaffe("models/deploy.prototxt")

# # Detectar cabezas en la imagen
# faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# # Dibujar un rectángulo alrededor de cada cabeza detectada
# for (x, y, w, h) in faces:
#     #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     # Obtener las coordenadas del rostro
#     face_coordinates = (x, y, w, h)

# # Almacenamos la imagen recortada
# face = get_face_from_image(image_gray, face_coordinates)

# # Identificamos si existe un rostro 
# face_locations = face_recognition.face_locations(face)

# if face_locations:

#     print("Se encontro un rostro")

#     person = DeepFace.extract_faces(face)[0]

#     # Extrae el vector numérico del rostro
#     person_embedding = person["face"]

#     print(person_embedding)

# else:

#     print("No se encontro un rostro")