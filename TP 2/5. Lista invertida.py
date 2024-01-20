# Ejercicio 5

def lista_invertida(lista):
    listaFinal = []
    contador = len(lista) - 1
    while contador != -1:
        listaFinal.append(lista[contador])
        contador -= 1
    return listaFinal