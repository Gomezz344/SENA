# Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.

año_nac = int(input("Ingrese el año de nacimiento: "))
año_act = int(input("Ingrese el año actual: "))

edad = año_act - año_nac

print("Su edad es:", edad)