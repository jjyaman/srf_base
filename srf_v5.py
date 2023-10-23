#Este algoritmo detecta los rostros que hay en una imagen 
import cv2

# Cargar el clasificador Haar Cascade pre-entrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# Cargar la imagen o video en el que deseas detectar cabezas
input_image = cv2.imread('C:/Users/SENA/Documents/JJYG/SRF/srf_base/imgs/will_smith_young.jpg')

# Convertir la imagen a escala de grises (la detección de rostros funciona en imágenes en escala de grises)
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Detectar cabezas en la imagen
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Dibujar un rectángulo alrededor de cada cabeza detectada
for (x, y, w, h) in faces:
    cv2.rectangle(input_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con las cabezas detectadas
cv2.imshow('Detección de Cabezas', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
