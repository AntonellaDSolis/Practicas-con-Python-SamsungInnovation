# Ejercicio 9

def elementos_pares(lista):
    for elem in lista:
        if (elem % 2) != 0:
            lista.remove(elem)
    return lista