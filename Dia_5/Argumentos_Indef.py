# def suma(*args):
#     total = 0 
#     for i in args:
#         total += i
#     return total

# print(suma(1,2,3,4,5,6,7,8))
############################################
# def suma(*args):
#     return sum(args)

# print(suma(1,2,3,4))
############################################
# def suma(**kwargs):
#     total = 0
#     for i, j in kwargs.items():
#         print(f"{i}={j}")
#         total += j
#     return total
# print(suma(x=3,y=4,z=5))
############################################
def suma(num1, num2, *args, **kwargs):
    print(f"{num1}")
    print(f"{num2}")
    
    for i in args:
        print(f"Argumento: {i}")

    for i, j in kwargs.items():
        print(f"Argumentos: {i} y {j}")

args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

suma(34,56, *args, **kwargs)
#print(suma(34,56,123,456,678,x='uno',y='dos',z='tres'))
######################################################################
def lista_atributos(**kwargs):
    lista = []
    for i, j in kwargs.items():
        lista.append(j)
    return lista
kwargs = {'1':'uno', '2':'dos', '3':'tres'}    
print(lista_atributos(**kwargs))