# Ejercicio 1
numero = int(input("Ingrese un número: "))

if numero > 0 :
    print ("El número es positivo")
elif numero == 0:
    print("El númrto es cero")
else:
    print("El número es negativo")

# Ejercicio 2
import math

radio = float(input("Ingrese el valor del radio del círculo:"))

perimetro = 2 * math.pi * radio
superficie = math.pi * radio * radio

print(f"El perímetro del círculo es {perimetro} y la superficie es de {superficie}")

# Ejercicio 3
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")

# Ejercicio 4
capitalTotal = 0
dic = {}

print( "Por favor ingrese los datos conrrespondientes. Para terminar ingrese en nombre: Salir")

while nombre != "Salir":
    nombre = str(input("Ingrese el nombre del inversor: "))
    aporte = float(input("Ingrese la cantidad a aportar: "))
    capitalTotal += aporte
    dic[nombre] = aporte

print(f"El total del capital es de {capitalTotal}")
print("La siguiente lista muestra el porcentaje aportado por cada inversor: ")

for nombre,aporte in dic.items():
    porcentaje : float = ((aporte) * 100) / capitalTotal
    print(f"{nombre} aporto el {porcentaje}%")

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

#Ejercicio 6
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

# Ejercicio 8
numeros = int(input("¿Cuantós números desea ingresar? "))
suma : int = 0
multiplicacion : int = 1

for i in range(numeros):
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    multiplicacion = multiplicacion * numero

print (suma)
print (multiplicacion)

# Ejercicio 9
usuario = "antonella.solis"
contraseña = 12345

while True:
    nombre = str(input("Ingrese su usuario: "))
    intento = str(input("Ingrese su contraseña: "))
    if nombre == usuario and intento == contraseña:
        print(f"El usuario ingresado es correcto, bienvenido {usuario} :)")
        break
    else:
        print("Error, intente de nuevo")

# Ejercicio 10
sumatoria : int = 0
numero : int = 1

while numero != 0:
    numero = int(input("Ingrese un número: "))
    sumatoria = sumatoria + numero
print(sumatoria)

#Ejercicio 11
facturacion : float = 0
gananciaTotal : float = 0
año = ["enero", "febrero" ,"marzo" ,"abril" ,"mayo" ,"junio" ,"julio" ,"agosto" ,"septiembre" ,"octubre" ,"noviembre" ,"diciembre"]

for mes in año:
    ingreso = float(input(f"Ingrese el monto de ventas realizadas en {mes}: "))
    gasto = float(input("Ingrese el gasto del mes: "))
    #Saco la ganancia mensual
    gananciaNeta = ingreso - gasto
    print (f"Ganancia de {mes}: {gananciaNeta}")
    #Auxiliar
    facturacion = facturacion + ingreso
    gananciaTotal = gananciaTotal + gananciaNeta

#Saco la Facturación anual
print(f"La Facturación anual es de: {facturacion}")

#Saco la ganancia promedio
gananciaPromedio = gananciaTotal/12
print (f"La ganancia promedio es de: {gananciaPromedio}")

#Ejercicio 12
while True:
    numero1 = float(input("Ingrese un número: "))
    numero2 = float(input("Ingrese un número: "))
    operacion = str(input("Ingrese la opeación a realizar: "))
    if operacion == "sumar":
        print(numero1 + numero2)
    elif operacion == "restar":
        print(numero1 - numero2)
    elif operacion == "multiplicar":
        print(numero1 * numero2)
    elif operacion == "dividir" :
        if numero2 == 0:
            print("Operación imposible")
        else:
            print(numero1 / numero2)
    else:
        print("Operación no disponible")