class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("¡Pio-Pio!")
    
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")
        self.piar()
    
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora tienes el pájaro {self.color}.")
    
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pájaro mira")


mi_pajaro = Pajaro('Azul', 'Guacamayo')
print(f"Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.")
mi_pajaro.piar()
mi_pajaro.volar(50)
mi_pajaro.pintar_negro()

Pajaro.poner_huevos(5)
Pajaro.mirar()
