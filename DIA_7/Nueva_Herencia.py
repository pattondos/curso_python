class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Jajaja! :v")
    
    def hablar(self):
        print("K ONDA MORRO")

class Hijo(Madre, Padre):
    pass

class Nieto(Hijo):
    pass

print(Nieto.__mro__)
mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()