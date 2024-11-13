# lista = ['a', 'b', 'c', 'd']
# for i in lista:
#     posicion_letra = lista.index(i) + 1
#     print(f"Letra: {i}")
#     print(f"La letra {i} está en la posición {posicion_letra}")
##################################################################
# numeros = [1, 2, 3, 4, 5, 6]
# valor = 0
# for i in numeros:
#     valor += i 
#     print(valor)
##################################################################
# palabra = 'Python'
# for i in palabra:
#     print(i)
#################################################################
# for i, j in [[1, 2], [3, 4], [5, 6]]:
#     print(f"Objeto i: {i}")
#     print(f"Objeto j: {j}")
#################################################################
# diccionario = {'c1':'a', 'c2':'b', 'c3':'c'}
# for i in diccionario:
#     print(diccionario[i])
# for i, j in diccionario.items():
#     print(i, j)
#################################################################
# lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
# for i in lista_numeros:
#     if i < 0:
#         break
#     else:
#         print(i)
#################################################################
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for i in lista_numeros:
    residuo = (i%2)
    if (residuo == 0):
        suma_pares += i
        # print(f"La suma del número par {i} es:{suma_pares}")
        print(suma_pares)
    elif (residuo == 1):
        suma_impares += i
        # print(f"La suma del número impar {i} es:{suma_impares}")
        print(suma_impares)