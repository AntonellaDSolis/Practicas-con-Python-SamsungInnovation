from typing import List
from typing import Dict

# Ejercicio 7

## Ejemplo de testeo:
# calculadoraDePrecios({"Auto": 100,"Computadora":50,"Viaje":200},["Computadora","Auto"])

def calculadoraDePrecios (productos: dict, listaDeCompra: list) -> float:
    total :  float = 0
    for comprar in listaDeCompra:
        for item,price in productos.items():
            if comprar == item:
                total += price
    print(f"Su total a pagar es de: {total}")