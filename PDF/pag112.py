asistentes = {}
categorias=["VIP", "Estudiante", "Patrocinador", "Ponente"]
def asignar_categoria():
    codigo=int(input("Ingresa codigo asistente: "))
    if codigo not in asistentes:
        asistentes[codigo] = []
    print("Categorías disponibles:", categorias)
    cat_a_asignar = input("Introduce las categorías a asignar (separadas por comas): ").split(',')
    cat_a_asignar = [categoria.strip() for categoria in cat_a_asignar]
    for categoria in cat_a_asignar:
        if categoria in categorias and categoria not in asistentes[codigo]:
            asistentes[codigo].append(categoria)
        elif categoria not in categorias:
            print(f"La categoría {categoria} no existe.")
        else:
            print(f"El asistente {codigo} ya tiene la categoría {categoria}.")


def mostrar_asistentes():
    if asistentes:
        print("\nLista de asistentes y sus categorías:")
        for codigo, categorias in asistentes.items():
            print(f"Código: {codigo}, Categorías: {', '.join(categorias)}")
    else:
        print("No hay asistentes registrados.")


def consultar_categoria():
    categoria = input("Introduce la categoría para consultar: ")
    if categoria in categorias:
        print(f"\nAsistentes en la categoría {categoria}:")
        for codigo, categorias in asistentes.items():
            if categoria in categorias:
                print(f"Código: {codigo}")
    else:
        print(f"La categoría {categoria} no existe.")


def eliminar_asistente():
    codigo = input("Introduce el código del asistente a eliminar: ")
    if codigo in asistentes:
        del asistentes[codigo]
        print(f"El asistente con código {codigo} ha sido eliminado.")
    else:
        print(f"El asistente con código {codigo} no existe.")
def menu():
    while True:
        print("\n--- Menú de gestión de asistentes ---")
        print("1. Asignar categorías a un asistente")
        print("2. Mostrar lista de asistentes y sus categorías")
        print("3. Consultar asistentes por categoría")
        print("4. Eliminar un asistente")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            asignar_categoria()
        elif opcion == "2":
            mostrar_asistentes()
        elif opcion == "3":
            consultar_categoria()
        elif opcion == "4":
            eliminar_asistente()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige de nuevo.")

# Llamamos al menú
menu()