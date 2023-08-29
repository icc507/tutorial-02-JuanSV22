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
h = input().split(' ')

for x in h:
    insertaEnArbolTrinario(w,int(x))
print(w)
