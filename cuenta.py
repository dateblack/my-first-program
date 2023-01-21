# creamos la clase Cuenta
class Cuenta:
	# inicializamos los atributos de la clase
	def __init__(self,):
		self.titular=input("cual es el nombre del titular")
		self.cantidad=int(input("ingrese la cantidad de dinero"))
 
	# imprimimos los datos
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
 
 
# creamos la clase CajaAhorro
# esta clase hereda atributos de la clase Cuenta
class CajaAhorro(Cuenta):
	# iniciamos los atributos de la clase
	def __init__(self):
		super().__init__()
 
	# imprimimos los datos de la cuenta
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()
 
 
# creamos la clase PlazoFijo
# esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(Cuenta):
	# inicializamos los atributos de la clase
	def __init__(self):
		super().__init__()
		self.plazo=float(int(input("ingrese el plazo")))
		self.interes=float(self.plazo/100)
 
 
	# calculamos la ganancia
	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)
 
 
	# imprimimos los resultados
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()
 
 
# bloque principal
caja1=CajaAhorro()
caja1.imprimir()
 
plazo1=PlazoFijo()
plazo1.imprimir()