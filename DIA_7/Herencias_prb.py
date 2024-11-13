class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Haz nacido maik, pio pio")

    def hablar(self):
        print("Hablaste maik!")
#########################################################
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("PIO PIO!")

    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros.")

piolin = Pajaro(2, 'Amarillo', 60)
animal = Animal(5, 'Negro')

piolin.nacer()
print(piolin.edad)