# import random
 
# def lanzar_dados():
#     return random.randint(1,6), random.randint(1,6)
 
# def evaluar_jugada(dado1, dado2):
#     suma_dados = dado1 + dado2
#     if suma_dados <= 6:
#         return f"La suma de tus dados es {suma_dados}. Lamentable"
#     elif suma_dados > 6 and suma_dados < 10:
#         return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#     else:
#         return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
#####################################################################################
# lista_numeros = [1,2,15,7,2,8]
 
# def reducir_lista(lista):
#     lista = list(set(lista))
#     lista.sort()
#     lista.pop(-1)
#     return lista
 
# def promedio(lista):
#     valor_medio = sum(lista)/len(lista)
#     return valor_medio
#######################################################################
lista_numeros = [1,2,15,7,2,8]
 
import random
 
def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista