# 11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.

ventas = float(input("Ingrese el valor de las ventas realizadas: "))
comision = 0.05

total = ventas * comision

print("El valor de la comision es de:", round(total, 2))
