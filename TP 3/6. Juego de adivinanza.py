from typing import List
from typing import Dict

# Ejercicio 6

import random

def juego_de_adivinanzas():
    diccionario = {"Frutilla": ["Es roja","Siempre pequeña","Tiene muchas semillas"],"Arandanos":["Son de color azul","Muy diminutos","Tienen formas de pequeñas bolitas"],"Palta":["Es de color verde","Tiene un relleno suave por dentro","Cae del árbol","Tambien van en las tostadas"]}
    respuesta = random.choice(list(diccionario.keys()))
    print("\nJuego de adivinanzas: Adivina la fruta")
    print("Recuerda, si te rindes ingresa: Salir")
    intento = None
    while respuesta != intento:
        intento = input("\n¿Qué fruta es...?: ")
        if intento == "Salir":
            print(f"La respuesta era: {respuesta}")
            break
        elif respuesta == intento:
            print(f"Felicidad, si era {respuesta}")
            break
        else:
            print("Respuesta incorrecta, sigue intentando.")
            if len(diccionario[respuesta]) != 0:
                print("Aquí una pista :)\n")
                print(diccionario[respuesta].pop())
