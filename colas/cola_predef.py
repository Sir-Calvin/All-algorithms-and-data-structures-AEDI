class ColaPredefinida(object):
	def __init__(self):
		self.items = []

	def encolar(self,x):
		self.items.append(x)

	def descolar(self):
		try:
			return self.items.pop(0)
		except ValueError:
			print("La cola está vacía")

	def es_vacia(self):
		return self.items==[]

	def elementoPrimero(self):
		return self.items[0]

	def tamaño(self):
		return len(self.items)

	def imprimir(self):
		for valor in self.items:
			print(valor)