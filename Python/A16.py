# Número par o impar: Solicitar un número entero e indicar si es par o impar.
def A16():
    try:
        num = int(input("Ingrese su número: "))

        if num %2 == 0:
            print("Su número es par")
        else:
            print("Su número es impar")
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A16()