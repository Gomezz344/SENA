# 9.Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.
def A9():
    try:
        valorx = int(input("Digite el valor de la venta sin impuestos: "))

        IVA = 0.19

        valori = valorx * IVA

        valort = valorx + valori

        print("El valor del IVA es:", valori)

        print("El valor total con impuestos es de:", valort)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A9()
