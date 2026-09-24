# 🧸 Plush Toy Factory - SCADA Monitoring & Analytics Dashboard

An end-to-end industrial SCADA monitoring and analytics solution for a plush toy manufacturing line. This project combines automated telemetry tracking, SQLite relational storage, interactive web dashboards (Streamlit & Chart.js), and automated reporting tools.

---

## 📌 Project Overview

In high-volume manufacturing environments, tracking machine telemetry—such as cycle times, scrap rates, and thermal conditions—is critical to preventing downtime and minimizing defective inventory.

This repository demonstrates how to build a zero-license, highly scalable monitoring stack using **Python**, **SQLite**, and **Streamlit** to collect, store, and visualize PLC/SCADA operational metrics.

---

## 🚀 Key Features

- **Interactive SCADA Dashboard**: Built with [Streamlit](https://streamlit.io/) and Altair for real-time production monitoring and scrap rate analysis.
- **Relational Data Storage**: Clean SQLite schema modeling manufacturing lines and timestamped sensor/PLC pulses.
- **Live Pulse Simulation**: Simulate real-time PLC events directly from the dashboard sidebar.
- **Static Visual Reports**: Automated Matplotlib script to generate shift performance charts (`.png`).
- **Web-Ready Standalone UI**: Minimalist HTML5 + Chart.js dashboard with zero backend dependencies.
- **Spreadsheet Integration**: Automated CSV export for Excel, LibreOffice Calc, or Google Sheets.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Database**: SQLite3
- **Web Dashboard**: Streamlit, Altair
- **Data Analysis**: Pandas
- **Visualization**: Matplotlib, Chart.js
- **Export Formats**: CSV, PNG, SQLite (`.db`)

---

## 📂 Repository Structure

```text
israel-pineapple/
├── docs/
│   ├── presentation_slides.tex # 10-slide Beamer presentation (7x7 rule for 10-minute briefing)
│   ├── presentation_slides.pdf # Compiled presentation slides ready for projection
│   ├── acordeon_estudio.tex    # LaTeX source for the 10-minute Spanish presentation cheat sheet
│   ├── acordeon_estudio.pdf    # Compiled Spanish study guide with verbatim script & trap Q&As
│   ├── architecture.md         # Detailed multi-tier SCADA architecture & pipeline specs
│   ├── user_guide.md           # Step-by-step intern handbook explained with metaphors
│   ├── contributions.md        # Git workflow, PR conventions, and code standards
│   ├── swe_intern_guide.tex    # Comprehensive LaTeX source for the PDF manual
│   └── swe_intern_guide.pdf    # Compiled 6-page professional engineering handbook
├── app_dashboard.py            # Main interactive Streamlit SCADA dashboard
├── db_setup.py                 # SQLite schema initialization & historical data generator
├── dashboard_peluches.py        # Standalone Python script for generating Matplotlib PNG reports
├── dashboard_web.html          # Lightweight HTML5 + Chart.js dashboard
├── generar_csv.py              # CSV exporter for spreadsheet analysis
├── dashboard_peluches.png      # Sample exported shift summary chart
├── fabrica_peluches.db         # SQLite database with production line tables and telemetry
├── peluches.db                 # Minimal SQLite database for simple shift tracking
└── scada_peluches.csv          # Sample generated SCADA CSV dataset
```

---

## 📚 Documentation, Slides & Study Materials

Comprehensive guides and presentation resources are available in the [`docs/`](./docs) directory:

1. 🎯 **[10-Slide Presentation (PDF)](./docs/presentation_slides.pdf)**: 10 slides strictly formatted under the **7$\times$7 presentation rule** ($\le 7$ lines/slide, $\le 7$ words/line) designed for a 10-minute technical pitch.
2. 📝 **[Acordeón de Exposición en Español (PDF)](./docs/acordeon_estudio.pdf)**: Guía de estudio minuto a minuto (del min 0 al 10) con guion textual en español, explicación sencilla con bolitas y palitos, y respuestas a preguntas trampa para la audiencia.
3. 🏛️ **[System Architecture](./docs/architecture.md)**: Hardware layers, PLC telemetry simulation, SQLite ER diagrams, and KPI mathematical formulations.
4. 🧸 **[Beginner's User Guide ("Balls and Sticks")](./docs/user_guide.md)**: A step-by-step walkthrough explaining every file, button, and SQL query with zero assumptions.
5. 🤝 **[Contribution Guidelines](./docs/contributions.md)**: Branching models, PEP 8 standards, parameterized SQL practices, and PR checklists.
6. 📄 **[SWE Intern Handbook (PDF)](./docs/swe_intern_guide.pdf)**: A 6-page printable manual compiled with LaTeX covering end-to-end industrial software engineering concepts.


---

## ⚡ Quickstart Guide

### 1. Clone the Repository

```bash
git clone https://github.com/EnigmaK9/israel-pineapple.git
cd israel-pineapple
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

Populate the database with production lines and simulated telemetry:

```bash
python db_setup.py
```

### 5. Launch the Dashboard

Run the Streamlit application in your browser:

```bash
streamlit run app_dashboard.py
```

The application will be accessible at `http://localhost:8501`.

---

## 🗄️ Database Architecture

The system utilizes two primary tables connected via foreign key:

### `lineas` (Production Lines)
| Column | Type | Description |
|---|---|---|
| `id_linea` | INTEGER PRIMARY KEY | Unique production line identifier |
| `nombre` | TEXT | Line name (e.g., Sewing, Stuffing, Embroidery) |
| `modelo_peluche` | TEXT | Plush toy model produced (e.g., Classic Teddy, Husky, Giant Panda) |

### `produccion_scada` (Telemetry Records)
| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | Record ID |
| `id_linea` | INTEGER | Foreign key to `lineas.id_linea` |
| `fecha_hora` | TEXT | Timestamp / Shift hour |
| `piezas_buenas` | INTEGER | Valid units completed |
| `piezas_defectuosas` | INTEGER | Defective units / scrap count |
| `temperatura_maquina` | REAL | Machine tool head temperature (°C) |

---

## 📊 Available Dashboards & Outputs

### 1. Interactive Streamlit Dashboard (`app_dashboard.py`)
- Real-time line selector.
- Live scrap percentage and machine status indicator (`Optimal` vs `Action Required`).
- Interactive trend graphs comparing good units vs defects.
- Thermal gradient area charts.

### 2. Static PNG Shift Summary (`dashboard_peluches.py`)
Run:
```bash
python dashboard_peluches.py
```
Outputs `dashboard_peluches.png` suitable for shift handover reports and email attachments.

### 3. Web Dashboard (`dashboard_web.html`)
Open `dashboard_web.html` directly in any web browser to view a lightweight Chart.js client-side interface.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
