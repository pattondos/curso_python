from random import shuffle
#
palitos = ['-', '--', '---', '----']

#
def mezclar(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos

#
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número del 1 al 4: ")
    return int(intento)

#
def verificar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Lavatestaaaaaaaaaaaaaa")
    else:
        print("Nambre estás bien ñango")

    print(f"Te ha tocado{lista[intento - 1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
verificar_intento(palitos_mezclados, seleccion)