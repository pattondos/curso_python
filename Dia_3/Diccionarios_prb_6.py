# diccionario = {'v1':'César', 'v2':'Katia', 'v3':'Amor', 'v4':'Gatos'}
# print(diccionario)

# resultado = diccionario['v1']
# print(resultado)
###############################################################################
# cliente = {'nombre':'César', 'apellido':'Medina', 'peso':80, 'talla':1.80}
# resultado = cliente['talla']
# print(resultado)
##############################################################################
# dic = {'v1':'César', 'v2':[10, 20, 30], 'v3':7, 'v4':{'s1':'JS', 's2':'Java'}}
# resultado = dic['v4']['s1']
# print(resultado)
###############################################################################
# dic = {'v1':['a', 'b', 'c'], 'v2':['d', 'e', 'f']}
# resultado = dic['v2'][1].upper()
# print(resultado)
###############################################################################
dic = {1:'a', 2:'d'}
print(dic)

dic[3] = 'g'
print(dic)

dic[2] = 'D'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
###############################################
# mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
# print(mi_dict["puntos"]["points2"][1])