#Algoritmos de búsqueda
def busqLineal(lista,x):
	"""Búsqueda lineal: recibe una lista y un valor a buscar.
	Me devuelve la posición del valor buscado dentro de la 
	lista o -1 en caso de que no se encuentre el valor"""
	c=0
	for i in lista:
		if x == i:
			return c
		c += 1
	return -1
#---------------------------------
def busqBinaria(lista, x):
	"""Búsqueda binaria: recibe una lista ORDENADA y un valor
	a buscar. Me devuelve la posición del valor buscado dentro 
	de la lista o -1 en caso de que no se encuentre el valor"""
	izq = 0 
	der = len(lista) -1 
	while izq <= der:
		medio = (izq+der)//2
		if lista[medio] == x:
			return medio
		elif lista[medio] > x:
			der = medio-1
		else:
			izq = medio+1
	return -1