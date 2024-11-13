from random import choice
#
palabras = ['IMPORTAR', 'PYTHON', 'CESAR', 'KATIA']

palabra_adivinada = False
auxiliar_contador = 6

print("Bienvenido a 'El ahorcado'!")
print("El objetivo del juego es adivinar una palabra secreta. Sino hace la automorición :v")
print("Después de cada intento, recibirás una retroalimentación para ayudarte.")
print("¡Vamos a empezar!")
#
def mezclar(lista_palabras):
    palabra_elegida = ""
    palabra_elegida = choice(lista_palabras)
    return palabra_elegida

#
def probar_suerte(palabra_elegida):
    intento = ''
    print(f"Tu palabra a adivinar tiene {len(palabra_elegida)} letras")
    while intento not in ['A', 'B', 'C',]:
        intento = input("Elige una letra: ")
    return str(intento.upper())

#
def verificar_intento(palabra_correcta, intento):
    intentos = 0
    lista_palabra_unida = [] 
    while not palabra_adivinada:
        intentos += 1
    
        print(f"Te quedan {auxiliar_contador} intentos")
                
        if intento in palabra_correcta:
            lista_palabra_unida.append(intento)
            for letra in lista_palabra_unida:
                
                if lista_palabra_unida.sort() == palabra_correcta:
                    print(f"¡LO CONSEGUISTE! La palabra es: {palabra_correcta}\n Lo hiciste en {intentos} intentos.")
                    print("¡Gracias por juegar! Si la ves, me la saludas :v")
                    palabra_adivinada = True
                elif lista_palabra_unida != palabra_correcta:
                    pass
            #break

    if intentos == 6:
        print(f"NI MODO MAIK, se murió el perro, la palabra era: {palabra_correcta}.")
        print("¡LA REGASTES MAIK! SUERTE PARA LA PRÓXIMA, O...")
        nuevo_ingreso = str(input("¿Acaso deseas intentar nuevamente? [s/n]: ").lower())

        if nuevo_ingreso == 's':
            print("Venga pues...\nPero será con otra palabra...")
            mezclar(palabras)
            seleccion = probar_suerte(palabras_mezcladas)
            verificar_intento(palabras_mezcladas, seleccion)
            palabra_adivinada = False
            intentos = 0
            auxiliar_contador = 6

        elif nuevo_ingreso == 'n':
            print("Te la lavas :v")
            palabra_adivinada = True

palabras_mezcladas = mezclar(palabras)
seleccion = probar_suerte(palabras_mezcladas)
verificar_intento(palabras_mezcladas.split(), seleccion)