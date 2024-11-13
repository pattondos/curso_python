from random import *
intentos = 0
numero_adivinado = False
auxiliar_contador = 8

numero_correcto = randint(1,100)

print("Bienvenido a 'Adivina el número'!")
print("El objetivo del juego es adivinar un número secreto. Esté número será entre 1 y 100")
print("Después de cada intento, recibirás una retroalimentación para ayudarte.")
print("¡Vamos a empezar!")



while not numero_adivinado:
    intentos += 1
    
    print(f"Te quedan {auxiliar_contador} intentos")
    numero_usuario = int(input("Digita el número que crées que sea el correcto: "))
    
    if numero_usuario == numero_correcto:
        print(f"¡LO CONSEGUISTE! El número correcto es: {numero_correcto}\n Lo hiciste en {intentos} intentos.")
        print("¡Gracias por juegar! Si la ves, me la saludas :v")
        numero_adivinado = True
        break

    elif ((numero_usuario < 1) or (numero_usuario > 100)):
        print(f"¡TE PASASTE MAIK :v! El número que escribiste es menor/mayor al rango permitido.\nTe la bativuelas intenta otra vez.")
    elif numero_usuario < numero_correcto:
        print(f"¡TE QUEDAS FRIO! El número que escribiste es menor al numero que elegí.\nSígue intentanto.")
    elif numero_usuario > numero_correcto:
        print(f"¡TE QUEMASTE MIJO! El número que escribiste es mayor al numero que elegí.\nSígue intentanto.")
    elif numero_usuario != numero_correcto:
        print(f"¡NO PUS NO, NO FURULAS! El número que escribiste NI ES IGUAL  numero que elegí.\nSígue intentanto.")
    auxiliar_contador -= 1
    if intentos == 8:
        print(f"NI MODO MAIK, el número era {numero_correcto}, O...")
        print("¡LA REGASTES MAIK! NI MODO SUERTE PARA LA PRÓXIMA, O...")
        nuevo_ingreso = str(input("¿Acaso deseas intentar nuevamente? [s/n]: ").lower())

        if nuevo_ingreso == 's':
            print("Venga pues...\nPero será con diferente número...")
            numero_correcto = randint(1,100)
            numero_adivinado = False
            intentos = 0
            auxiliar_contador = 8

        elif nuevo_ingreso == 'n':
            print("Te la lavas :v")
            numero_adivinado = True