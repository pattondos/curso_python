nombre_archivo = open("prueba.txt")

# linea = nombre_archivo.readline()
# print(linea.upper())

# linea = nombre_archivo.readline()
# print(linea.strip())

# linea = nombre_archivo.readline()
# print(linea)
##########################################
#   print(nombre_archivo.read())
#########################################
# for i in nombre_archivo:
#     print(f"Se escribe: {i}")
#########################################
todas_lineas = nombre_archivo.readlines()
print(todas_lineas.pop(1))

nombre_archivo.close()