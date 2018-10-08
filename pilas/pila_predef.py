class PilaPredefinida(object):
	def __init__(self):
		self.items = []

	def apilar(self,x):
		self.items.append(x)

	def desapilar(self):
		try:
			return self.items.pop()
		except ValueError:
			print("La pila está vacía")

	def es_vacia(self):
		return self.items==[]

	def elementoCima(self):
		return self.items[len(self.items)-1]

	def tamaño(self):
		return len(self.items)

	def imprimir(self):
		for i in range(len(self.items)-1,-1,-1):
			print(self.items[i])