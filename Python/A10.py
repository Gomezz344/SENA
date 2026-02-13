# 10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.
def A10():
    try:
        productos = int(input("Digite la cantidad de productos que compro: "))
        valor = int(input("Digite el precio del producto: "))

        total = productos * valor

        print("El valor a pagar es:", total)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A10()