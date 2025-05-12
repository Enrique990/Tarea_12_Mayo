# Pila de tareas
pila_tareas = []

# Función para agregar una nueva tarea (push)
def agregar_tarea():
    estudiante = input("Nombre del estudiante: ").strip()
    asignatura = input("Asignatura o tema: ").strip()
    
    if not estudiante or not asignatura:
        print("Todos los campos son obligatorios.")
        return

    tarea = {
        "estudiante": estudiante,
        "asignatura": asignatura
    }

    pila_tareas.append(tarea)
    print(f"Tarea de {estudiante} agregada a la pila.")

# Función para revisar la última tarea (pop)
def revisar_tarea():
    if pila_tareas:
        tarea = pila_tareas.pop()
        print(f"Revisando tarea de {tarea['estudiante']} sobre {tarea['asignatura']}.")
    else:
        print("No hay tareas por revisar.")

# Función para ver la siguiente tarea a revisar (peek)
def ver_siguiente_tarea():
    if pila_tareas:
        tarea = pila_tareas[-1]
        print("Siguiente tarea a revisar:")
        print(f"  Estudiante: {tarea['estudiante']}")
        print(f"  Asignatura: {tarea['asignatura']}")
    else:
        print("No hay tareas pendientes.")

# Menú principal
def menu():
    while True:
        print("\n--- Revisión de Tareas – Docente de Informática ---")
        print("1. Agregar tarea al escritorio")
        print("2. Revisar tarea (sacar la última)")
        print("3. Ver siguiente tarea por revisar")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            revisar_tarea()
        elif opcion == "3":
            ver_siguiente_tarea()
        elif opcion == "4":
            print("Fin de la jornada de revisión. ¡Buen trabajo!")
            break
        else:
            print("Opción inválida. Intente con un número del 1 al 4.")

# Ejecutar el sistema
menu()