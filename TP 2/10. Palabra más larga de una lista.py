# Ejercicio 10

def palabra_mas_larga(lista):
    max = None
    for elem in lista:
        if max is None:
            max = elem
        elif len(max) < len(elem): #devuelve el primer elemento con más letras encontrado.
            max = elem
    return max