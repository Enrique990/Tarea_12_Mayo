class PilaSacos:
    def __init__(self):
        self.sacos = []

    def apilar_saco(self, saco):
        """Carga un saco encima del camión (push)"""
        self.sacos.append(saco)
        print(f"✅ CARGADO: Saco '{saco}' colocado en la parte superior.\n")

    def descargar_saco(self):
        """Descarga el saco superior (pop)"""
        if self.esta_vacia():
            print("❌ DESCARGA FALLIDA: No hay sacos para descargar.\n")
            return None
        saco = self.sacos.pop()
        print(f"⬇️ DESCARGADO: Saco '{saco}' retirado del camión.\n")
        return saco

    def ver_saco_superior(self):
        """Muestra el saco que está encima (peek)"""
        if self.esta_vacia():
            print(" CAMIÓN VACÍO: No hay sacos en el camión.\n")
            return None
        print(f"  SACO SUPERIOR: '{self.sacos[-1]}' está en la cima.\n")
        return self.sacos[-1]

    def esta_vacia(self):
        return len(self.sacos) == 0

    def mostrar_sacos(self):
        print("  CONTENIDO ACTUAL DEL CAMIÓN:")
        if self.esta_vacia():
            print("  El camión está vacío.\n")
        else:
            for i in range(len(self.sacos)-1, -1, -1):
                print(f"  ▪ Nivel {len(self.sacos)-i}: {self.sacos[i]}")
            print()  # Salto de línea

# --- Demostración de uso ---
if __name__ == "__main__":
    print("===  SIMULACIÓN DE PILA DE SACOS EN UN CAMIÓN ===\n")

    camion = PilaSacos()

    # Cargando sacos
    camion.apilar_saco("Arroz")
    camion.apilar_saco("Frijoles")
    camion.apilar_saco("Maíz")

    # Mostrar el contenido actual
    camion.mostrar_sacos()

    # Ver el saco encima
    camion.ver_saco_superior()

    # Descargar el último cargado
    camion.descargar_saco()

    # Mostrar nuevamente
    camion.ver_saco_superior()
    camion.mostrar_sacos()
