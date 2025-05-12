from collections import deque  # Importamos deque para manejar la cola de pedidos

class Restaurante:
    def __init__(self):
        self.cola_pedidos = deque()  # Usamos deque para gestionar la cola de pedidos
        self.tipos_combos = ["Clásico", "Familiar", "Sándwich"]  # Opciones de combo disponibles

    def agregar_pedido(self):
        numero_orden = input("Ingrese el número de orden: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        # Menú para seleccionar el tipo de combo
        print("\nSeleccione el tipo de combo:")
        for idx, combo in enumerate(self.tipos_combos, start=1):
            print(f"{idx}. {combo}")

        while True:
            try:
                opcion_combo = int(input("\nIngrese el número del combo: "))
                if 1 <= opcion_combo <= len(self.tipos_combos):
                    tipo_combo = self.tipos_combos[opcion_combo - 1]
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        hora_pedido = input("Ingrese la hora del pedido (HH:MM AM/PM): ")
        pedido = {"numero_orden": numero_orden, "nombre_cliente": nombre_cliente, "tipo_combo": tipo_combo, "hora_pedido": hora_pedido}
        
        self.cola_pedidos.append(pedido)  # Agregamos el pedido al final de la cola
        print(f"\nEl pedido {numero_orden} de {nombre_cliente} ha sido registrado con el combo {tipo_combo}.\n")

    def visualizar_pedidos(self):
        if not self.cola_pedidos:
            print("\nNo hay pedidos en espera.\n")
        else:
            print("\nLista de pedidos en espera:")
            for idx, pedido in enumerate(self.cola_pedidos, start=1):
                print(f"{idx}. Orden {pedido['numero_orden']} - {pedido['nombre_cliente']} - {pedido['tipo_combo']} - Pedido a las {pedido['hora_pedido']}")
            print()

    def atender_pedido(self):
        if not self.cola_pedidos:
            print("\nNo hay pedidos en espera para atender.\n")
        else:
            pedido_atendido = self.cola_pedidos.popleft()  # Retiramos el primer pedido de la cola
            print(f"\nEl pedido {pedido_atendido['numero_orden']} de {pedido_atendido['nombre_cliente']} ha sido atendido.\n")

# Menú interactivo para administrar los pedidos
def menu():
    restaurante = Restaurante()

    while True:
        print("\n--- Tip-Top Metrocentro - Gestión de Pedidos ---")
        print("1. Agregar pedido a la cola")
        print("2. Visualizar lista de pedidos")
        print("3. Atender primer pedido")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            restaurante.agregar_pedido()
        elif opcion == "2":
            restaurante.visualizar_pedidos()
        elif opcion == "3":
            restaurante.atender_pedido()
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, intente nuevamente.\n")

# Ejecutar el menú
menu()