# Ejercicio 8

def ordenar_lista(lista):
    listaFinal = []
    while len(lista) != 0:
        listaFinal.append(min(lista))
        lista.remove(min(lista))
    return listaFinal