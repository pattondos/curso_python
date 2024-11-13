#import time
import timeit

declaracion = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
    lista = []
    for i in range(1, numero + 1):
        lista.append(i)
    return lista
'''
duracion = timeit.timeit(declaracion, mi_setup, number = 100000)
print(duracion)


declaracion_2 = '''
prueba_while(10)
'''

mi_setup_2 = '''
def prueba_while(numero):
    lista = []
    contador = 0
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
duracion_2 = timeit.timeit(declaracion_2, mi_setup_2, number = 100000)
print(duracion_2)

# inicio = time.time()
# prueba_for(20000000)
# final = time.time()
# print(final - inicio)


# inicio = time.time()
# prueba_while(20000000)
# final = time.time()
# print(final - inicio)