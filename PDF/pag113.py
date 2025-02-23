# Diccionarios para almacenar clientes y eventos
clientes = {}
eventos = {}

# Función para añadir o modificar un cliente
def añadir_o_modificar_cliente():
    dni = input("Introduce el DNI del cliente: ")
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    categoria = input("Introduce la categoría del cliente (VIP, Estudiante, Senior): ")
    
    clientes[dni] = {
        "nombre": nombre,
        "telefono": telefono,
        "categoria": categoria
    }
    print(f"Cliente {nombre} con DNI {dni} añadido/modificado exitosamente.")

# Función para buscar un cliente
def buscar_cliente():
    print("Buscar cliente por:")
    print("1. DNI")
    print("2. Nombre")
    print("3. Categoría")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    if opcion == "1":
        dni = input("Introduce el DNI del cliente: ")
        if dni in clientes:
            cliente = clientes[dni]
            print(f"DNI: {dni}, Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}, Categoría: {cliente['categoria']}")
        else:
            print("Cliente no encontrado.")
    
    elif opcion == "2":
        nombre = input("Introduce el nombre del cliente: ")
        encontrado = False
        for dni, cliente in clientes.items():
            if cliente['nombre'].lower() == nombre.lower():
                print(f"DNI: {dni}, Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}, Categoría: {cliente['categoria']}")
                encontrado = True
        if not encontrado:
            print("Cliente no encontrado.")
    
    elif opcion == "3":
        categoria = input("Introduce la categoría del cliente (VIP, Estudiante, Senior): ")
        encontrado = False
        for dni, cliente in clientes.items():
            if cliente['categoria'].lower() == categoria.lower():
                print(f"DNI: {dni}, Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}, Categoría: {cliente['categoria']}")
                encontrado = True
        if not encontrado:
            print("No se encontraron clientes en esta categoría.")
    
    else:
        print("Opción no válida.")

# Función para crear un evento
def crear_evento():
    evento_nombre = input("Introduce el nombre del evento (por ejemplo: Nochevieja_VIP): ")
    categoria = input("Introduce la categoría del evento (VIP, Estudiante, Senior): ")
    
    if evento_nombre not in eventos:
        eventos[evento_nombre] = {"categoria": categoria, "asistentes": set()}
        print(f"Evento {evento_nombre} creado con éxito.")
    else:
        print(f"El evento {evento_nombre} ya existe.")

# Función para añadir asistente a un evento
def añadir_asistente_a_evento():
    evento_nombre = input("Introduce el nombre del evento: ")
    if evento_nombre in eventos:
        dni = input("Introduce el DNI del asistente: ")
        if dni in clientes:
            if clientes[dni]["categoria"].lower() == eventos[evento_nombre]["categoria"].lower():
                eventos[evento_nombre]["asistentes"].add(dni)
                print(f"El asistente con DNI {dni} ha sido añadido al evento {evento_nombre}.")
            else:
                print(f"El asistente con DNI {dni} no pertenece a la categoría correcta para este evento.")
        else:
            print(f"El cliente con DNI {dni} no existe.")
    else:
        print(f"El evento {evento_nombre} no existe.")

# Función para listar los eventos
def listar_eventos():
    if eventos:
        print("\nLista de eventos:")
        for evento, datos in eventos.items():
            print(f"Evento: {evento}, Categoría: {datos['categoria']}, Asistentes: {', '.join(datos['asistentes'])}")
    else:
        print("No hay eventos registrados.")

# Menú de opciones
def menu():
    while True:
        print("\n--- Menú de gestión de clientes y eventos ---")
        print("1. Añadir/Modificar Cliente")
        print("2. Buscar Cliente")
        print("3. Crear Evento")
        print("4. Añadir Asistente a Evento")
        print("5. Listar Eventos")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            añadir_o_modificar_cliente()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            crear_evento()
        elif opcion == "4":
            añadir_asistente_a_evento()
        elif opcion == "5":
            listar_eventos()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige de nuevo.")

# Llamada al menú
menu()
