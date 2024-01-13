# Ejercicio 5

pares = 0
impares = 0

print( "Por favor ingrese los datos conrrespondientes. Para terminar ingrese en nombre: Salir")

while numero != "Salir":
    numero = input("Ingrese un número: ")
    if numero % 2 == 0:
        print (f"El número {numero} es par")
        pares += 1
    else:
        print(f"El número {numero} es impar")
        impares += 1

print (f"Hay {pares} números pares ingresados")
print(f"Hay {impares} números impares ingresados")