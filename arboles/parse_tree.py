#TAD del ParseTree
from pilas.pila_predef import PilaPredefinida
from arboles.binary_tree import BinaryTree

def buildParseTree(fpexp):
	"""Construyo el árbol de análisis sintáctico"""
	fplist = fpexp.split() 
	pStack = PilaPredefinida() 
	eTree = BinaryTree("")

	pStack.apilar(eTree)
	currentTree = eTree
	
	for i in fplist:
		if i == "(":
			currentTree.insertLeft("")
			pStack.apilar(currentTree)
			currentTree = currentTree.getLeftChild() 

		elif i not in ["+", "-", "/", "*", ")"]:
			currentTree.setRootVal(int (i))
			parent = pStack.desapilar()
			currentTree = parent

		elif i in ["+", "-", "/", "*"]:
			currentTree.setRootVal(i)
			currentTree.insertRight("")
			pStack.apilar(currentTree)
			currentTree = currentTree.getRightChild()

		elif i == ")":
			currentTree = pStack.desapilar()

		else:
			print("No se contempla el carácter evaluado")

	return eTree
