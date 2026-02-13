# Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.
def A18():
    try:
        edad = int(input("Ingrese su edad: "))

        if edad >= 60:
            print("Usted es un adulto mayor")
        elif edad >= 18:
            print("Usted es mayor de edad")
        elif edad < 18:
            print("Usted es menor de edad")
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A18()