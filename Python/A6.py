# 6. Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.
def A6():
    try:
        prod = input("Digite el nombre de su producto: ")
        valor = int(input("Digite el valor de su producto: "))
        cant = int(input("Digite la cantidad comprada: "))

        total = valor * cant

        print("Su monto a pagar es:", total)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A6()