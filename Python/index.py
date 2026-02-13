import os
import sys
import subprocess

while True:
    print("=============================================")
    print("Taller 1 - Algoritmos Basicos en Python")
    print("By Emmanuel Gómez Velez")
    print("Menú Pruncipal")
    print("==============================================")
    
    for i in range(1, 26):
        print(f"{i}. Ejercicio {i}")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "0":
        print("Saliendo del programa...")
        break
    
    if opcion.isdigit() and 1<= int(opcion) <= 25:
        archivo = f"A{opcion}.py"
        
        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"No existe {archivo}")
    else:
        print("Opción no válida")
    
    input("\n Presiona ENTER para continuar...")
    