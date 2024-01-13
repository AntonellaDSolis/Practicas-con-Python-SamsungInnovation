# Ejercicio 12

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