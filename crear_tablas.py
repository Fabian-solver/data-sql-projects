import sqlite3

def inicializar_base_de_datos():
    # 1. Conectar a la base de datos (si no existe, se creará automáticamente el archivo 'rendimiento_futbol.db')
    conexion = sqlite3.connect('rendimiento_futbol.db')
    cursor = conexion.cursor()

    print("Conexión establecida con SQLite. Creando tablas...")

    # 2. Crear tabla de Jugadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugadores (
            id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            posicion TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL
        )
    ''')

    # 3. Crear tabla de Sesiones de Entrenamiento
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sesiones_entrenamiento (
            id_sesion INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            tipo_entrenamiento TEXT NOT NULL,
            duracion_minutos INTEGER NOT NULL
        )
    ''')

    # 4. Crear tabla de Métricas de Rendimiento (con Claves Foráneas)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metricas_rendimiento (
            id_metrica INTEGER PRIMARY KEY AUTOINCREMENT,
            id_jugador INTEGER,
            id_sesion INTEGER,
            velocidad_max_kmh REAL,
            carga_fuerza_kg REAL,
            fatiga_percibida INTEGER,
            FOREIGN KEY (id_jugador) 
            REFERENCES jugadores (id_jugador) 
            ON DELETE CASCADE,
            FOREIGN KEY (id_sesion) 
            REFERENCES sesiones_entrenamiento (id_sesion) 
            ON DELETE CASCADE
        )
    ''')

    # 5. Crear tabla de Partidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS partidos (
            id_partido INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            rival TEXT NOT NULL,
            resultado TEXT,
            minutos_jugados_equipo INTEGER
        )
    ''')

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("¡Base de datos y tablas creadas con éxito!")

if __name__ == "__main__":
    inicializar_base_de_datos()