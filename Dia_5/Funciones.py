# def mi_funcion (nombre):
#     print(f"Kámara {nombre} te la lavas :v")
# mi_funcion("Cesar")
####################################################
# def multiplicar (num1, num2):
#     total = num1 * num2
#     return total
# resultado = multiplicar(2,2)
# print(resultado)
#####################################################
def verifica_3_cifras(lista_numeros):
    lista_3_cifras = []
    for i in lista_numeros:
        if i % 2 ==0:
            lista_3_cifras.append(i)
        else:
            pass
    return lista_3_cifras

resultado = verifica_3_cifras([35,99,900])
print(resultado)