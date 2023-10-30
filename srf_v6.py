import cv2
import dlib

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

# Crear el detector de rostros
detector = dlib.get_frontal_face_detector()

while True:
    # Leer el frame actual
    ret, frame = cap.read()

    if not ret:
        break

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el frame
    faces = detector(gray)

    # Dibujar rectángulos alrededor de los rostros detectados
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el frame
    cv2.imshow("frame", frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
