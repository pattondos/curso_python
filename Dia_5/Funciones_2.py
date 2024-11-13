precios_cafe = [('Capuccino', 23.9),('Mokaccino', 39.99), ('Americano', 20.5)]

def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_car0 = ""
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_car0 = cafe
        else:
            pass
    return (cafe_car0, precio_mayor)

cafe, precio = cafe_caro(precios_cafe)
print(f"El café más caro es {cafe}, porque cuesta : ${precio}")