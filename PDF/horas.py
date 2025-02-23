from datetime import datetime
'''Si la clase termina a las 14:30 horas, ¿cuánto
tiempo le queda para terminar la clase de hoy?'''
# Hora actual
hora_actual = datetime.now()

# Hora final de la clase (14:30)
hora_final_clase = hora_actual.replace(hour=14, minute=30, second=0, microsecond=0)

# Si ya pasó la hora final (es decir, es después de las 14:30), entonces la clase ya terminó
if hora_actual > hora_final_clase:
    print("La clase ya terminó.")
else:
    # Calcular cuánto tiempo queda para las 14:30
    tiempo_restante = hora_final_clase - hora_actual
    print(f"Te quedan {tiempo_restante} hasta las 14:30.")
