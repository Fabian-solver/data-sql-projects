import sqlite3

def ejecutar_analiticas():
    # Conectamos a la base de datos
    conexion = sqlite3.connect('rendimiento_futbol.db')
    cursor = conexion.cursor()

    print("=== ANALÍTICA DE RENDIMIENTO DEPORTIVO (SQL) ===\n")

    # -------------------------------------------------------------------------
    # CONSULTA 1: Unir tablas (JOIN) para ver el rendimiento físico por jugador
    # Queremos saber el nombre del jugador, qué entrenamiento hizo y su velocidad punta.
    # -------------------------------------------------------------------------
    print("1. Rendimiento de velocidad por jugador y entrenamiento:")
    consulta_velocidad = '''
        SELECT j.nombre, s.tipo_entrenamiento, m.velocidad_max_kmh
        FROM metricas_rendimiento m
        JOIN jugadores j 
        ON m.id_jugador = j.id_jugador
        JOIN sesiones_entrenamiento s 
        ON m.id_sesion = s.id_sesion
        ORDER BY m.velocidad_max_kmh DESC;
    '''
    cursor.execute(consulta_velocidad)
    for fila in cursor.fetchall():
        print(f"   - {fila[0]} alcanzó {fila[2]} km/h en la sesión de '{fila[1]}'")
    
    print("\n" + "-"*50 + "\n")

    # -------------------------------------------------------------------------
    # CONSULTA 2: Agregación y Agrupación (GROUP BY + AVG)
    # Vamos a calcular la fatiga promedio y la carga máxima de fuerza por jugador.
    # -------------------------------------------------------------------------
    print("2. Resumen de carga física y fatiga media por jugador:")
    consulta_resumen = '''
        SELECT j.nombre, 
               AVG(m.fatiga_percibida) as fatiga_promedio, 
               MAX(m.carga_fuerza_kg) as carga_maxima_pesas
        FROM metricas_rendimiento m
        JOIN jugadores j 
        ON m.id_jugador = j.id_jugador
        GROUP BY j.id_jugador;
    '''
    cursor.execute(consulta_resumen)
    for fila in cursor.fetchall():
        print(f"   - {fila[0]}: Fatiga media de {fila[1]}/10 | Carga máx levantada: {fila[2]} kg")

    # Cerramos la conexión
    conexion.close()

if __name__ == "__main__":
    ejecutar_analiticas()