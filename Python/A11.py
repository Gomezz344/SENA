# 11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.
def A11():
    try:
        ventas = float(input("Ingrese el valor de las ventas realizadas: "))
        comision = 0.05

        total = ventas * comision

        print("El valor de la comision es de:", round(total, 2))
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A11()
