##  Analítica de Rendimiento Deportivo

Este es mi primer pequeño proyecto el cual consiste en el diseño, desarrollo e implementación de una base de datos relacional local enfocada en el seguimiento físico y analítico de entrenamientos de fútbol. El objetivo es estructurar, automatizar y consultar métricas de rendimiento deportivo para la toma de decisiones técnicas.

Este repositorio demuestra habilidades prácticas que complementan mi certificación **Microsoft Azure Data Fundamentals (DP-900)**, aplicando teoría directamente en código real.

---

### Arquitectura de Datos y Modelo Relacional

La base de datos consta de 4 tablas principales vinculadas mediante llaves primarias y foráneas:

-   **`jugadores`**: Datos maestros del plantel (ID, nombre, posición, fecha de nacimiento).
-   **`sesiones_entrenamiento`**: Historial de entrenamientos físicos (carrera continua, fuerza explosiva, agilidad, pliometría).
-   **`metricas_rendimiento`**: Tabla puente que registra el rendimiento individual de un jugador en una sesión específica (velocidad punta, carga de fuerza y escala de fatiga percibida).
-   **`partidos`**: Registro de encuentros oficiales, rivales, resultados y minutos disputados.

---

### Estructura del Proyecto

-   `crear_tablas.py`: Script encargado de inicializar la base de datos `rendimiento_futbol.db` y crear los esquemas DDL de las tablas relacionales.
-   `insertar_datos.py`: Automatización DML en Python para registrar datos realistas de prueba en el sistema.
-   `consultas.py`: Script con consultas SQL complejas utilizando sentencias `JOIN`, agregaciones (`AVG`, `MAX`) y agrupamientos (`GROUP BY`) para extraer métricas clave del equipo.
