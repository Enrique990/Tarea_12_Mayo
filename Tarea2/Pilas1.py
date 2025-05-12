'''
Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua recibe documentos para revisión. 
Por cada solicitud, se apilan los documentos entregados en el orden en que llegan. 
El personal debe revisar el último documento entregado primero. Se debe simular el proceso de revisión, 
utilizando una pila, y permitir agregar nuevos documentos, eliminar el último revisado y mostrar los pendientes.
'''

def oficina():
    
    pila_documentos = []

    while True:
        print("\n--- Oficina de Atención Ciudadana ---")
        print("\nOpciones:")
        print("1. Agregar nuevo documento")
        print("2. Revisar último documento entregado")
        print("3. Mostrar documentos pendientes")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            nombre_documento = input("Ingrese el nombre o descripci0n del documento a agregar: ")
            pila_documentos.append(nombre_documento)
            print(f"'{nombre_documento}' ha sido agregado a la pila.")
        elif opcion == '2':
            if not pila_documentos:
                print("No hay documentos para revisar.")
            else:
                documento_revisado = pila_documentos.pop()
                print(f"Se ha revisado y eliminado el documento: '{documento_revisado}'")
        elif opcion == '3':
            if not pila_documentos:
                print("No hay documentos pendientes.")
            else:
                print("\n--- Documentos Pendientes (del mas reciente al mas antiguo) ---")
                for i in range(len(pila_documentos) - 1, -1, -1):
                    print(f"- {pila_documentos[i]}")
        elif opcion == '4':
            print("Saliendo del sistema de atencion ciudadana.")
            break
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    oficina()