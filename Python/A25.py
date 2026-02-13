def A25():
    try:
        numero_ventas = int(input("Ingrese el número de ventas realizadas en el día: "))

        total_vendido = 0


        for i in range(1, numero_ventas + 1):
            valor_venta = float(input(f"Ingrese el valor de la venta #{i}: "))
            total_vendido += valor_venta


            if numero_ventas > 0:
                promedio = total_vendido / numero_ventas
            else:
                promedio = 0

            print("\n--- Resumen de Ventas ---")
            print(f"Total vendido: ${total_vendido}")
            print(f"Promedio por venta: ${promedio}")
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A25()
