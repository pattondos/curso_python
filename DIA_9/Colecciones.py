from collections import deque

# numeros = [3,4,5,6,7,7,8,8,9,3, 3, 1, 2, 5, 5, 8, 8, 9]

# print(Counter(numeros))
#######################################################
# mi_diccionario = {'uno':'Verde', 'dos':'rojo', 'tres':'Azul'}

# mi_dic = defaultdict(lambda: 'nada')
# mi_dic['uno'] = 'verde'
# print(mi_dic['dos'])
#########################################################
# mi_tupla = (23,343,453)
# Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
# katy = Persona('Katy', 1.58, 60)
# print(katy[2])
###########################################################
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)
lista_ciudades.appendleft('México')
print(lista_ciudades)


