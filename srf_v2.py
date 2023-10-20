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

# Cargamos la imagen estática
image_path = "imgs/will_smith.jpg"

# Capturamos la imagen especificada en la ruta
image = cv2.imread(image_path)

# Asegúrate de que la imagen se haya cargado correctamente
if image is not None:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Generamos la instancia para el detector de rostros de 'MediaPipe'
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,  # Procesar solo un rostro en la imagen
        min_detection_confidence=0.5) as face_mesh:

        # Procesamos la imagen
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks:
            # Extraemos los landmarks del primer rostro detectado
            face_landmarks = results.multi_face_landmarks[0]

            # Se convierten los 'Landmarks' en un Array de 'Numpy'
            landmarks = np.array([(lmk.x, lmk.y) for lmk in face_landmarks.landmark])

            # Normalizamos los valores de los landmarks entre 0 y 1
            min_coords = np.min(landmarks, axis=0)
            max_coords = np.max(landmarks, axis=0)
            normalized_landmarks = (landmarks - min_coords) / (max_coords - min_coords)

            # Asumiendo que el modelo FaceNet espera landmarks normalizados en el rango (-1, 1)
            landmarks_normalized = (normalized_landmarks - 0.5) * 2  # Normalizar a (-1, 1)

            # Reformatear para que coincida con el formato de entrada del modelo FaceNet
            landmarks_reshaped = landmarks_normalized.reshape(1, 3, 96, 96)

            # Calcular el vector embedding del rostro
            embedding = model_facenet.forward(landmarks_reshaped)

            # Imprimir el vector embedding
            print(embedding)

            # Dibujamos los 'Landmarks' en la imagen
            mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=1, circle_radius=1), connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1))

        # Mostrar la imagen con los landmarks
        cv2.imshow("Image with Landmarks", image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

else:
    print("No se pudo cargar la imagen.")