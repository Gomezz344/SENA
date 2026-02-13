# Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.
def A14():
    try:
        taller = float(input("Ingrese la nota de su taller: "))
        parcial = float(input("Ingrese la nota de su parcial: "))
        examenf = float(input("Ingrese la nota de su examen final: "))

        nota_def = (taller * 0.30) + (parcial * 0.30) + (examenf * 0.40)

        print("Su nota definitiva es: ", round(nota_def, 2))
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A14()

