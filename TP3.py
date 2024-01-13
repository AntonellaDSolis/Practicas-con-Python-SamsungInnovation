from typing import List
from typing import Dict

# Ejercicio 1

def contador_de_palabras(texto: str) -> str:
    palabra : str = ""
    dic : dict = {}
    ultima_letra = 1
    for letra in texto:
        if letra != " ":
            palabra = palabra + letra
        if letra == " " or ultima_letra == len(texto):
            if palabra in dic.keys():
                dic[palabra] = dic[palabra]+1
            else:
                dic[palabra] = 1
            palabra = ""
        ultima_letra += 1

# Ejercicio 2

def calculadoraDeEstadistica (lista : list) -> dict:
    diccionario = {}
    diccionario ["suma"] = sum(lista)
    diccionario["promedio"] = (sum(lista)/len(lista))
    diccionario["minimo"] = min(lista)
    diccionario["maximo"] = max(lista)
    return diccionario 

# Ejercicio 3

def agregarContacto():
    agenda = {}
    print("Agenda interactiva: ")
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("\nElige una opción: ")
        if opcion == "1":
            nombre = input("\nIngresa el nombre del contacto: ")
            telefono = input("Ingresa el número de teléfono: ")
            agenda[nombre] = telefono
            print("Contacto agregado con éxito.")
        elif opcion == "2":
            nombre = input("\nIngresa el nombre del contacto: ")
            if nombre in agenda:
                print(nombre + ": " + agenda[nombre])
            else:
                print("Contacto no encontrado.")
        elif opcion == "3":
            if agenda == {}:
                print("No tiene ningún contacto guardado.")
            else:
                print("\nLista de contactos:")
                for nombre, telefono in agenda.items():
                    print(nombre + ": " + telefono)
        elif opcion == '4':
            nombre = input("\nIngresa el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        elif opcion == '5':
            print("¡Hasta luego!")
            break 
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

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

# Ejercicio 5

def registroDeEstudiantes():
    registroDeAlumnos = []
    alumno = {}
    print("Registro de estudiantes: ")
    while True:
        print("\n1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Registro")
        print("4. Salir\n")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            alumno["Nombre"] = nombre
            edad = input("Ingrese la edad: ")
            alumno["Edad"] = edad
            num : int = input("¿Cuántas materias desea ingresar?: ")
            registroDeMaterias = {}
            for i in range(int(num)):
                materia = input("Ingrese la materia: ")
                calificacion = input("Ingrese la calificacion: ")
                registroDeMaterias[materia] = calificacion
            alumno["Materias"] = registroDeMaterias
            registroDeAlumnos.append(alumno)
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            valor = False
            for alumno in registroDeAlumnos:
                if alumno["Nombre"] == nombre:
                    print(alumno)
                    valor = True
                    break
            if valor == False:
                print("El alumno no ha sido ingresado al registro.")
        elif opcion == "3":
            print("\nRegistro actual: ")
            for alumno in registroDeAlumnos:
                print(alumno)
        elif opcion == '4':
            print("Registro cerrado.")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

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

# Ejercicio 8

def registroDeEmpleados():
    registro = []
    print("Registro de empleados: ")
    while True:
        print("\n1. Agregar nuevo empleado")
        print("2. Lista de empleados según departamento")
        print("3. Total de salarios según departamento")
        print("4. Salir\n")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            empleado = {}
            nombre = input("Ingrese el nombre: ")
            empleado["Nombre"] = nombre
            salario = input("Ingrese el salario: ")
            empleado["Salario"] = salario
            departamento = input("Ingrese el departamento donde trabaja: ")
            empleado["Departamento de trabajo"] = departamento
            registro.append(empleado)
        elif opcion == "2":
            buscar_depto = input("Ingrese el departamento: ")
            valor = False
            print(f"\nLista de empleados del departamento de {buscar_depto}")
            for datos in registro:
                if datos["Departamento de trabajo"] == buscar_depto:
                    print(datos)
                    valor = True
            if valor == False:
                print("\n...")
                print("\nNo existe empleado que pertenezca a ese departamento en el registro.")
        elif opcion == "3":
            buscar_depto = input("Ingrese el departamento: ")
            total = 0
            valor = False
            for datos in registro:
                if datos["Departamento de trabajo"] == buscar_depto:
                    total += float(datos["Salario"])
                    valor = True
            if valor == False:
                print("\nNo existe empleado que pertenezca a ese departamento en el registro.")
            else:
                print(f"\nTotal de salarios: {total}.")
        elif opcion == '4':
            print("Registro cerrado.")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")