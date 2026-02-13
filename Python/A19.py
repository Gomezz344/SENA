# Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.
def A19():
    try:
        cop = float(input("Ingrese su cantidad en pesos colombianos: "))
        tasa = float(input("Ingrese la tasa de cambio: "))

        usd = cop / tasa

        print("La conversion es:", round(usd, 2))
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A19()