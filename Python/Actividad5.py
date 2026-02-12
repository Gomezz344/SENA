# 6. Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.

prod = input("Digite el nombre de su producto: ")
valor = int(input("Digite el valor de su producto: "))
cant = int(input("Digite la cantidad comprada: "))

total = valor * cant

print("Su monto a pagar es:", total)