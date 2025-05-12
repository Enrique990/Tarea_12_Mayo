import heapq  # Importamos heapq para manejar la cola de prioridad

class Aeropuerto:
    def __init__(self):
        self.cola_vuelos = []  # Lista que funcionará como cola con prioridad
        self.destinos_disponibles = ["Bluefields", "Corn Island", "Panamá", "Miami"]
        self.tipos_vuelo = ["Comercial", "Carga", "Emergencia"]  # Tipos de vuelo disponibles

    def ingresar_vuelo(self):
        codigo_vuelo = input("Ingrese el código de vuelo: ")
        aerolinea = input("Ingrese la aerolínea: ")

        # Menú para elegir destino
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

        # Menú para elegir tipo de vuelo
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

        # Guardamos el vuelo como una tupla en la cola de prioridad
        heapq.heappush(self.cola_vuelos, (prioridad, codigo_vuelo, aerolinea, destino, tipo_vuelo))
        print(f"\nEl vuelo {codigo_vuelo} de {aerolinea} con destino a {destino} ha sido registrado como {tipo_vuelo}.\n")

    def visualizar_vuelos(self):
        if not self.cola_vuelos:
            print("\nNo hay vuelos registrados.\n")
        else:
            print("\nLista de vuelos en espera (prioridad más alta primero):")
            vuelos_ordenados = sorted(self.cola_vuelos, key=lambda x: x[0])  # Ordenamos por prioridad
            for idx, (_, codigo_vuelo, aerolinea, destino, tipo_vuelo) in enumerate(vuelos_ordenados, start=1):
                print(f"{idx}. {codigo_vuelo} - {aerolinea} - {destino} - {tipo_vuelo}")
            print()

    def autorizar_despegue(self):
        if not self.cola_vuelos:
            print("\nNo hay vuelos en espera para despegar.\n")
        else:
            _, codigo_vuelo, aerolinea, destino, tipo_vuelo = heapq.heappop(self.cola_vuelos)  # Extraemos el vuelo con mayor prioridad
            print(f"\nEl vuelo {codigo_vuelo} de {aerolinea} con destino a {destino} ha sido autorizado para despegar.\n")

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