from typing import List
from typing import Dict

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
