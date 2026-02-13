#2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
def A2():
    try:
        x = int(input("Ingrese la base del rectangulo: "))
        y = int(input("Ingrese la altura del rectangulo: "))

        area = x * y

        print("La area del rectangulo es:", area)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A2()