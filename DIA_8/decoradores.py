def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion

def minuscula(texto):
    print(texto.lower())

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

minuscula("PALABRA")
mayuscula("minusculas")

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula("cesar")
mayuscula_decorada("fede")
#########################################################
# def cambiar_letras(tipo):
#     def mayuscula(texto):
#         print(texto.upper())

#     def minuscula(texto):
#         print(texto.lower())

#     if tipo == "may":
#         return mayuscula
#     elif tipo == "min":
#         return minuscula
    
# operacion = cambiar_letras("may")
# operacion("palabra")
######################################################
# mi_funcion = mayuscula
# mi_funcion("python")
###################################################
# def mayuscula(texto):
#         print(texto.upper())

# def minuscula(texto):
#     print(texto.lower())
# def una_funcion(funcion):
#     return funcion

# una_funcion(mayuscula("césar medina"))


