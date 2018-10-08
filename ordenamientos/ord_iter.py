#Algoritmos de ordenación de forma iterativa
def bubbleSort(lista):
	"""Ordenamiento burbuja: recibe una lista desordenada y la ordena.
	En caso de detectar que la lista está ordenada entonces no hace 
	corta antes el recorrido."""
	intercambio = True
	numPass = len(lista) - 1
	while numPass > 0 and intercambio:
		intercambio = False
		for i in range(numPass):
			if lista[i] > lista[i+1]:
				intercambio = True
				temp = lista[i]
				lista[i] = lista[i+1]
				lista[i+1] = temp
		numPass = numPass - 1
#------------------------------------------------------------------
def insertionSort(lista):
	"""Ordenamiento por inserción: recibe una lista desordenada y
	la ordena."""
	for i in range(1,len(lista)):
		valorActual = lista[i]
		pos = i
		while pos > 0 and lista[pos-1] > valorActual:
			lista[pos] = lista[pos-1]
			pos = pos - 1
		lista[pos] = valorActual
#------------------------------------------------------------------
def selectionSort(lista):
	"""Ordenamiento por selección: recibe una lista desordenada y
	la ordena."""
	n = len(lista) - 1
	while n > 0:
		p = buscar_max(lista,0,n)
		lista[p], lista[n] = lista[n], lista[p]
		n -= 1
		
def buscar_max(lista, ini, fin):
	"""Busca el máximo número para el ordenamiento de selección"""
	pos_max = ini
	for i in range(ini+1,fin+1):
		if lista[i] > lista[pos_max]:
			pos_max = i
	return pos_max