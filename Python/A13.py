# Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).
def A13():
    try:
        nota1 = float(input("Ingrese su nota 1: "))
        nota2 = float(input("Ingrese su nota 2: "))
        nota3 = float(input("Ingrese su nota 3: "))

        promedio = (nota1 + nota2 + nota3) / 3

        print("Su promedio es: ", round(promedio, 2))
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A13()