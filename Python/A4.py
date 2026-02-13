# 4. Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.
def A4():
    try:
        horas = int(input("Ingrese las horas trabajadas esta semana: "))

        vhora = 60000

        salariosem = horas * vhora

        print("Su salario semanal es:", salariosem)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A4()
