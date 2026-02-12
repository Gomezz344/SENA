# 10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.

productos = int(input("Digite la cantidad de productos que compro: "))
valor = int(input("Digite el precio del producto: "))

total = productos * valor

print("El valor a pagar es:", total)