# def mi_funcion():
#     lista = []
#     for i in range(1, 5):
#         lista.append(i * 10)
#     return lista


# def mi_generador():
#     for i in range(1, 5):
#         yield i * 10

# print(mi_funcion())
# print(mi_generador())

# gen = mi_generador()
# print(next(gen))
# print(next(gen))
# print(next(gen))
##########################################
def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x
gen = mi_generador()
print(next(gen))
print(next(gen))
print(next(gen))
###########################################


