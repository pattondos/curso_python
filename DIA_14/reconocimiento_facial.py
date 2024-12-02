import cv2
import face_recognition as fr
import os

ruta_imagenes = os.getcwd() + "\\images\\"

#Cargar imágenes
foto_ctrl = fr.load_image_file(f"{ruta_imagenes}cesar1.jpg")
foto_prb = fr.load_image_file(f"{ruta_imagenes}cesar2.jpg")
# foto_prb = fr.load_image_file(f"{ruta_imagenes}cesar3.jpg")

foto_ctrl = cv2.cvtColor(foto_ctrl, cv2.COLOR_BGR2RGB)
foto_prb = cv2.cvtColor(foto_prb, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_ctrl)[0]
cara_codif_A = fr.face_encodings(foto_ctrl)[0]

# Localizar cara prueba
lugar_cara_B = fr.face_locations(foto_prb)[0]
cara_codif_B = fr.face_encodings(foto_prb)[0]

# Mostrar rectángulos
cv2.rectangle(foto_ctrl,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (255, 0, 0),
              2)

cv2.rectangle(foto_prb,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (255, 0, 0),
              2)


# COMPARAR FOTOS
resultado = fr.compare_faces([cara_codif_A], cara_codif_B)
# resultado = fr.compare_faces([cara_codif_A], cara_codif_B, 0.3) Para cambiar la tolerancia de comparación

# Medida de la distancia
distancia = fr.face_distance([cara_codif_A], cara_codif_B)

# Mostrar resultado en pantalla
cv2.putText(foto_prb,
            f"{resultado} {distancia.round(2)}",
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 0, 0),
            2)

# Mostrar imágenes
cv2.imshow("Foto de control", foto_ctrl)
cv2.imshow("Foto de prueba", foto_prb)

# Mantener programa
cv2.waitKey(0)
