# Bandeja como una pila vacía
bandeja = []

# Función para agregar pan (push)
def agregar_pan():
    tipo = input("Ingrese el tipo de pan que desea agregar: ").strip()
    if tipo == "":
        print("No se puede agregar un pan sin nombre.")
    else:
        bandeja.append(tipo)
        print(f"Se agregó un pan de {tipo} a la bandeja.")

# Función para vender pan (pop)
def vender_pan():
    if bandeja:
        vendido = bandeja.pop()
        print(f"Se vendió un pan de {vendido}.")
    else:
        print("La bandeja está vacía. No hay panes para vender.")

# Función para ver el pan listo para vender (peek)
def ver_ultimo_pan():
    if bandeja:
        print(f"El pan listo para vender es de {bandeja[-1]}.")
    else:
        print("La bandeja está vacía.")

# Menú principal
def menu():
    while True:
        print("\n--- Panadería el pancito ---")
        print("1. Agregar pan a la bandeja")
        print("2. Vender pan")
        print("3. Ver pan listo para vender")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            agregar_pan()
        elif opcion == "2":
            vender_pan()
        elif opcion == "3":
            ver_ultimo_pan()
        elif opcion == "4":
            print("Gracias por usar el sistema de la panadería.")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 4.")

# Ejecutar el menú
menu()
