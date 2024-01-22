from typing import List
from typing import Dict

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