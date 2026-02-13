# Entradas
def A1():
    try:
        x = int(input("Ingrese el primer número entero: "))
        y = int(input("Ingrese el segundo número entero: "))
        z = int(input("Ingrese el tercer número entero: "))

        # Proceso
        sum = x + y + z
        average = sum / 3

        # Salidas
        print("La suma total es:", sum)
        print("El promedio es:", int(average)) # Se fuerza a que de un promedio en número entero
        
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A1()






