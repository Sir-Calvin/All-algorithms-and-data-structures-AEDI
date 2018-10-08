#Algoritmos de ordenación de forma recursiva
def mergeSort(lista):
	"""Ordenamiento de Mezcla: recibo una lista desordenada
	y devuelvo una lista ordenada."""
	if len(lista) < 2:
		return lista
	medio = len(lista) // 2 
	izq = mergeSort(lista[:medio])
	der = mergeSort(lista[medio:])
	return merge(izq,der)

def merge(lista1,lista2):
	"""Función que utiliza MergeSort para mezclar las sublistas."""
	i,j = 0,0
	resultado = []
	while i<len(lista1) and j<len(lista2):
		if (lista1[i] < lista2[j]):
			resultado.append(lista1[i])
			i += 1
		else:
			resultado.append(lista2[j])
			j += 1
	resultado += lista1[i:]
	resultado += lista2[j:]
	return resultado
#------------------------------------------------------------------
def quickSort(lista):
	"""Ordenamiento Rápido: recibo una lista desordenada
	y devuelvo una lista ordenada."""
	if len(lista) < 2: 
		return lista 
	menores, medio, mayores = _partition(lista)
	return quickSort(menores) + medio + quickSort(mayores) 
	
def _partition(lista):
	"""Función que utiliza QuickSort para particionar la
	lista en tres sublistas."""
	pivote = lista[0]
	menores = []
	mayores = []
	for x in range(1,len(lista)):
		if lista[x] < pivote:
			menores.append(lista[x])
		else:
			mayores.append(lista[x])
	return menores, [pivote], mayores