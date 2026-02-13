# Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.
def A23():
    try:
        peso = float(input("Ingrese el peso del paquete (kg): "))

        if peso >= 5:
            print("Su envio cuesta 10.000")
        else:
            print("Su envío cuesta 20.000")
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A23()
