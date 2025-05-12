from collections import deque
from datetime import datetime

class Paciente:
    def __init__(self, nombre, edad, motivo):
        self.nombre = nombre
        self.edad = edad
        self.motivo = motivo
        self.hora_llegada = datetime.now()

    def __str__(self):
        return (f"  Nombre: {self.nombre} | Edad: {self.edad} | Motivo: {self.motivo} | "
                f"Hora: {self.hora_llegada.strftime('%H:%M:%S')}")

class CentroSalud:
    def __init__(self):
        self.cola_pacientes = deque()

    def registrar_paciente(self):
        nombre = input("  Ingrese nombre del paciente: ")
        edad = input("  Ingrese edad del paciente: ")
        motivo = input("  Motivo de consulta: ")
        paciente = Paciente(nombre, edad, motivo)
        self.cola_pacientes.append(paciente)
        print(f"\n  REGISTRO EXITOSO:\n{paciente}\n")

    def atender_paciente(self):
        if not self.cola_pacientes:
            print("\n  No hay pacientes para atender.\n")
            return
        paciente = self.cola_pacientes.popleft()
        print(f"\n  PACIENTE ATENDIDO:\n{paciente}\n")

    def ver_siguiente_paciente(self):
        if not self.cola_pacientes:
            print("\n  No hay pacientes en espera.\n")
            return
        print(f"\n  SIGUIENTE EN ESPERA:\n{self.cola_pacientes[0]}\n")

    def mostrar_cola(self):
        if not self.cola_pacientes:
            print("\n  La cola está vacía.\n")
        else:
            print("\n  COLA DE PACIENTES:\n")
            for i, paciente in enumerate(self.cola_pacientes, start=1):
                print(f"{i}. {paciente}")
            print()

def menu():
    centro = CentroSalud()
    while True:
        print("===   CENTRO DE SALUD - LEÓN ===")
        print("1. Registrar nuevo paciente")
        print("2. Atender siguiente paciente")
        print("3. Ver siguiente paciente sin atender")
        print("4. Ver cola de pacientes")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            centro.registrar_paciente()
        elif opcion == "2":
            centro.atender_paciente()
        elif opcion == "3":
            centro.ver_siguiente_paciente()
        elif opcion == "4":
            centro.mostrar_cola()
        elif opcion == "5":
            print("\n Gracias. ¡Hasta luego!\n")
            break
        else:
            print("\n  Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
