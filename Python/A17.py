# Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.
def A17():
    try:
        año_nac = int(input("Ingrese el año de nacimiento: "))
        año_act = int(input("Ingrese el año actual: "))

        edad = año_act - año_nac

        print("Su edad es:", edad)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A17()