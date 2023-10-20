import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

# Creamos una instancia de 'Face Mesh', la cual utilizaremos para detectar y rastrear los rostros
mp_face_mesh = mp.solutions.face_mesh
# Creamos una instancia de 'Drawing Utils', la cual utilizaremos para dibujar 'Landmarks' en los rostros
mp_drawing = mp.solutions.drawing_utils

# Cargamos el modelo FaceNet
model_facenet = tf.saved_model.load("C:/Users/SENA/Documents/JJYG/SRF/20180402-114759/")

# Inicializamos la captura de video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Creamos la función para normalizar los landmarks entre 0 y 1
def normalize_landmarks(landmarks):
    # Se debe calcular las coordenadas mínimas y máximas y luego aplicar una transformación lineal  
    min_coords = np.min(landmarks, axis=0)
    max_coords = np.max(landmarks, axis=0)
    normalized_landmarks = (landmarks - min_coords) / (max_coords - min_coords)
    return normalized_landmarks

with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=3,
    min_detection_confidence=0.5) as face_mesh:

    # Bucle para procesar cada frame del video
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Llamamos a la función `process` del detector de rostros con el frame en formato RGB
        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks is not None:
            for face_landmarks in results.multi_face_landmarks:
                
                # Se convierten los 'Landmarks' en un Array de 'Numpy'
                landmarks = np.array([(lmk.x, lmk.y) for lmk in face_landmarks.landmark])

                # Normalizamos los valores de los landmarks entre 0 y 1
                landmarks = normalize_landmarks(landmarks)

                # Asumiendo que el modelo FaceNet espera landmarks normalizados en el rango (-1, 1)
                landmarks_normalized = (landmarks - 0.5) * 2  # Normalizar a (-1, 1)

                # Reformatear para que coincida con el formato de entrada del modelo FaceNet
                landmarks_reshaped = landmarks_normalized.reshape(1, 3, 96, 96)

                # Calcular el vector embedding del rostro
                embedding = model_facenet.forward(landmarks_reshaped)

                # Imprimir el vector embedding
                print(embedding)

                # Dibujamos los 'Landmarks' en el rostro detectado, además generar sus relaciones
                mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=1, circle_radius=1), connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1))


        # Mostramos los frames procesados, o sea el vídeo
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()