# Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.
def A20():
    try:
        capital = float(input("Ingrese su capital: "))
        meses = int(input("Ingrese los meses: "))
        tasa_intereses = float(input("Ingrese la tasa de intereses: "))

        interes_simple = capital * meses * tasa_intereses
        total = capital + interes_simple

        print("El interes simple es:", interes_simple)
        print("El total es :", total)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A20()