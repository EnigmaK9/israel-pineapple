import csv

# Generar un CSV compatible con Excel, LibreOffice Calc o Google Sheets
datos_csv = [
    ["Hora", "Modelo", "Producidos", "Defectuosos", "% Defecto"],
    ["08:00", "Oso Teddy", 50, 2, "=D2/C2"],
    ["09:00", "Oso Teddy", 55, 1, "=D3/C3"],
    ["10:00", "Oso Teddy", 40, 5, "=D4/C4"],
    ["11:00", "Oso Teddy", 60, 0, "=D5/C5"],
    ["12:00", "Oso Teddy", 30, 8, "=D6/C6"],
    ["13:00", "Oso Teddy", 58, 2, "=D7/C7"],
]

with open("scada_peluches.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(datos_csv)

print("✅ 'scada_peluches.csv' creado para abrir con Excel.")
