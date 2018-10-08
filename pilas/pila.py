class _Nodo(object):
	def __init__(self, dato = None, prox = None):
		self.dato = dato
		self.prox = prox
	def __str__(self):
		return self.dato

class Pila(object):
	def __init__(self):
		self.ultimo = None

	def apilar(self,x):
		nuevo = _Nodo(x)
		if self.ultimo:
			nuevo.prox = self.ultimo
			self.ultimo = nuevo
		else:
			self.ultimo = nuevo

	def desapilar(self):
		if self.ultimo:
			valor  = self.ultimo.dato
			self.ultimo = self.ultimo.prox
			return valor
		else:
			print("Pila Vacía.")

	def es_vacia(self):
		return self.ultimo == None

	def imprimir(self):
		if self.es_vacia()==True:
			print("Pila vacia.")
		else:
			validar = True
			temp = self.ultimo
			while(validar):
				print(temp.__str__())
				if temp.prox == None:
					validar = False
				else:
					temp = temp.prox