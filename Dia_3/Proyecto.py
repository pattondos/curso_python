frase = input("Por favor ingresa una frase, de longitud que deseés: ").lower()
lista_letras = []
print("Ahora ingresarás 3 letras al azar.")
lista_letras.append(input("Ingresa la 1a letra: ").lower())
lista_letras.append(input("Ingresa la 2a letra: ").lower())
lista_letras.append(input("Ingresa la 3a letra: ").lower())
################################################################
palabras = frase.split()
longitud_frase = str(len(palabras))

cantidad_primera_letra = frase.count(lista_letras[0])
cantidad_segunda_letra = frase.count(lista_letras[1])
cantidad_tercera_letra = frase.count(lista_letras[2])

primera_letra = frase[0]
ultima_letra = frase[len(frase) - 1]

reversar = palabras.reverse()
frase_invertida = " ".join(palabras)

busqueda = "Python" in frase
diccionario ={True:'Sí', False:'No'}
#################################################################
print("\n")
print(frase)
print(lista_letras)
print(f"La primera letra de la frase es: {primera_letra}.\nLa última letra de la frase es: {ultima_letra}.")
print(f"La cantidad de letras {lista_letras[0]} en la frase es de: {cantidad_primera_letra}")
print(f"La cantidad de letras {lista_letras[1]} en la frase es de: {cantidad_segunda_letra}")
print(f"La cantidad de letras {lista_letras[2]} en la frase es de: {cantidad_tercera_letra}")
print(f"La cantidad de palabras de la frase es de: {longitud_frase}")
print(f"La frase invertida: {frase_invertida}")
#print(f"La longitud de la frase : {longitud_frase}")
print(f"La palabra Python está en la frase : {diccionario[busqueda]}")

