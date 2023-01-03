#este es mi primer programa  vamos hacer un oop
class persona():
    def __init__(self):
        self.nombre=input("el nombre de la persona es")
        self.edad=int(input("la edad de  la personas es"))


    def  Mostras(self):
    print("Nombre:" , self.nombre)
    print("Edad:",self.edad )

class Empleado(persona):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("ingrese el sueldo"))

    def Mostrar(self):
        super().Mostrar()
        print("sueldo: ", self.sueldo) 

    def paga_impuestos(self):
        if self.sueldo >= 3000:
            print("debe pagar impuesto")
        else:
            print("no debes de pagar")    


#bloque principal
personas1=persona()
persona1.Mostrar()
empleado1=Empleado()
empleado1.Mostrar()