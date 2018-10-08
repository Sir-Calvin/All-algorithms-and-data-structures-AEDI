class _Nodo(object):
	def __init__(self, dato = None, prox = None):
		self.dato = dato
		self.prox = prox
	def __str__(self):
		return self.dato

class Cola(object):
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def encolar(self,x):
		nuevo = _Nodo(x)
		if self.ultimo:
			self.ultimo.prox = nuevo
			self.ultimo = nuevo
		else:
			self.primero = nuevo
			self.ultimo = nuevo

	def descolar(self):
		if self.primero:
			valor  = self.primero.dato
			self.primero = self.primero.prox
			if not self.primero:
				self.ultimo  = None
			return valor
		else:
			print("Cola Vacía.")

	def es_vacia(self):
		return self.primero == None

	def imprimir(self):
		if self.es_vacia()==True:
			print("Cola vacia.")
		else:
			validar = True
			temp = self.primero
			while(validar):
				print(temp.__str__())
				if temp == self.ultimo:
					validar = False
				else:
					temp = temp.prox