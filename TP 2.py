# Ejercicio 1

def suma_elementos(lista) -> int:
    sumatoria = 0
    for elem in lista:
        sumatoria = sumatoria + elem
    return sumatoria

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

# Ejercicio 3

def eliminar_duplicados(lista):
    listaFinal = []
    for elem in lista:
        if not elem in listaFinal:
            listaFinal.append(elem)
    return listaFinal

def eliminar_duplicados2(lista):
    listaFinal = []
    for elem in lista:
        cant = 0
        print("Elem")
        print(elem)
        for new in lista:
            if elem == new:
                cant = cant + 1
            print(cant)
        if (cant == 1) :
            listaFinal.append(elem)
        else:
            coincidencia = False
            for valor in listaFinal:
                if(valor == elem):
                    coincidencia = True
            if(coincidencia == False):
                listaFinal.append(elem)            
    return listaFinal

print(eliminar_duplicados2([1,2,3,4,5,2,2,2,3,5]))
# Ejercicio 4

def lista_al_cuadrado(lista):
    listaFinal = []
    for elem in lista:
        elemAlCuadrado = elem * elem
        listaFinal.append(elemAlCuadrado)
    return listaFinal

# Ejercicio 5

def lista_invertida(lista):
    listaFinal = []
    contador = len(lista) - 1
    while contador != -1:
        listaFinal.append(lista[contador])
        contador -= 1
    return listaFinal

# Ejercicio 6

def contar_elemento(lista, elemento):
    contador = 0
    for elem in lista:
        if elem == elemento:
            contador += 1
    return contador

# Ejercicio 7

def combinar_listas(lista1, lista2):
    lista = lista1 + lista2
    return (eliminar_duplicados (lista)) 

# Ejercicio 8

def ordenar_lista(lista):
    listaFinal = []
    while len(lista) != 0:
        listaFinal.append(min(lista))
        lista.remove(min(lista))
    return listaFinal

# Ejercicio 9

def elementos_pares(lista):
    for elem in lista:
        if (elem % 2) != 0:
            lista.remove(elem)
    return lista

# Ejercicio 10

def palabra_mas_larga(lista):
    max = None
    for elem in lista:
        if max is None:
            max = elem
        elif len(max) < len(elem): #devuelve el primer elemento con más letras encontrado.
            max = elem
    return max