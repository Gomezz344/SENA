# 8.  Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.

vprod = int(input("Digite el precio de su producto: "))
descuento = int(input("Digite el porcentaje del descuento: "))

valor_desc = vprod * (descuento / 100 )

print("Su monto a pagar con descuento es:", valor_desc)
