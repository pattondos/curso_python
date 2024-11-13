import cv2
import face_recognition as fr
import os

ruta_imagenes = os.getcwd() + "\\images\\"

#Cargar imágenes
foto_ctrl = fr.load_image_file("cesar1.jpg")
foto_prb = fr.load_image_file("cesar2.jpg")

foto_ctrl = cv2.cvtColor(foto_ctrl, cv2.COLOR_BGR2RGB)
foto_prb = cv2.cvtColor(foto_prb, cv2.COLOR_BGR2RGB)

# Mostrar imágenes
cv2.imshow("Foto de control", foto_ctrl)
cv2.imshow("Foto de prueba", foto_prb)

# Mantener programa
cv2.waitKey(0)
