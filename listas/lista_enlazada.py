class _Nodo(object):
	def __init__(self,dato=None,prox=None):
		self.dato=dato
		self.prox=prox
	def __str__(self):
		return str(self.dato)

class ListaEnlazada(object):
	def __init__(self):
		self.prim=None
		self.len=0

	def __len__(self):
		return self.len

	def pop(self, i=None):
		if i==None:
			i=self.len-1
		try: 
			if i==0:
				dato=self.prim.dato
				self.prim=self.prim.prox
			else:
				n_ant=self.prim
				n_act=n_ant.prox
				for pos in range(1,i):
					n_ant=n_act
					n_act=n_ant.prox
				dato=n_act.dato
				n_ant.prox=n_act.prox
			self.len -=1
			return dato
		except:
			if (i<0) or (i>=self.len):
				print("Indice fuera de rango")

	def remove(self, x):
		if self.len == 0:
			print("Lista vacía")
		elif self.prim.dato == x:
			self.prim = self.prim.prox
		else:
			n_ant = self.prim
			n_act = n_ant.prox
			while n_act != None and n_act.dato != x:
				n_ant = n_act
				n_act = n_ant.prox
			if n_act == None:
				print("El valor no está en la lista")
			else:
				n_ant.prox = n_act.prox
		self.len -= 1


	def insert(self, i, x):
		try:
			nuevo = _Nodo(x)
			if i == 0:
				nuevo.prox = self.prim
				self.prim = nuevo
			else:
				n_ant = self.prim
				for pos in range(1,i):
					n_ant = n_ant.prox
				nuevo.prox = n_ant.prox
				n_ant.prox = nuevo
			self.len += 1
		except:
			if(i > self.len) or (i < 0):
				print("Posición inválida")

	def append(self, x):
		nuevo = _Nodo(x)
		if self.len == 0:
			self.prim = nuevo
		else:
			n_ant = self.prim
			for pos in range(1,self.len):
				n_ant = n_ant.prox
			n_ant.prox = nuevo
		self.len += 1

	def index(self, x):
		if self.len == 0:
			print("Lista vacía")
		n_act = self.prim
		for valor in range(0,self.len):
			if n_act.dato != x:
				n_act = n_act.prox
			else:
				return valor
		if n_act == None:
			print("El valor no está en la lista")

	def __iter__(self):
		return IteradorListaEnlazada(self.prim)

class IteradorListaEnlazada(object):
	def __init__(self, prim):
		self.actual = prim

	def next(self):
		if self.actual == None:
			print("No hay más elementos en la lista")
		dato = self.actual.dato
		self.actual = self.actual.prox
		return dato
