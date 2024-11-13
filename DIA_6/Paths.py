#import os
from pathlib import Path #PureWindowsPath

# ruta = os.chdir('C:\\Users\\CésarGabrielMedinaTa\\Music\\Alternativo')
# archivo = open('Hola.txt')
# print(archivo.read())
# os.rmdir('C:\\Users\\CésarGabrielMedinaTa\\Music\\Alternativo\\nueva')
# os.mkdir('C:\\Users\\CésarGabrielMedinaTa\\Music\\Alternativo\\nueva')
#######################################################################################
#ruta = 'C:\\Users\\CésarGabrielMedinaTa\\Documents\\CURSO_PYTHON\\DIA_6\\prueba.txt'
#elemento = os.path.basename(ruta)
# elemento = os.path.dirname(ruta)
# elemento = os.path.split(ruta)
#print(elemento)
#######################################################################################
# carpeta = Path('/Users/CésarGabrielMedinaTa/Music/Alternativo/Hola.txt')
# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

# if not carpeta.exists():
#     print('Nones maik')
# else:
#     print('Simon we')

# ruta_windows = PureWindowsPath(carpeta)
# print(ruta_windows) 
###########################################################################
# base = Path.home()
# guia = Path(base, "Europa", "Italia", Path("Roma", "El_panteon.txt"))
# guia_2 = guia.with_name("El_castillo_del_angel.txt")
# print(base)
# print(guia.parent)
# print(guia_2)
##########################################################################
# guia = Path(Path.home(), "Europa")

# for i in Path(guia).glob("**/*.txt"):
#     print(i)
##########################################################################
guia = Path("Europa", "Italia", "Roma", "El_panteon.txt")
en_europa = guia.relative_to(Path("Europa"))
en_italia = guia.relative_to(Path("Europa", "Italia"))
print(en_europa)
print(en_italia)
