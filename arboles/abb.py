#TAD de Árbol Binario de Búsqueda
class ABB(object):
	"""Clase de ABB""" 
	def __init__(self, data):
		"""Constructor del ABB: Creo un nodo con el valor que
		se instancia e inicializo tanto los dos hijos con None."""
		self.right = None 
		self.left = None 
		self.data = data 

	def setRootVal(self,obj):
		"""Configuro la raíz.""" 
		self.data = obj

	def getRootVal(self):
		"""Obtengo la raíz."""
		return self.data

	def getChildLeft(self):
		"""Obtengo el hijo izquierdo."""
		return self.left

	def getChildRight(self):
		"""Obtengo el hijo derecho."""
		return self.right

	def insert(self, data):
		"""Inserto tanto por izquiera o por derecha según la regla
		de los ABB. Cuando el k>dato_arbol se inserta por derecha
		y cuando k<dato_arbol se inserta por izquierda.""" 
		if self.data: 
			if data < self.data: 
				if self.left == None: 
					self.left = ABB(data) 
				else: 
					self.left.insert(data) 
			elif data > self.data: 
				if self.right == None: 
					self.right = ABB(data) 
				else: 
					self.right.insert(data) 
		else: 
			self.data = data 

	def inorder(self,n): 
		"""Recorro el BT: subárbol izquierdo, raíz y subárbol derecho."""
		if self.left:
			self.left.inorder(n+1)
		print("Nivel Nº: " + str(n) + " = " + str(self.data))
		if self.right:
			self.right.inorder(n+1)	

	def maximo(self):
		"""Busco el nodo con el máximo valor. Por se ABB siempre
		se encuentra el que está más a la derecha del árbol."""
		if self.right:
			return self.right.maximo()
		return self.data

	def minimo(self):
		"""Busco el nodo con el mínimo valor. Por se ABB siempre
		se encuentra el que está más a la izquierda del árbol."""
		if self.left:
			return self.left.minimo()
		return self.data

	def sucesor(self):
		"""Se busca el sucesor del árbol (o sea de su raíz), 
		no necesariamente es el hijo."""
		if self.right:
			return self.right.minimo()
		y = self.dato
		while y and self == y.right:
			self = y
			y = y.dato
		return y

	def antecesor(self):
		"""Se busca el antecesor del árbol (o sea de su raíz), 
		no necesariamente es el hijo."""
		if self.left:
			return self.left.maximo()
		y = self.dato
		while y and self == y.left:
			self = y
			y = y.dato
		return y

	def buscar(self, x):
		if x != self.data:
			if self.data > x:
				if self.left: 
					return self.left.buscar(x)
				else:
					return False
			else:
				if self.right: 
					return self.right.buscar(x)
				else:
					return False
		if self.data == x:
			return True