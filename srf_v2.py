#Este algoritmo traza una 'Face Mesh' en el rostro. Además extrae un 'Vector Embedding' del rostro
import cv2
import mediapipe as mp
import face_recognition 
import numpy as np

# Creamos una instancia de 'Face Mesh', la cual utilizaremos para detectar y rastrear los rostros
mp_face_mesh = mp.solutions.face_mesh
# Creamos una instancia de 'Drawing Utils', la cual utilizaremos para dibujar 'Landmarks' en los rostros
mp_drawing = mp.solutions.drawing_utils

# Cargamos la imagen estática
image_path = "imgs/will_smith.jpg"

# Capturamos la imagen especificada en la ruta
image = cv2.imread(image_path)

ruta_guardado = "C:/Users/SENA/Documents/JJYG/SRF/srf_base/imgs"

# Nos aseguramos que la imagen se haya cargado correctamente
if image is not None:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detectamos los rostros en la imagen utilizando face_recognition
    face_locations = face_recognition.face_locations(image_rgb)
    
    if face_locations:
        # Extraemos la ubicación del primer rostro detectado
        top, right, bottom, left = face_locations[0]

        # Recortamos el rostro de la imagen
        face_image = image[top:bottom, left:right]

        # Obtenemos el vector de embedding utilizando face_recognition.face_encodings
        face_encodings = face_recognition.face_encodings(face_image)

        # Imprimimos el vector de embedding
        print(face_encodings[0])

        # Dibujamos los 'Landmarks' en la imagen
        with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.5) as face_mesh:

            results = face_mesh.process(image_rgb)

            if results.multi_face_landmarks:
                face_landmarks = results.multi_face_landmarks[0]
                mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=1, circle_radius=1), connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1))

        # Mostrar la imagen con los landmarks
        cv2.imwrite(ruta_guardado, image)
        cv2.waitKey(0)

    else:
        print("No se detectaron rostros en la imagen.")
else:
    print("No se pudo cargar la imagen.")

cv2.destroyAllWindows()