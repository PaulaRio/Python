class Asistente:
    categoriaDisponible = {"VIP", "Estudiante", "Patrocinador", "Pobre"}

    def __init__(self, id):
        self.id = id
        self.categorias = set() 

    def __str__(self):
        return f"ID: {self.id}, Categorías: {', '.join(self.categorias) if self.categorias else 'Sin categoría'}"

    def agregar_categoria(self, categoria):
        if categoria in Asistente.categoriaDisponible:
            self.categorias.add(categoria) 
            print(f"Categoría '{categoria}' añadida a {self.id}.")
        else:
            print(f"Error: '{categoria}' no es una categoría válida.")


class Evento:
    def __init__(self):
        self.asistentes = {}  

    def agregar_asistente(self, id_asistente):
        if id_asistente not in self.asistentes:
            self.asistentes[id_asistente] = Asistente(id_asistente)
            print(f"Asistente {id_asistente} agregado.")
        else:
            print(f"El asistente {id_asistente} ya está registrado.")

    def asignar_categoria(self, id_asistente, categoria):
        if id_asistente in self.asistentes:
            self.asistentes[id_asistente].agregar_categoria(categoria)
        else:
            print(f"Error: Asistente {id_asistente} no encontrado.")

    def mostrar_asistentes(self):
        if self.asistentes:
            for asistente in self.asistentes.values():
                print(asistente)
        else:
            print("No hay asistentes registrados.")

    def asistentes_por_categoria(self, categoria):
        if categoria not in Asistente.categoriaDisponible:
            print(f"Error: '{categoria}' no es una categoría válida.")
            return
        asistentes_en_categoria = [a.id for a in self.asistentes.values() if categoria in a.categorias]
        if asistentes_en_categoria:
            print(f"Asistentes en categoría '{categoria}': {', '.join(asistentes_en_categoria)}")
        else:
            print(f"No hay asistentes en la categoría '{categoria}'.")

    def eliminar_asistente(self, id_asistente):
        if id_asistente in self.asistentes:
            del self.asistentes[id_asistente]
            print(f"Asistente {id_asistente} eliminado.")
        else:
            print(f"Error: Asistente {id_asistente} no encontrado.")


evento = Evento()
evento.agregar_asistente("A001")
evento.asignar_categoria("A001", "VIP")
evento.asignar_categoria("A001", "Estudiante")
evento.mostrar_asistentes()
evento.asistentes_por_categoria("VIP")
evento.eliminar_asistente("A001")
evento.mostrar_asistentes()
