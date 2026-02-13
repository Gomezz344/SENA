# Comisión escalonada: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.
def A12():
    try:
        ventas = float(input("Ingrese el valor de las ventas mensuales: "))


        if ventas > 1000000 :
            comision = 0.10
            total = ventas * comision
            print("La comision es de:", round(total, 2))
        else:
            comision = 0.05
            total = ventas * comision
            print("Su comision es de: ", round(total, 2))
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A12()
