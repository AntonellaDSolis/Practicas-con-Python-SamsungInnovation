# Ejercicio 2

def elemento_maximo(lista):
    maximo = None
    for elem in lista:
        if maximo is None:
            maximo = elem
        elif maximo < elem:
            maximo = elem
    return maximo

#OTRA FORMA:

def elemento_maximo(lista):
    return max(lista)