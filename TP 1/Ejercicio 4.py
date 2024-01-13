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