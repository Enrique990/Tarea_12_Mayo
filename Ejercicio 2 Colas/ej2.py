from collections import deque  # Importamos deque para manejar la cola de vuelos

class Aeropuerto:
    def __init__(self):
        self.cola_vuelos = deque()  # Usamos deque en lugar de una lista
        self.destinos_disponibles = ["Bluefields", "Corn Island", "Panamá", "Miami"]
        self.tipos_vuelo = ["Comercial", "Carga", "Emergencia"]

    def ingresar_vuelo(self):
        codigo_vuelo = input("Ingrese el código de vuelo: ")
        aerolinea = input("Ingrese la aerolínea: ")

        # Menú para seleccionar destino
        print("\nSeleccione el destino:")
        for idx, destino in enumerate(self.destinos_disponibles, start=1):
            print(f"{idx}. {destino}")

        while True:
            try:
                opcion_destino = int(input("\nIngrese el número de destino: "))
                if 1 <= opcion_destino <= len(self.destinos_disponibles):
                    destino = self.destinos_disponibles[opcion_destino - 1]
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        # Menú para seleccionar tipo de vuelo
        print("\nSeleccione el tipo de vuelo:")
        for idx, tipo in enumerate(self.tipos_vuelo, start=1):
            print(f"{idx}. {tipo}")

        while True:
            try:
                opcion_tipo = int(input("\nIngrese el número del tipo de vuelo: "))
                if 1 <= opcion_tipo <= len(self.tipos_vuelo):
                    tipo_vuelo = self.tipos_vuelo[opcion_tipo - 1]
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        # Asignamos la prioridad (0 = Emergencia, 1 = Carga, 2 = Comercial)
        prioridad = 0 if tipo_vuelo == "Emergencia" else (1 if tipo_vuelo == "Carga" else 2)

        vuelo = {"prioridad": prioridad, "codigo_vuelo": codigo_vuelo, "aerolinea": aerolinea, "destino": destino, "tipo_vuelo": tipo_vuelo}
        
        # Insertamos el vuelo en la posición correcta para mantener la prioridad
        if prioridad == 0:
            self.cola_vuelos.appendleft(vuelo)  # Los vuelos de emergencia se agregan al inicio
        else:
            self.cola_vuelos.append(vuelo)  # Los demás vuelos se agregan al final
        
        print(f"\nEl vuelo {codigo_vuelo} de {aerolinea} con destino a {destino} ha sido registrado como {tipo_vuelo}.\n")

    def visualizar_vuelos(self):
        if not self.cola_vuelos:
            print("\nNo hay vuelos registrados.\n")
        else:
            print("\nLista de vuelos en espera (prioridad más alta primero):")
            for idx, vuelo in enumerate(self.cola_vuelos, start=1):
                print(f"{idx}. {vuelo['codigo_vuelo']} - {vuelo['aerolinea']} - {vuelo['destino']} - {vuelo['tipo_vuelo']}")
            print()

    def autorizar_despegue(self):
        if not self.cola_vuelos:
            print("\nNo hay vuelos en espera para despegar.\n")
        else:
            vuelo_autorizado = self.cola_vuelos.popleft()  # Retiramos el primer vuelo en la cola (mayor prioridad)
            print(f"\nEl vuelo {vuelo_autorizado['codigo_vuelo']} de {vuelo_autorizado['aerolinea']} con destino a {vuelo_autorizado['destino']} ha sido autorizado para despegar.\n")

# Menú interactivo para administrar los vuelos
def menu():
    aeropuerto = Aeropuerto()

    while True:
        print("\n--- Aeropuerto Internacional ---")
        print("1. Ingresar vuelo a la cola")
        print("2. Visualizar lista de vuelos")
        print("3. Autorizar siguiente vuelo para despegar")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            aeropuerto.ingresar_vuelo()
        elif opcion == "2":
            aeropuerto.visualizar_vuelos()
        elif opcion == "3":
            aeropuerto.autorizar_despegue()
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, intente nuevamente.\n")

# Ejecutar el menú
menu()