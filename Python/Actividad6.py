# 7. Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.

valort = int(input("Digite el valor total de su compra: "))

if valort > 200000 :
    descuento = valort * 0.10
    totalp = valort - descuento
    print("Su valor con descuento es:", totalp)
else: 
    print("Su valor de la compra es:", valort)