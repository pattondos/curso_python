import re

#frase = "Si tu me llamas (722-159-1933), nos vamos pa tu casa y nos quedamos en la cama sin pijama"
#patron = r'\d{3}-\d{3}-\d{4}'
#patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

#busqueda = re.search(patron, frase)
#busqueda = re.findall(patron, frase)
#print(busqueda[2])

# for i in re.finditer(patron, frase):
#     print(i.group())
#########################################################################################################
clave = input("Clave: ")
regex = r'\D{1}\w{7}'

buscador = re.search(regex, clave)

print(buscador)