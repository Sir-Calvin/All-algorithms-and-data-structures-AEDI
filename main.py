# MÓDULO PRINCIPAL DE LOS TADS PARA AED I
#Autor: Emiliano Calvacho
#Materia: Algoritmo y Estructura de Datos I
#Profesora: Lic. Virginia Moré

def limpiador_diplay():
	"""Se limpia la pantalla, cuando se presiona la tecla Enter."""
	import os
	input("\nPresione ENTER para continuar")
	os.system('cls')

def mensaje_welcome():
	print("""                   ¡¡¡BIENVENIDO AL PROGRAMA DE LOS TADs!!!

			Aquí usted podrá utilizar diversas funciones que les servirá como
		herramientas a la hora de programar.
			Objetivo: ejemplificar el funcionamiento de estos algoritmos, cada 
		uno de ellos con una características que los distinguen de los demás.
			Usted como usuario tendrá la posibilidad de ingresar por medio de
		las opciones el ejemplo que desee.                                          """)

def menu():
	"""Menu de los TADs."""
	print("Menú del TADs:")
	print("1-Listas enlazadas.")
	print("2-Pilas.")
	print("3-Colas.")
	print("4-Árboles.")
	print("5-Búsquedas.")
	print("6-Ordenamientos iterativos.")
	print("7-Ordenamientos recursivos.")
	print("8-Usando la recursividad.")
	print("9-Implementando diccionarios.")
	print("10-Salir del programa.")
	return input("Ingrese una de las opciones: ")

def opc_incorrecta():
	"""En el caso de que se haya ingresado un dato errado
	salta un mensaje de error."""
	print("Usted a seleccionado una opción incorrecta.")
	print("Por favor, ingrese una opción válida.")

def mensaje_pilacola(pc):
	"""Para el menú de las pilas o de las colas."""
	print("Opciones de las %s: " %pc)
	print("1-%s como TAD." %pc)
	print("2-%s predefinidas." %pc)
	return input("Ingrese una de las opciones: ")

def mensaje_arboles():
	"""Para el menú de los árboles."""
	print("Opciones de los Árboles:")
	print("1-Árboles binarios comunes.")
	print("2-Árboles binario de búsqueda.")
	print("3-Árboles balanceados AVL.")
	print("4-Parse Tree.")
	return input("Ingrese una de las opciones: ")

def opc_tad_pilacola(tad):
	"""Función tanto para el TAD de pila como cola."""
	opc_TAD = '1'
	while opc_TAD != '5':
		print("Opciones de las %s como TAD: "%tad)
		print("1-Insertar un nodo en la %s."%tad)
		print("2-Eliminar el nodo de la %s."%tad)
		print("3-Ver si está vacía.")
		print("4-Imprimir la %s."%tad)
		print("5-Salir de la opciones de %s TAD."%tad)
		opc_TAD = input("Seleccione una opción válida: ")

		limpiador_diplay()

		if opc_TAD == '1':
			# apilar() o encolar()
			if tad == "Pila":
				valor = input("Ingrese el valor del nodo a insertar: ")
				nodo.apilar(valor)
			else:
				valor = input("Ingrese el valor del nodo a insertar: ")
				nodo.encolar(valor)

		elif opc_TAD == '2':
			# desapilar() o descolar()
			if tad == "Pila":
				print("El valor del nodo eliminado es: ",nodo.desapilar())
			else:
				print("El valor del nodo eliminado es: ",nodo.descolar())

		elif opc_TAD == '3':
			# es_vacia()
			print("¿La %s está vacía? :"%tad, nodo.es_vacia())

		elif opc_TAD == '4':
			# imprimirPila() o imprimirCola()
			nodo.imprimir()

		elif opc_TAD == '5':
			print("Saliendo de %s TAD."%tad)

		else:
			opc_incorrecta()

		limpiador_diplay()      

def opc_pre_pilacola(pc):
	"""Función tanto para la pila como cola predefinida."""
	opc_PREDEF = '1'        
	while opc_PREDEF != '7':
		print("Opciones de %s predefinida: "%pc)
		print("1-Insertar un nodo en la %s."%pc)
		print("2-Eliminar el nodo de la %s."%pc)
		print("3-Ver si está vacía.")
		if pc == "Pila":
			print("4-Ver el nodo de la cima de la %s."%pc)
		else:
			print("4-Ver el primer nodo de la %s."%pc)
		print("5-Ver tamaño de la %s."%pc)
		print("6-Imprimir la %s."%pc)
		print("7-Salir de la opciones de %s predefinida."%pc)
		opc_PREDEF = input("Seleccione una opción válida: ")

		limpiador_diplay()

		if opc_PREDEF == '1':
			# apilar() o encolar()
			if pc == "Pila":
				valor = input("Ingrese el valor del nodo a insertar: ")
				nodo.apilar(valor)
			else:
				valor = input("Ingrese el valor del nodo a insertar: ")
				nodo.encolar(valor)

		elif opc_PREDEF == '2':
			# desapilar() o descolar()
			if pc == "Pila":
				print("El valor del nodo eliminado es: ",nodo.desapilar())
			else:
				print("El valor del nodo eliminado es: ",nodo.descolar())

		elif opc_PREDEF == '3':
			# es_vacia()
			print("¿La %s está vacía? :"%pc, nodo.es_vacia())

		elif opc_PREDEF == '4':
			# elementoCima()
			if pc == "Pila":
				print("El elemento de la cima es: ",nodo.elementoCima())
			else:
				print("El elemento primero es: ",nodo.elementoPrimero())

		elif opc_PREDEF == '5':
			# tamaño()
			print("El tamaño de la %s es de: "%pc, nodo.tamaño())

		elif opc_PREDEF == '6':
			# imprimir()
			nodo.imprimir()

		elif opc_PREDEF == '7':
			print("Saliendo de %s predefinida."%pc)

		else:
			opc_incorrecta()

		limpiador_diplay()  

mensaje_welcome()

opc = '1'
while opc != '10':
	limpiador_diplay()
	opc = menu()
	limpiador_diplay()
#--------------------------------------Listas--------------------------------------------
	if opc == '1':
		# Opción de las listas enlazadas
		from listas.lista_enlazada import *
		nodo = ListaEnlazada()
		opc_lista = '1'

		while opc_lista != '8':
			print("Opciones de las listas enlazadas: ")
			print("1-Insertar un nodo en una posición.")
			print("2-Agregar un nodo al final de las listas enlazadas.")
			print("3-Eliminar el nodo según el valor 'x'.")
			print("4-Eliminar el nodo según la posición.")
			print("5-Encuentra la posición del valor en las listas enlazadas.")
			print("6-Iterar por pantalla las listas enlazadas.")
			print("7-Ver la longitud de las listas enlazadas")
			print("8-Salir de la opciones de listas enlazadas.")
			opc_lista = input("Seleccione una opción válida: ")

			limpiador_diplay()
			
			if opc_lista == '1':
				# insert()
				print("AVISO: si es la primera vez que ingresa la pos = 0.")
				pos = int(input("Ingrese la posición a insertar: "))
				valor = input("Ingrese el valor del nodo: ")
				nodo.insert(pos,valor)

			elif opc_lista == '2':
				# append()
				valor = input("Ingrese el valor del nodo a insertar al final: ")
				nodo.append(valor)

			elif opc_lista == '3':
				# remove()
				valor = input("Ingrese el valor del nodo a eliminar: ")
				nodo.remove(valor)

			elif opc_lista == '4':
				# pop()
				d = input("Desea eliminar el último elemento?(si-no): ")
				if d == 'si' or d == 'SI' or d == 'Si':
					print("El dato removido es: ",nodo.pop())
				elif d == 'no' or d == 'NO' or d == 'No':
					pos = int(input("Ingrese la posición del nodo a remover: "))
					print("El dato removido es: ",nodo.pop(pos))
				else:
					opc_incorrecta()

			elif opc_lista == '5':
				# index()
				valor = input("Ingrese el valor del nodo para buscar la posición: ")
				print("El dato '{}' se encuentra en la posición Nº {}".format(valor,nodo.index(valor)))

			elif opc_lista == '6':
				# iterador()
				iterador=IteradorListaEnlazada(nodo.prim)
				for pos in range(0,nodo.len):
					print(iterador.next())
			
			elif opc_lista == '7':
				# len(lista)
				print("La longitud de la lista es: ",nodo.len)
			
			elif opc_lista == '8':
				print("Saliendo de lista enlazada.")

			else:
				opc_incorrecta()

			limpiador_diplay()
#--------------------------------------Pilas---------------------------------------------
	elif opc == '2':
		# Opción de las pilas
		opc_pila = mensaje_pilacola("Pilas")
		
		limpiador_diplay()
		
		if opc_pila == '1':
			# Opción de las pilas como TAD
			from pilas.pila import *
			nodo = Pila()
			opc_tad_pilacola("Pila")

		elif opc_pila == '2': 
			# Opción de la Pila con funciones predefinidas
			from pilas.pila_predef import *
			nodo = PilaPredefinida()
			opc_pre_pilacola("Pila")

		else:
			opc_incorrecta()
#--------------------------------------Colas---------------------------------------------
	elif opc == '3':
		# Opción de las colas
		opc_cola = mensaje_pilacola("Colas")
		limpiador_diplay()

		if opc_cola == '1':
			# Opción de las colas como TAD
			from colas.cola import *
			nodo = Cola()
			opc_tad_pilacola("Cola")

		elif opc_cola == '2':
			# Opción de la Cola con funciones predefinidas
			from colas.cola_predef import *
			nodo = ColaPredefinida()
			opc_pre_pilacola("Cola")

		else:
			opc_incorrecta()
#-------------------------------------Árboles--------------------------------------------
	elif opc == '4':
		# Opción de los 
		opc_arbol = mensaje_arboles()
		
		limpiador_diplay()

		if opc_arbol == '1':
			# Ejemplo deL Binary Tree
			from arboles.binary_tree import *
			print("Ejemplo de una inserción y recorrido de un BT:")
			print("        a      ")
			print("       / \     ")
			print("      b   c    ") 
			print("     /   / \   ")
			print("    d   e   f  ")
			a = BinaryTree("a")
			a.insertLeft("b") 
			a.insertRight("c") 
			a.getLeftChild().insertLeft("d")
			a.getRightChild().insertLeft("e")
			a.getRightChild().insertRight("f") 
			print("\nImprimo el árbol de forma Preorden")
			a.printPreordenTree(0) 
			print("\nImprimo el árbol de forma Inorden")
			a.printInordenTree(0) 
			print("\nImprimo el árbol de forma Postorden")
			a.printPostordenTree(0)  
		
		elif opc_arbol == '2':
			# Opción del ABB
			from arboles.abb import *
			n = ABB(None)
			opc_abb = '1'

			while opc_abb != '8':
				print("Opciones del árbol ABB: ")
				print("1-Insertar un nodo con valor numérico.")
				print("2-Buscar el máximo valor del árbol.")
				print("3-Buscar el mínimo valor del árbol.")
				print("4-Buscar el antecesor del árbol.")
				print("5-Buscar el sucesor del árbol.")
				print("6-Buscar un valor en el árbol.")
				print("7-Imprimir el árbol en formato inorden.")
				print("8-Salir de las opciones del ABB.")
				opc_abb = input("Ingrese una de las opciones: ")

				limpiador_diplay()

				if opc_abb == '1':
					valor = int(input("Ingrese un valor numérico: "))
					n.insert(valor)

				elif opc_abb == '2':
					print("El máximo del Árbol es: ",n.maximo())

				elif opc_abb == '3':
					print("El mínimo del Árbol es: ",n.minimo())

				elif opc_abb == '4':
					print("El antecesor del Árbol es: ",n.antecesor())

				elif opc_abb == '5':
					print("El sucesor del Árbol es: ",n.sucesor())

				elif opc_abb == '6':
					val_busq = int(input("Ingrese el valor buscado: "))
					print("¿El valor buscado existe?: ",n.buscar(val_busq))

				elif opc_abb == '7':
					n.inorder(0)

				elif opc_abb == '8':
					print("Saliendo de ABB.")

				else:   
					opc_incorrecta()            

				limpiador_diplay()
		
		elif opc_arbol == '3':
			# Opción del AVL
			from arboles.avl import *
			tree = AVLTree()
			lista = eval(input("Ingrese una lista de números usando '[]' y ',': "))
			for key in lista:
				tree.insert(key)
			print("Imprimiendo lista ordenada: ", tree.inorder_traverse())
			tree.display()
		
		elif opc_arbol == '4':
			# Opción del Parse Tree
			from arboles.parse_tree import *
			print("RERCORDAR: dejar un espacio entre cada símbolo.")
			expresion = input("Ingrese la expresión para representarlo como Árbol: ")
			ParseTree = buildParseTree(expresion)
			ParseTree.printPostordenTree(0)

		else:
			opc_incorrecta()
#------------------------------------Búsquedas-------------------------------------------
	elif opc == '5':
		# Opción de las búsquedas
		from busquedas.busq import *
		print("Opciones de la búsquedas:")
		print("1-Búsqueda lineal.")
		print("2-Búsqueda binaria.")
		opc_busq = input("Seleccione una opción: ")
		if opc_busq == '1':
			lista = eval(input("Ingrese una lista de números usando '[]' y ',': "))
			valor = int(input("Ingrese el valor a buscar: "))
			pos = busqLineal(lista,valor)
			if pos != -1:
				print("La posición del número en la lista es: ",pos)
			else: 
				print("No se encontró el valor en la lista.")
		elif opc_busq == '2':
			lista = eval(input("Ingrese una lista ORDENADA de números usando '[]' y ',': "))
			valor = int(input("Ingrese el valor a buscar: "))
			pos = busqBinaria(lista,valor)
			if pos != -1:
				print("La posición del número en la lista es: ",pos)
			else: 
				print("No se encontró el valor en la lista.")
		else:
			opc_incorrecta()
#-----------------------------Ordenamientos Iterativos-----------------------------------
	elif opc == '6':
		# Opción de los ordenamientos iterativos
		from ordenamientos.ord_iter import *
		lista = eval(input("Ingrese una lista desordenada de números usando '[]' y ',': "))
		print("Opciones del ordenamiento iterativo:")
		print("1-Bubble Sort.")
		print("2-Insertion Sort.")
		print("3-Selection Sort")
		opc_ord_iter = input("Seleccione una opción: ")
		if opc_ord_iter == '1':
			bubbleSort(lista)
			print("Aquí está la lista ordenada",lista)
		elif opc_ord_iter == '2':
			insertionSort(lista)
			print("Aquí está la lista ordenada",lista)
		elif opc_ord_iter == '3':
			selectionSort(lista)
			print("Aquí está la lista ordenada",lista)
		else:
			opc_incorrecta()
#-----------------------------Ordenamientos Recursivos-----------------------------------
	elif opc == '7':
		# Opciones de los ordenamientos recursivos
		from ordenamientos.ord_rec import * 
		lista = eval(input("Ingrese una lista desordenada de números usando '[]' y ',': "))
		print("Opciones del ordenamiento recursivo:")
		print("1-MergeSort.")
		print("2-QuickSort.")
		opc_ord_rec = input("Seleccione una opción: ")
		if opc_ord_rec == '1':
			print("Aquí está la lista ordenada",mergeSort(lista))
		elif opc_ord_rec == '2':
			print("Aquí está la lista ordenada",quickSort(lista))
		else:
			opc_incorrecta()
#----------------------------------Recursividad------------------------------------------
	elif opc == '8':
		# Ejemplo de recursividad
		print("Con esta función veremos un uso de la recursividad.")
		print("Haremos una función recursiva que me indique qué palabras empiezan con una letra dada.")
		
		lista = eval(input("Ingrese una lista palabras usando '[]', ',' y '': "))
		letra = input("Ingrese una letra (solo una): ")

		def empiezaCon(lista, letra):
			if lista==[]:
				return []
			else:
				if lista[0][0]==letra:
					return [lista[0]]+empiezaCon(lista[1:],letra)
				else:
					return empiezaCon(lista[1:],letra)
		print("La/s palabra/s es/son: ")
		print(empiezaCon(lista,letra))
#----------------------------------Diccionarios------------------------------------------
	elif opc == '9':
		# Ejemplo de diccionario
		print("Con un determinado diccionario vamos a ver las operaciones que se pueden hacer.")
		#---Crear diccionario
		print("\n-Para crear un diccionario se usan llaves '{' '}':")
		diccionario = {"emi":100,"juan":180,"paula":704}
		print("Diccionario ejemplo: ",diccionario)
		#---Eliminando un elemento
		print("\n-Podemos eliminar un elemento con la clave de esta manera: 'del diccionario[clave]'")
		print("Por ejemplo queremos eliminar el elemento con clave emi")
		print("Entonces ponemos del diccionario['emi']")
		del diccionario["emi"]
		print("Y el diccionario actual queda así: ", diccionario)
		#---Cambiar valor
		print("\n-Podemos cambiar el valor de un elemento con la clave así: 'diccionario[clave] = valor_new'")
		print("Por ejemplo queremos cambiar el elemento con clave juan")
		print("Entonces ponemos: diccionario['juan'] = 453")
		diccionario["juan"] = 453
		print("Y el diccionario actual queda así: ", diccionario)
		#---Imprimir valor
		print("\n-Podemos imprimir el valor de uno de las claves del diccionario.")
		print("Queremos ver el valor de la clave 'paula': ",diccionario["paula"])
		#---Crear lista con las claves
		print("\n-Podemos obtener una lista con las claves del diccionario con la función .keys()")
		lista = diccionario.keys()
		print("La lista resultante es: ", lista)
		#---Valor existente o no
		print("\n-Podemos indicar si una clave existe o no con la palabra 'in'")
		print("¿existe la clave 'euge'?: ","euge" in diccionario)
		print("¿existe la clave 'juan'?: ","juan" in diccionario)
		#---Iterar
		print("\n-Podemos iterar un diccionario con un for")
		print("Iteramos el diccionario anterior con formato Clave-Valor:")
		for nombre in diccionario:
			print("Clave: " , nombre , " - " , "Valor: " , diccionario[nombre])
#------------------------------------The End---------------------------------------------
	elif opc == '10':
		# Opción de fin del programa
		print("Fin de la ejecución del programa.\nHave a nice day! ;)")
#-----------------------------------Incorrecto-------------------------------------------
	else:
		# Opción incorrecta
		opc_incorrecta()

# Copiar estas listas para las pruebas (copiarla con los corchetes):
# [5,55,-1,77,60,44,33,100,143,-9]  
# [4,12,34,67,90,120]
# ['ana','armar','piedra','tornado','queso','arte'] --> letra 'a' para usar
# Modelo de expresión para el Parse Tree ( ( 6 - 8 ) + ( 3 * 4 ) )

