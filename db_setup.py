import sqlite3
import random
from datetime import datetime, timedelta

def init_db():
    conn = sqlite3.connect("fabrica_peluches.db")
    cur = conn.cursor()

    # 1. Tabla de Líneas de producción (máquinas)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lineas (
        id_linea INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        modelo_peluche TEXT NOT NULL
    )
    """)

    # 2. Tabla de Registros de producción tipo SCADA/PLC
    cur.execute("""
    CREATE TABLE IF NOT EXISTS produccion_scada (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_linea INTEGER,
        fecha_hora TEXT NOT NULL,
        piezas_buenas INTEGER NOT NULL,
        piezas_defectuosas INTEGER NOT NULL,
        temperatura_maquina REAL NOT NULL,
        FOREIGN KEY (id_linea) REFERENCES lineas(id_linea)
    )
    """)

    # Insertar líneas si no existen
    cur.execute("DELETE FROM produccion_scada")
    cur.execute("DELETE FROM lineas")

    cur.executemany("INSERT INTO lineas VALUES (?, ?, ?)", [
        (1, "Línea 1 - Costura Principal", "Oso Teddy Clásico"),
        (2, "Línea 2 - Relleno y Acabados", "Perrito Husky"),
        (3, "Línea 3 - Bordados Ojos/Nariz", "Panda Gigante")
    ])

    # Generar lecturas de las últimas 8 horas para cada línea
    hora_base = datetime.now() - timedelta(hours=8)
    registros = []

    for i in range(8):
        t = hora_base + timedelta(hours=i)
        hora_str = t.strftime("%H:00")
        
        # Línea 1
        buenas = random.randint(45, 60)
        malas = random.randint(0, 3)
        temp = round(random.uniform(65.0, 72.0), 1)
        # Provocar una falla a las 12:00
        if hora_str == "12:00":
            buenas = 25
            malas = 10
            temp = 85.5
        registros.append((1, hora_str, buenas, malas, temp))

        # Línea 2
        buenas_2 = random.randint(35, 50)
        malas_2 = random.randint(0, 2)
        temp_2 = round(random.uniform(55.0, 62.0), 1)
        registros.append((2, hora_str, buenas_2, malas_2, temp_2))

        # Línea 3
        buenas_3 = random.randint(50, 70)
        malas_3 = random.randint(1, 4)
        temp_3 = round(random.uniform(50.0, 58.0), 1)
        registros.append((3, hora_str, buenas_3, malas_3, temp_3))

    cur.executemany("""
    INSERT INTO produccion_scada (id_linea, fecha_hora, piezas_buenas, piezas_defectuosas, temperatura_maquina)
    VALUES (?, ?, ?, ?, ?)
    """, registros)

    conn.commit()
    conn.close()
    print("✅ Base de datos 'fabrica_peluches.db' inicializada con éxito con tablas y relaciones SQL.")

if __name__ == "__main__":
    init_db()
