from typing import List
from typing import Dict

# Ejercicio 2

def calculadoraDeEstadistica (lista : list) -> dict:
    diccionario = {}
    diccionario ["suma"] = sum(lista)
    diccionario["promedio"] = (sum(lista)/len(lista))
    diccionario["minimo"] = min(lista)
    diccionario["maximo"] = max(lista)
    return diccionario 