class NodoTrinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.iguales = []
        self.derecha = None


def insertar_nodo(raiz, valor):
    if raiz is None:
        return NodoTrinario(valor)

    if valor == raiz.valor:
        raiz.iguales.append(valor)
    elif valor < raiz.valor:
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar_nodo(raiz.derecha, valor)

    return raiz


def construir_arbol_trinario(valores):
    raiz = None
    for valor in valores:
        if raiz is None:
            raiz = NodoTrinario(valor)
        else:
            insertar_nodo(raiz, valor)
    return raiz


def generar_salida_arbol_trinario(raiz):
    if raiz is None:
        return "[]"

    salida = "["
    salida += str(raiz.valor)

    if raiz.iguales:
        salida += ", " + str(raiz.iguales)
    else:
        salida += ", [],"

    salida += " " + generar_salida_arbol_trinario(raiz.izquierda)
    salida += ", " + generar_salida_arbol_trinario(raiz.derecha)
    salida += "]"

    return salida


valores_entrada = input().split()
valores_entrada = list(map(int, valores_entrada))

arbol_trinario = construir_arbol_trinario(valores_entrada)

salida = generar_salida_arbol_trinario(arbol_trinario)
print(salida)
