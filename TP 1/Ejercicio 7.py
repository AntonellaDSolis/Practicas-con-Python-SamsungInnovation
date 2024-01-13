# Ejercicio 7

max = None
min = None
for i in range(10):
    numero = float(input("Ingrese un número: "))
    if max is None and min is None :
        max = min = numero 
    if numero > max:
        max = numero
    if numero < min:
        min = numero

print(f"El número más grande ingresado es {max}")
print(f"El número más pequeño ingresado es {min}")