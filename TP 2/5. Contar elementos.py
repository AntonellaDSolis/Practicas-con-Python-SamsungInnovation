# Ejercicio 6

def contar_elemento(lista, elemento):
    contador = 0
    for elem in lista:
        if elem == elemento:
            contador += 1
    return contador