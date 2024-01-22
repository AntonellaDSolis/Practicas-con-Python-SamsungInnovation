from typing import List
from typing import Dict

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