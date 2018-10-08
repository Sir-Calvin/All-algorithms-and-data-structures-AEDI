#TAD de Árbol Binario
class BinaryTree(object):
	"""Clase del Binary Tree"""
	def __init__(self, data):
		"""Constructor del BT: Creo un nodo con el valor que
		se instancia e inicializo tanto los dos hijos con None."""
		self.key = data
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		"""Inserto por izquierda: si el hijo izquierdo está
		vacío lo instancio como BT. Sino voy hasta el hijo
		izquierdo del izquierdo y lo inserto allí."""
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		"""Insertar por derecha: Simétrico a insertar por izquierda."""
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else: 
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t 

	def getRightChild(self): 
		"""Obtengo el hijo derecho."""
		return self.rightChild

	def getLeftChild(self): 
		"""Obtengo el hijo izquierdo."""
		return self.leftChild

	def setRootVal(self, obj):
		"""Configuro la raíz.""" 
		self.key = obj

	def getRootVal(self):
		"""Obtengo la raíz.""" 
		return self.key     

	def printPreordenTree(self, n):
		"""Recorro el BT: raíz, subárbol izquierdo y subárbol derecho."""
		if self.getRootVal() != None: 
			print("Level: "+ str(n) + " : " + str(self.getRootVal()))
			if self.getLeftChild() != None:
				self.getLeftChild().printPreordenTree(n+1)
			if self.getRightChild() != None:
				self.getRightChild().printPreordenTree(n+1)
		return n

	def printInordenTree(self, n):
		"""Recorro el BT: subárbol izquierdo, raíz y subárbol derecho."""
		if self.getRootVal() != None: 
			if self.getLeftChild() != None: 
				self.getLeftChild().printInordenTree(n+1) 
			print("Level: "+ str(n) + " : " + str(self.getRootVal())) 
			if self.getRightChild() != None: 
				self.getRightChild().printInordenTree(n+1) 
		return n 

	def printPostordenTree(self, n):
		"""Recorro el BT: subárbol izquierdo, subárbol derecho y raíz."""
		if self.getRootVal() != None:
			if self.getLeftChild() != None:
				self.getLeftChild().printPostordenTree(n+1)
			if self.getRightChild() != None:
				self.getRightChild().printPostordenTree(n+1) 
			print("Level: "+ str(n) + " : " + str(self.getRootVal())) 
		return n 