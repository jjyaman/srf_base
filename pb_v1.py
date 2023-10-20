import os

# Verifica que el archivo exista.
if os.path.exists("imgs/will_smith.jpg"):
    # La ruta es correcta.
    print("Sí")
else:
    print("No")
    # La ruta es incorrecta.


# import cv2

# facenet = cv2.dnn.readNet("C:/Users/SENA/Documents/JJYG/SRF/20180402-114759/20180402-114759.pb")

# # Verificamos si el modelo es compatible
# if facenet is None:
#     print("El archivo de modelo no es compatible con OpenCV.")
# else:
#     print("El archivo de modelo es compatible con OpenCV.")
