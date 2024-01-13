pares = 0
impares = 0
cant = int(input("Cantidad de números para ingresar: "))

for i in range(cant):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print (f"El número {numero} es par")
        pares = pares + 1
    else:
        print(f"El número {numero} es impar")
        impares = impares + 1

print (f"Hay {pares} números pares ingresados")
print(f"Hay {impares} números impares ingresados")