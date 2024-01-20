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