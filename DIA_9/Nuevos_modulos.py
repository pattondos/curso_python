import os
# import shutil
# import send2trash

# archivo = open('curso.txt', 'w')
# archivo.write('Texto de prueba')
# archivo.close()

# print(os.listdir())

ruta = 'C:\\ACI'

for i,j,k in os.walk(ruta):
    print(f"En la carpeta {i}")
    print("Las subcrapetas son: ")
    for l in j:
        print(f"\t{l}")
    print("Los archivos son:")
    for m in k:
        print(f"\t{m}")
    print("\n")



# shutil.move('curso.txt', 'C:\\Users\\CésarGabrielMedinaTapia\\Desktop')

# send2trash.send2trash()