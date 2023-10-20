import os

# Verifica que el archivo exista.
if os.path.exists("C:/Users/SENA/Documents/JJYG/SRF/20180402-114759/20180402-114759.pb"):
    # La ruta es correcta.
    print("Sí")
else:
    print("No")
    # La ruta es incorrecta.


# import cv2

# # Cargamos el modelo
# cv2.dnn.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)

# facenet = cv2.dnn.readNet("C:/Users/SENA/Documents/JJYG/SRF/srf_base/model/modelolbphfface.xml")

# # Verificamos si el modelo es compatible
# if facenet is None:
#     print("El archivo de modelo no es compatible con OpenCV.")
# else:
#     print("El archivo de modelo es compatible con OpenCV.")
