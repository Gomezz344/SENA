def A24():
    try:
        consumo = float(input("Ingrese el consumo de agua en metros cúbicos: "))
        valor_metro_cubico = float(input("Ingrese el valor por metro cúbico: "))

        total = consumo * valor_metro_cubico


        print("\n--- Factura de Agua ---")
        print(f"Consumo: {consumo} m³")
        print(f"Valor por m³: ${valor_metro_cubico}")
        print(f"Total a pagar: ${total}")
    except ValueError:
        print("Debes ingresar un número válido")
if __name__ == "__main__":
        A24()
