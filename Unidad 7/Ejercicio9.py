# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora

agenda = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Cita con el dentista',
    ('Miércoles', '09:00'): 'Clase de yoga',
    ('Jueves', '16:00'): 'Llamada con cliente',
    ('Viernes', '12:00'): 'Almuerzo con amigos'
}

def consultar_evento(dia, hora):
    evento = agenda.get((dia, hora))
    if evento:
        return f'El evento programado para el {dia} a las {hora} es: {evento}'
    else:
        return f'No hay eventos programados para el {dia} a las {hora}.'   
    

print(consultar_evento('Lunes', '10:00'))
print(consultar_evento('Martes', '14:00'))
print(consultar_evento('Sábado', '10:00'))
