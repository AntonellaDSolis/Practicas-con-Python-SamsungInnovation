from typing import List
from typing import Dict

# Ejercicio 1

def contador_de_palabras(texto: str) -> str:
    palabra : str = ""
    dic : dict = {}
    ultima_letra = 1
    for letra in texto:
        if letra != " ":
            palabra = palabra + letra
        if letra == " " or ultima_letra == len(texto):
            if palabra in dic.keys():
                dic[palabra] = dic[palabra]+1
            else:
                dic[palabra] = 1
            palabra = ""
        ultima_letra += 1