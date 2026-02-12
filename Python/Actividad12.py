# Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).

nota1 = float(input("Ingrese su nota 1: "))
nota2 = float(input("Ingrese su nota 2: "))
nota3 = float(input("Ingrese su nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Su promedio es: ", round(promedio, 2))