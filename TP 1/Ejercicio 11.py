# Ejercicio 11

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