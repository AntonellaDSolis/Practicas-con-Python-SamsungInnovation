# Ejercicios 8

numeros = int(input("¿Cuantós números desea ingresar? "))
suma : int = 0
multiplicacion : int = 1

for i in range(numeros):
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    multiplicacion = multiplicacion * numero

print (suma)
print (multiplicacion)