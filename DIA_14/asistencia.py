from datetime import datetime
import cv2
import face_recognition as fr
import os, numpy

# Crear BD
ruta_imagenes = os.getcwd()+ "\\images\\employees\\"
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta_imagenes)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta_imagenes}/{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
    
# Codificar imágenes
def codificar_imagenes(imagenes):
    lista_codificada = []
    
    # Pasar las imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    
        # Codificar imágenes
        codificador = fr.face_encodings(imagen)[0]
        
        # Agregar a la lista codificada
        lista_codificada.append(codificador)
        
    return lista_codificada

# Registrar asistencia
def registrar_asistencia(persona):
    
    archivo_ingreso = open("registro.csv", "r+")
    lista_datos = archivo_ingreso.readlines()
    nombres_asistencia = []
    
    for linea in lista_datos:
        ingreso = linea.split(",")
        nombres_asistencia.append([0])
    
    if persona not in nombres_asistencia:
        fecha = datetime.now()
        formato_fecha = fecha.strftime("%H:%M:%S")
        archivo_ingreso.writelines(f"\n{persona}, {formato_fecha}")
        

lista_empleados_codificados = codificar_imagenes(mis_imagenes)

# Tomar una foto desde la webcam
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen
exito,  imagen = captura.read()

if not exito:
    print("No se tomó la foto")
else:
    print("Fotografía capturada, comienza reconocimiento")
    # Reconocer la captura
    cara_captura = fr.face_locations(imagen)
    
    # Codficar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    
    # Buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        
        coincidencia = fr.compare_faces(lista_empleados_codificados, caracodif)
        distancias = fr.face_distance(lista_empleados_codificados, caracodif)
        
        indice_coincidencia = numpy.argmin(distancias)
        
        if distancias[indice_coincidencia] > 0.6:
            print("No existe registro del empleado")
        else:
            print("Bienvenido al trabajo")
            
            nombre = nombres_empleados[indice_coincidencia]
            
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen,
                          (x1, y1),
                          (x2, y2),
                          (255, 0, 0),
                          2)
            
            cv2.rectangle(imagen,
                          (x1, y2 - 35),
                          (x2, y2),
                          (255, 0, 0),
                          cv2.FILLED)
            
            cv2.putText(imagen, 
                        nombre,
                        (x1 + 6, y2 -6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        2)
            
            registrar_asistencia(nombre)
            
            #Mostrar imágen
            cv2.imshow("Foto Web", imagen)
            
            # Mantener la ventana abierta
            cv2.waitKey(0)
  

