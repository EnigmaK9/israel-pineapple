import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Conexión a la base de datos (se crea el archivo peluches.db si no existe)
    conexion = sqlite3.connect("peluches.db")
    cursor = conexion.cursor()

    # 2. Crear tabla si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produccion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hora TEXT,
        modelo TEXT,
        producidos INTEGER,
        defectuosos INTEGER
    )
    """)

    # 3. Limpiar e insertar datos de ejemplo (como los que arrojaría un PLC / SCADA)
    cursor.execute("DELETE FROM produccion")
    
    datos_ejemplo = [
        ("08:00", "Oso Teddy", 50, 2),
        ("09:00", "Oso Teddy", 55, 1),
        ("10:00", "Oso Teddy", 40, 5),
        ("11:00", "Oso Teddy", 60, 0),
        ("12:00", "Oso Teddy", 30, 8), # Aquí pasó algo raro en la máquina
        ("13:00", "Oso Teddy", 58, 2),
    ]

    cursor.executemany("""
    INSERT INTO produccion (hora, modelo, producidos, defectuosos)
    VALUES (?, ?, ?, ?)
    """, datos_ejemplo)

    conexion.commit()
    print("✅ Datos de SCADA guardados en 'peluches.db'")

    # 4. Consultar los datos con Pandas (como un SELECT de SQL)
    df = pd.read_sql_query("SELECT hora, producidos, defectuosos FROM produccion", conexion)
    conexion.close()

    print("\n--- REPORTE TABULAR DE FÁBRICA ---")
    print(df)

    # 5. Generar Dashboard Visual (Gráfica de Tendencia)
    plt.figure(figsize=(9, 4.5))
    
    # Línea de producción
    plt.plot(df["hora"], df["producidos"], marker="o", color="#2b5c8f", label="Buenos Producidos", linewidth=2)
    # Línea de defectuosos
    plt.plot(df["hora"], df["defectuosos"], marker="s", color="#d9534f", linestyle="--", label="Defectuosos", linewidth=2)

    plt.title("Línea 1: Fábrica de Peluches - Tendencia de Turno Matutino", fontsize=13, fontweight="bold")
    plt.xlabel("Hora del Día")
    plt.ylabel("Cantidad de Peluches")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Guardar gráfico como reporte visual
    archivo_grafica = "dashboard_peluches.png"
    plt.savefig(archivo_grafica, dpi=120)
    print(f"\n📊 Dashboard generado con éxito: '{archivo_grafica}'")

if __name__ == "__main__":
    main()
