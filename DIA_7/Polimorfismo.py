class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Mow!")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Beeeee!")

vaca= Vaca("Clara bella")
oveja = Oveja("Dolly")

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca)

# animales = [vaca, oveja]

# for i in animales:
#     i.hablar()