registro_repuestos.py
def agregar_repuesto():
    print("Agregar repuesto (en construcción)")

def buscar_repuesto():
    print("Buscar repuesto (en construcción)")

def actualizar_cantidad():
    print("Actualizar cantidad (en construcción)")

def consultar_lista():
    print("Consultar lista (en construcción)")

def menu():
    while True:
        print("\n--- Registro de repuestos del taller ---")
        print("1. Agregar repuesto")
        print("2. Buscar repuesto")
        print("3. Actualizar cantidad")
        print("4. Consultar lista")
        print("5. Salir")
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            agregar_repuesto()
        elif opcion == "2":
            buscar_repuesto()
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
            consultar_lista()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, probá de nuevo.")

menu()
