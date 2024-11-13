#import shutil
import zipfile
import os
# import re

# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

current = os.getcwd()
ruta = "\\DIA_9\\"
ruta_completa = current + ruta
# buscador = re.findall(r"[^\W]+", ruta_completa)
# print(str(buscador[-1:]))


# mi_zip.write(f"{ruta_completa}\\mi_texto_A.txt")
# mi_zip.write(f"{ruta_completa}\\mi_texto_B.txt")
# mi_zip.write(f"{ruta_completa}\\Fechas.py")

# mi_zip.close()

mi_zip_abierto = zipfile.ZipFile(f'{ruta_completa}\\Proyecto+Dia+9.zip', 'r')
mi_zip_abierto.extractall()
##############################################################################
# carpeta_origen = "C:\\Users\\CésarGabrielMedinaTapia\\Documents\\CURSO_PYTHON"
# archivo_destino = "Todo_Comprimido"

# shutil.make_archive(archivo_destino, "zip", carpeta_origen)
##############################################################################
#shutil.unpack_archive("Todo_Comprimido.zip", "Extraccion_Terminada", "zip")
