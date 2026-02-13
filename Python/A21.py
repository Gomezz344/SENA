#  Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.
def A21():
    try:
        capitali = float(input("Ingrese su capital inicial: "))
        tasai = float(input("Ingrese la tasa de interés: "))
        periodos = float(input("Ingrese el número de períodos: "))

        tasa_decimal = tasai / 100

        monto_final = capitali * (1 + tasa_decimal) ** periodos

        print("El monto final es: ", monto_final)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A21()
