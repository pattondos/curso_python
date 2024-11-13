import datetime, os, re

fecha = datetime.date.today()

regex= r'([N][a-z]{3}[-][0-9]{5})'

ruta = os.getcwd() +"\\Mi_Gran_Directorio"

print(f"\nFecha de reporte: {fecha}")
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta {carpeta}")
    print("Las subcrapetas son: ")
    for nom_sub in subcarpeta:
        print(f"\t{nom_sub}")
    print("Los archivos son:")
    for nom_arch in archivo:
        print(f"\t{archivo}")
        arch = open(nom_arch, "r")
        linea = arch.read()
        buscador = re.search(regex, linea)
        
    print("\n")