# 3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
def A3():
    try:
        T1 = int(input("Ingrese el primer número: "))

        conversion = (T1 * 9/5) + 32    

        print("La conversion a farenheit es:", conversion)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A3()
