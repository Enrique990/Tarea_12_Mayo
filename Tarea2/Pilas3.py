# Lista para simular la pila de donantes
pila_donantes = []

# Función para registrar un nuevo donante (push)
def registrar_donante():
    nombre = input("Ingrese el nombre del donante: ").strip()
    edad = input("Ingrese la edad del donante: ").strip()
    tipo_sangre = input("Ingrese el tipo de sangre del donante: ").strip().upper()

    if not nombre or not edad or not tipo_sangre:
        print("Todos los campos son obligatorios.")
        return

    if not edad.isdigit() or int(edad) < 18:
        print("El donante debe tener al menos 18 años y edad válida.")
        return

    donante = {
        "nombre": nombre,
        "edad": int(edad),
        "tipo_sangre": tipo_sangre
    }
    pila_donantes.append(donante)
    print(f"Donante {nombre} registrado correctamente.")

# Función para eliminar el último donante registrado (pop)
def eliminar_ultimo_donante():
    if pila_donantes:
        eliminado = pila_donantes.pop()
        print(f"Registro de {eliminado['nombre']} eliminado (reversión técnica).")
    else:
        print("No hay registros para eliminar.")

# Función para mostrar el donante actual en proceso (peek)
def mostrar_donante_actual():
    if pila_donantes:
        actual = pila_donantes[-1]
        print("Donante actual en proceso:")
        print(f"  Nombre: {actual['nombre']}")
        print(f"  Edad: {actual['edad']}")
        print(f"  Tipo de sangre: {actual['tipo_sangre']}")
    else:
        print("No hay donantes registrados en este momento.")

# Menú principal
def menu():
    while True:
        print("\n--- Campaña de Donación de Sangre – Hospital de Estelí ---")
        print("1. Registrar nuevo donante")
        print("2. Eliminar último registro (reversión técnica)")
        print("3. Mostrar donante actual en proceso")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            registrar_donante()
        elif opcion == "2":
            eliminar_ultimo_donante()
        elif opcion == "3":
            mostrar_donante_actual()
        elif opcion == "4":
            print("Gracias por apoyar la campaña de donación.")
            break
        else:
            print("Opción inválida. Intente con 1, 2, 3 o 4.")

# Ejecutar el sistema
menu()
