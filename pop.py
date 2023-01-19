class traingulos():
    def __init__(self):
        self.lado1=int(input("ingrese el valor del  primer lado"))
        self.lado2=int(input("digame cual es el vALOR DEL SEGUNDO LADO"))
        self.lado3=int(input("ingrese el valor del tercer lado"))
        
    def mostrar(self):
        print(" Lado:" self.lado1)
        print(" Lado 2:" self.lado2)
        print(" Lado 3 :" self.lado3)
 
class equilateros(traingulos):
    def __init__(self):
        super().__init__()
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("el triangulo es equilatero")
        else :
            print("el traingulo no es equilatero")
    def Mostrar(self):
        super().mostrar

class escaleno(traingulos):
    def __init__(self):
        super().__init__()
        if self.lado1!=self.lado2 and self.lado1!=self.lado3:
            print("el triangulo es escaleno")
        else:
            print("el traingulo es isoceles")   
    def show(self):
        super().mostrar
#bloque principal
Figura=traingulos()
#Figura.mostrar()
Equilatero=equilateros()
Equilatero.Mostrar()
Escaleno=escaleno()
Escaleno.show()