import datetime

def dia_de_la_semana(dia, mes, año):
    try:
        fecha = datetime.date(año, mes, dia)
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return dias_semana[fecha.weekday()]
    except ValueError as e:
        return f"Error: {e}"

# Ejemplo de uso
dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
año = int(input("Ingresa el año: "))

resultado = dia_de_la_semana(dia, mes, año)
print(f"El {dia}/{mes}/{año} cayó en un {resultado}.")
28