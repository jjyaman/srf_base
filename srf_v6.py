import numpy as np
from deepface import DeepFace

archivo_txt = "C:/Users/SENA/Documents/JJYG/SRF/srf_base/vector/embeddings.txt"

tupac = DeepFace.extract_faces("imgs/tupac_shakur.jpg")

# Extrae el vector numérico de Tupac.
tupac_embedding = np.array(tupac[0])

# Guarda el vector numérico en un archivo de texto.
with open(archivo_txt, "a") as archivo:
    archivo.write(" ".join(str(tupac_embedding)) + "\n")


# # Convierte los diccionarios a matrices.
# tupac_array = np.array(tupac["face"])
# will_young_array = np.array(will_young["face"])

# # Multiplica las matrices.
# similarity = np.dot(tupac_array, will_young_array)

# print(similarity)