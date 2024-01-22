from typing import List
from typing import Dict

# Ejercicio 4

def traductorSimple(palabra: str) -> str:
    diccionarioTraductor : dict = {"Hello":"Hola","Everyone":"Todos (para sujetos)", "Bye":["Chau","Adios"], "Thank you":"Gracias"}
    print("\nTraductor inglés a español:")
    if palabra in diccionarioTraductor:
        for word, traduccion in diccionarioTraductor.items():
            if word == palabra:
                respuesta = (f"\n{word}=")
                for x in diccionarioTraductor[palabra]:
                    if respuesta[-1] == "=":
                        respuesta = respuesta + " "+ x
                    else:
                        respuesta = respuesta + ", " + x
                break
        print(respuesta)
    else:
        print("\nLa palabra ingresada no se encuentra en el diccionario...")