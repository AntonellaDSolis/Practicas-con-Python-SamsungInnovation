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
