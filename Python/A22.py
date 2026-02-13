# Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.
def A22():
    try:
        cant_ini_prod = float(input("Ingrese la cantidad inicial de un producto en inventario: "))
        cantv = float(input("Ingrese la cantidad vendida: "))
        cantr = float(input("Ingrese la canatidad recibida: "))

        inv_final = cant_ini_prod - cantv + cantr

        print("El inventario final es: ", inv_final)
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A22()
