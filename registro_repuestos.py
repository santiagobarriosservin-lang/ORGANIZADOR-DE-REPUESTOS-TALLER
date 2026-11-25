from datetime import datetime

repuestos = []

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("No puede estar vacío.")

def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Tiene que ser mayor a cero.")
        except ValueError:
            print("Tenés que escribir un número entero.")

def pedir_fecha(mensaje):
    while True:
        texto = input(mensaje)
        try:
            datetime.strptime(texto, "%d/%m/%Y")
            return texto
        except ValueError:
            print("Formato inválido, usá dd/mm/aaaa.")

def agregar_repuesto():
    repuesto = {
        "codigo": pedir_entero("Código: "),
        "nombre": pedir_texto("Nombre del repuesto: "),
        "marca": pedir_texto("Marca: "),
        "cantidad": pedir_entero("Cantidad: "),
        "fecha_ingreso": pedir_fecha("Fecha de ingreso (dd/mm/aaaa): ")
    }
    repuestos.append(repuesto)
    print("Repuesto agregado.")

def mostrar_repuesto(repuesto):
    print(f"Código: {repuesto['codigo']} | Nombre: {repuesto['nombre']} | "
          f"Marca: {repuesto['marca']} | Cantidad: {repuesto['cantidad']} | "
          f"Ingreso: {repuesto['fecha_ingreso']}")

def buscar_repuesto():
    if len(repuestos) == 0:
        print("No hay repuestos registrados todavía.")
        return
    codigo = pedir_entero("Código a buscar: ")
    for repuesto in repuestos:
        if repuesto["codigo"] == codigo:
            print("Repuesto encontrado:")
            mostrar_repuesto(repuesto)
            return
    print("No se encontró ningún repuesto con ese código.")

def actualizar_cantidad():
    print("Actualizar cantidad (en construcción)")

def consultar_lista():
    if len(repuestos) == 0:
        print("No hay repuestos registrados todavía.")
        return
    print("\n--- Lista de repuestos ---")
    for repuesto in repuestos:
        mostrar_repuesto(repuesto)
    print(f"Total: {len(repuestos)} repuesto(s).")

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
