def arbolTrinario(numero):
	return [numero, [], [], []]

def insertaEnArbolTrinario(arbol,numero):
	if arbol==[]:
		arbol+=arbolTrinario(numero)
	elif numero < arbol[0]:
		insertaEnArbolTrinario(arbol[1],numero)
	elif numero == arbol[0]:
		insertaEnArbolTrinario(arbol[2],numero)
	else:
		insertaEnArbolTrinario(arbol[3],numero)


w = []

for x in (20, 30, 90, 90, 8, 5, 90):
    insertaEnArbolTrinario(w,x)
print(w)
