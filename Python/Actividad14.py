# Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El número uno es mayor")
elif num1 < num2:
    print("El número dos es mayor")
elif num1 == num2:
    print("Los números son iguales")

    