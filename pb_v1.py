# import os

# # Verifica que el archivo exista.
# if os.path.exists("C:/Users/SENA/Documents/JJYG/SRF/srf_base/vector/embeddings.txt"):
#     # La ruta es correcta.
#     print("Sí")
# else:
#     print("No")
#     # La ruta es incorrecta.

# ************************************************************************************************** #

# import cv2

# facenet = cv2.dnn.readNet("C:/Users/SENA/Documents/JJYG/SRF/20180402-114759/20180402-114759.pb")

# # Verificamos si el modelo es compatible
# if facenet is None:
#     print("El archivo de modelo no es compatible con OpenCV.")
# else:
#     print("El archivo de modelo es compatible con OpenCV.")

# ************************************************************************************************** #

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

for elemento_a in a:
    for elemento_b in b:
        if elemento_a == elemento_b:
            print(f"Elemento de 'a' ({elemento_a}) es igual al elemento de 'b' ({elemento_b})")
        else:
            print(f"Elemento de 'a' ({elemento_a}) no es igual al elemento de 'b' ({elemento_b})")
