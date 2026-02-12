# Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.

edad = int(input("Ingrese su edad: "))

if edad >= 60:
    print("Usted es un adulto mayor")
elif edad >= 18:
    print("Usted es mayor de edad")
elif edad < 18:
    print("Usted es menor de edad")