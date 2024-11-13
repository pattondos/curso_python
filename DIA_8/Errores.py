# def suma():
#     num_1 = int(input("Ingresar 1er número a sumar: "))
#     num_2 = int(input("Ingresar 2o número a sumar: "))
#     print(num_1 + num_2)
#     print("Gracias por sumar :v")


# try:
#     suma()
# except ValueError:
#     print("LA TAS CAGANDO MAIK SOLO NÚMEROS MIJO :v")
# except TypeError:
#     print("LA TAS CAGANDO MAIK NO SE CONCATENAN DISTINTOS FORMATOS:'C")
# else:
#     print("NO LA KGATS MAIK :3")
# finally:
#     print("ESO ES TODO AMIKOS :'3")
##############################################################################
def pedir_numero():
    while True:
        try:
            numero = int(input("Dame el maldito número: "))
        except:
            print("LA TAS CAGANDO MAIK SOLO NÚMEROS MIJO :v")
        else:
            print(f"Ingresaste el número: {numero}")
            break
    print("BAITS")
pedir_numero()
############################################################
def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")
############################################################
def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
###############################################################
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")