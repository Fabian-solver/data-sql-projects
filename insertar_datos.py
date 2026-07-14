import sqlite3

def registrar_datos_de_prueba():
    # Conectamos a la base de datos existente
    conexion = sqlite3.connect('rendimiento_futbol.db')
    cursor = conexion.cursor()

    print("Conectando a la base de datos para registrar datos de prueba...")

    # 1. Insertar Jugadores
    # Usamos INSERT OR IGNORE o simplemente controlamos no duplicar si ejecutas este script varias veces
    jugadores = [
        ('Fabian', 'Centrocampista', '2001-05-15'),
        ('Carlos', 'Delantero', '1999-08-22'),
        ('Dani', 'Defensa', '2002-11-03')
    ]
    cursor.executemany('''
        INSERT INTO jugadores (nombre, posicion, fecha_nacimiento) 
        VALUES (?, ?, ?)
    ''', jugadores)

    # 2. Insertar Sesiones de Entrenamiento
    # Metemos sesiones con los tipos de trabajo físico que se suelen hacer en pretemporada
    sesiones = [
        ('2026-07-10', 'Carrera continua', 45),
        ('2026-07-12', 'Fuerza explosiva', 60),
        ('2026-07-13', 'Agilidad y pliometría', 50)
    ]
    cursor.executemany('''
        INSERT INTO sesiones_entrenamiento (fecha, tipo_entrenamiento, duracion_minutos) 
        VALUES (?, ?, ?)
    ''', sesiones)

    # Guardamos los cambios temporalmente para obtener los IDs generados
    conexion.commit()

    # 3. Insertar Métricas de Rendimiento
    # Conectamos manualmente los IDs de los jugadores con las sesiones creadas
    # Ejemplo: Fabian (ID 1) en la sesión de Fuerza explosiva (ID 2) y Carrera continua (ID 1)
    metricas = [
        # (id_jugador, id_sesion, velocidad_max_kmh, carga_fuerza_kg, fatiga_percibida)
        (1, 1, 24.5, 0.0, 6),   # Fabian - Carrera continua (mucha carrera, sin carga de pesas)
        (1, 2, 18.2, 85.0, 8),  # Fabian - Fuerza explosiva (poca velocidad punta, mucha carga)
        (2, 1, 29.8, 0.0, 5),   # Carlos - Carrera continua
        (2, 2, 19.5, 70.0, 7),  # Carlos - Fuerza explosiva
        (3, 3, 26.0, 40.0, 6)   # Dani - Agilidad y pliometría
    ]
    cursor.executemany('''
        INSERT INTO metricas_rendimiento (id_jugador, id_sesion, velocidad_max_kmh, carga_fuerza_kg, fatiga_percibida)
        VALUES (?, ?, ?, ?, ?)
    ''', metricas)

    # 4. Insertar Partidos de competición
    partidos = [
        ('2026-07-05', 'Rayo Vallecano', '2-1', 90),
        ('2026-07-11', 'Getafe CF', '1-1', 90)
    ]
    cursor.executemany('''
        INSERT INTO partidos (fecha, rival, resultado, minutos_jugados_equipo)
        VALUES (?, ?, ?, ?)
    ''', partidos)

    # Confirmamos definitivamente todos los inserts
    conexion.commit()
    conexion.close()
    print("¡Datos de prueba insertados con éxito en todas las tablas!")

if __name__ == "__main__":
    registrar_datos_de_prueba()