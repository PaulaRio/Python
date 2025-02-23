from datetime import datetime

# Solicitar la fecha de cumpleaños al usuario
fecha_cumple = input("Introduce tu fecha de cumpleaños (formato: dd-mm-yyyy): ")

# Convertir la fecha de cumpleaños ingresada en un objeto datetime
cumpleaños = datetime.strptime(fecha_cumple, "%d-%m-%Y")

# Fecha actual
hoy = datetime.today()

# Si el cumpleaños ya pasó este año, calculamos el siguiente año
if hoy.month > cumpleaños.month or (hoy.month == cumpleaños.month and hoy.day > cumpleaños.day):
    cumpleaños = cumpleaños.replace(year=hoy.year + 1)
else:
    cumpleaños = cumpleaños.replace(year=hoy.year)

# Calcular los días faltantes
dias_faltantes = (cumpleaños - hoy).days

print(f"Faltan {dias_faltantes} días para tu cumpleaños.")
