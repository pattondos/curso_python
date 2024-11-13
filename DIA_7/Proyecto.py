class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellidos, numero_cuenta, saldo_cuenta):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta

    def __str__(self):
        return f"\n{self.nombre} {self.apellido} usted tiene en la cuenta {self.numero_cuenta}: $ {self.saldo_cuenta}"

    def depositar(self, nuevo_saldo):
        self.saldo_cuenta += nuevo_saldo
        print("Se depositó con éxito el dinero.")
        return nuevo_saldo
    
    def retirar(self, retiro_saldo):
        if retiro_saldo < self.saldo_cuenta:
            self.saldo_cuenta -= retiro_saldo
            print("Se depositó con éxito el dinero.")
        else:
            print("No se puede retirar más de lo que tienes en la cuenta.")

def alta_cliente():
    print("Ingresa los datos generales para dar de alta tu cuenta.")
    nombre = str(input("Ingresa tu(s) nombre(s): "))
    apellido = str(input("Ingresa tu(s) apellido(s): "))
    numero_cuenta = str(input("Ingresa tu número de cuenta:"))
    saldo = 0.0
    alta_cliente = Cliente(nombre, apellido, numero_cuenta, saldo)
    return alta_cliente

def inicio():
    cliente = alta_cliente()
    print(cliente)
    bandera_menu = True
    opcion = 0
    
    while (not bandera_menu) or (opcion != 4):
        print("Bienvenidos al Banco posas\nEste es nuestro menú:")
        print("1. Depositar\n2. Retirar\n3. Salir")    
        opcion = int(input("Elige tu opción deseada:"))
        match opcion:
            case 1:
                deposito = float(input("Ingresa cuanto deseas depositar: $"))
                cliente.depositar(deposito)
                print(cliente)                
            case 2:
                retiro = float(input("Ingresa cuanto deseas retirar: $"))
                cliente.retirar(retiro)
                print(cliente) 
            case 3:
                print("Gracias por venir.")
                bandera_menu = False
                break
inicio()  

    
        