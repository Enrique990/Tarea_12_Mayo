from collections import deque
from datetime import datetime

class Camion:
    def __init__(self, placa, conductor, empresa, hora_llegada):
        self.placa = placa
        self.conductor = conductor
        self.empresa = empresa
        self.hora_llegada = hora_llegada

    def __str__(self):
        return (f"  Placa: {self.placa} | Conductor: {self.conductor} | "
                f"Empresa: {self.empresa} | Hora: {self.hora_llegada.strftime('%H:%M:%S')}")

class CentroDistribucion:
    def __init__(self):
        self.cola_camiones = deque()

    def registrar_camion(self, placa, conductor, empresa):
        hora_actual = datetime.now()
        camion = Camion(placa, conductor, empresa, hora_actual)
        self.cola_camiones.append(camion)
        print(f"  REGISTRADO: {camion}\n")

    def mostrar_orden_camiones(self):
        print("  ORDEN ACTUAL DE CAMIONES EN ESPERA:")
        if not self.cola_camiones:
            print("  No hay camiones en la cola.\n")
        else:
            for i, camion in enumerate(self.cola_camiones, start=1):
                print(f"  {i}. {camion}")
            print()

    def salir_camion(self):
        if not self.cola_camiones:
            print(" SALIDA FALLIDA: No hay camiones para descargar.\n")
            return None
        camion = self.cola_camiones.popleft()
        print(f"  SALIDA: Camión atendido y descargado -> {camion}\n")
        return camion

# --- Demostración de uso ---
if __name__ == "__main__":
    print("===   CENTRO DE DISTRIBUCIÓN - MERCADO ORIENTAL ===\n")

    centro = CentroDistribucion()

    # Registrar camiones
    centro.registrar_camion("CH1234", "Carlos López", "Distribuidora San Jorge")
    centro.registrar_camion("MN5678", "Ana Torres", "Alimentos del Norte")
    centro.registrar_camion("LE9012", "Luis Pérez", "La Colonia S.A.")

    # Mostrar orden
    centro.mostrar_orden_camiones()

    # Salida del primer camión
    centro.salir_camion()

    # Mostrar orden actualizado
    centro.mostrar_orden_camiones()
