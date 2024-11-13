# lista_palabras = ['Hola','Mundo','soy', 'Tu papi']
# archivo = open("prueba.txt", "a")
# archivo.write('''
#     que
#     onda perros 
#     infelices
# ''')
# for i in lista_palabras:
#     archivo.writelines(i + '\n')

# archivo.close()
#######################################################3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("registro.txt", "a")
for i in registro_ultima_sesion:
    archivo.writelines(f"\t{i}")

archivo.close()
archivo = open("registro.txt", "r")
print(archivo.read())