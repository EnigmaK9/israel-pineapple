import streamlit as st
import sqlite3
import pandas as pd
import altair as alt

st.set_page_config(page_title="Fábrica de Peluches - Dashboard SCADA", layout="wide", page_icon="🧸")

st.title("🧸 Dashboard SCADA: Monitoreo Fábrica de Peluches")
st.markdown("Datos consultados directamente con **SQL (SQLite)** desde los registros de planta.")

# 1. Función para consultar SQLite
def consultar_sql(query, params=()):
    with sqlite3.connect("fabrica_peluches.db") as conn:
        return pd.read_sql_query(query, conn, params=params)

# 2. Selector en la barra lateral (Interacción)
lineas_df = consultar_sql("SELECT id_linea, nombre, modelo_peluche FROM lineas")
opciones = {f"{row['nombre']} ({row['modelo_peluche']})": row['id_linea'] for _, row in lineas_df.iterrows()}

linea_seleccionada = st.sidebar.selectbox("Selecciona la Línea de Producción:", list(opciones.keys()))
id_linea_activa = opciones[linea_seleccionada]

# Botón para simular que el PLC manda un nuevo registro en tiempo real
if st.sidebar.button("⚡ Simular pulso SCADA (+1 lectura de PLC)"):
    with sqlite3.connect("fabrica_peluches.db") as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO produccion_scada (id_linea, fecha_hora, piezas_buenas, piezas_defectuosas, temperatura_maquina)
            VALUES (?, '14:00 (En vivo)', 62, 1, 68.4)
        """, (id_linea_activa,))
        conn.commit()
    st.sidebar.success("¡Nuevo pulso guardado en SQL!")

# 3. Consulta SQL con JOIN y Filtro
query = """
SELECT 
    p.fecha_hora,
    p.piezas_buenas,
    p.piezas_defectuosas,
    p.temperatura_maquina,
    l.nombre AS linea,
    l.modelo_peluche
FROM produccion_scada p
JOIN lineas l ON p.id_linea = l.id_linea
WHERE p.id_linea = ?
ORDER BY p.id ASC
"""
df = consultar_sql(query, (id_linea_activa,))

# 4. Métricas / KPIs Principales (Cards)
total_buenas = int(df['piezas_buenas'].sum())
total_malas = int(df['piezas_defectuosas'].sum())
pct_scrap = round((total_malas / (total_buenas + total_malas)) * 100, 2) if (total_buenas + total_malas) > 0 else 0
temp_promedio = round(df['temperatura_maquina'].mean(), 1)

col1, col2, col3, col4 = st.columns(4)
col1.metric("🧸 Total Peluches Buenos", f"{total_buenas} pcs")
col2.metric("❌ Defectuosos / Merma", f"{total_malas} pcs", delta=f"{pct_scrap}% scrap", delta_color="inverse")
col3.metric("🌡️ Temp. Promedio Máquina", f"{temp_promedio} °C")
col4.metric("⚙️ Estado Línea", "Óptimo" if pct_scrap < 5 else "⚠️ Revisión Requerida")

st.divider()

# 5. Gráficas de Tendencia con Python
col_graf1, col_graf2 = st.columns([2, 1])

with col_graf1:
    st.subheader("📈 Tendencia de Producción vs Defectos por Hora")
    # Gráfica de líneas interactiva
    chart_data = df.melt(id_vars=['fecha_hora'], value_vars=['piezas_buenas', 'piezas_defectuosas'],
                         var_name='Tipo', value_name='Cantidad')
    chart = alt.Chart(chart_data).mark_line(point=True).encode(
        x=alt.X('fecha_hora', title='Hora de Turno'),
        y=alt.Y('Cantidad', title='Piezas'),
        color=alt.Color('Tipo', scale=alt.Scale(domain=['piezas_buenas', 'piezas_defectuosas'], range=['#2ecc71', '#e74c3c'])),
        tooltip=['fecha_hora', 'Tipo', 'Cantidad']
    ).properties(height=350)
    st.altair_chart(chart, use_container_width=True)

with col_graf2:
    st.subheader("🌡️ Temperatura del Cabezal")
    temp_chart = alt.Chart(df).mark_area(
        line={'color': '#f39c12'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='#f39c12', offset=0),
                   alt.GradientStop(color='rgba(243, 156, 18, 0.1)', offset=1)],
            x1=1, x2=1, y1=1, y2=0
        )
    ).encode(
        x=alt.X('fecha_hora', title='Hora'),
        y=alt.Y('temperatura_maquina', scale=alt.Scale(zero=False), title='Temp (°C)'),
        tooltip=['fecha_hora', 'temperatura_maquina']
    ).properties(height=350)
    st.altair_chart(temp_chart, use_container_width=True)

st.subheader("📋 Datos Crudos desde la Base de Datos SQLite (SELECT * ...)")
st.dataframe(df[['fecha_hora', 'piezas_buenas', 'piezas_defectuosas', 'temperatura_maquina']], use_container_width=True)
