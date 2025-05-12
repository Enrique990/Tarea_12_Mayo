#En la ventanilla única de la Alcaldía de Managua, los ciudadanos hacen fila para trámites como solicitudes de permisos de construcción, pagos de impuestos o certificaciones. Cada ciudadano se registra con su cédula, nombre completo, tipo de trámite y hora de llegada. Se requiere simular:
#✔	El ingreso de ciudadanos a la fila,
#✔	La visualización del orden de atención,
#✔	El retiro del ciudadano atendido.

from collections import deque  # Importamos deque para manejar la cola de ciudadanos

class VentanillaUnica:
    def __init__(self):
        self.fila = deque()  # Inicializamos una cola vacía
        self.tramites_disponibles = ["Solicitudes de permiso de construcción", "Pago de impuestos", "Certificaciones"]  # Lista de trámites disponibles

    def ingresar_ciudadano(self):
        cedula = input("Ingrese la cédula: ")
        nombre = input("Ingrese el nombre completo: ")

        # Mostrar los trámites disponibles con opción seleccionable
        print("\nSeleccione el tipo de trámite:")
        for idx, tramite in enumerate(self.tramites_disponibles, start=1):
            print(f"{idx}. {tramite}")

        while True:
            try:
                opcion = int(input("\nIngrese el número de su trámite: "))
                if 1 <= opcion <= len(self.tramites_disponibles):
                    tramite = self.tramites_disponibles[opcion - 1]
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        hora_llegada = input("Ingrese la hora de llegada (HH:MM AM/PM): ")
        ciudadano = {"cedula": cedula, "nombre": nombre, "tramite": tramite, "hora_llegada": hora_llegada}
        self.fila.append(ciudadano)  # Agregar el ciudadano a la cola
        print(f"\n{nombre} ha sido agregado a la fila con el trámite: {tramite}.\n")

    def visualizar_fila(self):
        if not self.fila:
            print("\nLa fila está vacía.\n")
        else:
            # Ordenar la lista de ciudadanos por la hora de llegada antes de mostrarla
            lista_ordenada = sorted(self.fila, key=lambda x: x["hora_llegada"])  
            print("\nOrden de atención (por hora de llegada):")
            for idx, ciudadano in enumerate(lista_ordenada, start=1):
                print(f"{idx}. {ciudadano['nombre']} - {ciudadano['tramite']} - Llegó a las {ciudadano['hora_llegada']}")
            print()

    def retirar_ciudadano(self):
        if not self.fila:
            print("\nNo hay ciudadanos en espera.\n")
        else:
            ciudadano_atendido = self.fila.popleft()  # Retirar al primer ciudadano de la cola
            print(f"\n{ciudadano_atendido['nombre']} ha sido atendido y retirado de la fila.\n")

# Menú interactivo para administrar la fila
def menu():
    ventanilla = VentanillaUnica()
    
    while True:
        print("\n--- Ventanilla Única - Alcaldía de Managua ---")
        print("1. Ingresar ciudadano a la fila")
        print("2. Visualizar orden de atención por hora de llegada")
        print("3. Retirar ciudadano atendido")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ventanilla.ingresar_ciudadano()
        elif opcion == "2":
            ventanilla.visualizar_fila()
        elif opcion == "3":
            ventanilla.retirar_ciudadano()
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, intente nuevamente.\n")

# Ejecutar el menú
menu()