# 🧸 User Guide & Intern Handbook: "Plush Toys with Balls and Sticks" 🔴🍡

Hello and welcome, fellow engineer! 👋

If you are a Junior Software Engineer, a SWE intern, or someone who is looking at this codebase and wondering:
> *"What on earth is a SCADA? Why are there plush toys? What does this Python code actually do?"*

**Don't panic!** This guide is designed to explain everything from scratch with **"bolitas y palitos"** (crystal-clear, zero-jargon metaphors).

---

## 1. The Story (The Big Picture)

Imagine your company owns a **giant factory making plush toys**:
1. **Station 1** sews the soft bodies of **Teddy Bears** 🐻.
2. **Station 2** fills **Husky Puppies** with fluffy cotton 🐶.
3. **Station 3** stitches sparkling eyes and noses onto **Giant Pandas** 🐼.

Every station has a heavy machine with an internal computer called a **PLC** (Programmable Logic Controller). Every hour, the machine counts:
- How many plush toys were made nicely (**good pieces** ✅)
- How many came out torn or missing an ear (**defective scrap** ❌)
- How hot the sewing needle or motor got (**temperature in °C** 🌡️)

**Our job as Software Engineers:**
Take those numbers, save them in a clean database, and draw colorful dashboards so the Factory Boss can see if a machine is catching fire or making too many broken toys!

---

## 2. Directory Tour: What Does Each File Do?

Think of our files as a team in a restaurant kitchen:

```
israel-pineapple/
│
├── db_setup.py            --> 🧑‍🍳 THE CHEF: Creates the database file and puts food (data) in it.
├── fabrica_peluches.db    --> 📦 THE PANTRY: The SQLite database file where tables live.
├── app_dashboard.py       --> 🖥️ THE WAITER (Interactive UI): The Streamlit web app with buttons and live graphs.
├── dashboard_peluches.py  --> 📸 THE POLAROID CAMERA: Takes data and saves a nice chart picture (PNG).
├── dashboard_peluches.png --> 🖼️ THE PHOTO: The generated chart image.
├── dashboard_web.html     --> 🌐 THE SIMPLE WEBSITE: Pure HTML + JavaScript dashboard that runs anywhere.
├── generar_csv.py         --> 📊 THE EXCEL REPORT: Exports data into a spreadsheet for accounting.
└── requirements.txt       --> 📜 THE SHOPPING LIST: Python packages you need to install.
```

---

## 3. Step-by-Step: How to Run Everything (5 Minutes)

### Step 1: Open your Terminal
Open your Linux terminal (or macOS / Windows terminal) and go inside the folder:
```bash
cd ~/github/israel-pineapple
```

### Step 2: Create a Virtual Room (Virtual Environment)
In Python, we always build a clean "room" so we don't mess up our computer's main Python packages:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
*(You will see `(.venv)` appear in front of your terminal prompt! That means you are safe inside your clean room).*

### Step 3: Install the Tools
Install the required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 4: Create and Fill the Database
Before you can see graphs, you need data! Run the setup script:
```bash
python db_setup.py
```
**What happens?**
It creates `fabrica_peluches.db`, creates 2 tables (`lineas` and `produccion_scada`), and generates 8 hours of telemetry data for 3 plush toy lines.

### Step 5: Launch the Streamlit Dashboard! 🚀
Now for the coolest part:
```bash
streamlit run app_dashboard.py
```
Your web browser will automatically open with `http://localhost:8501`.

---

## 4. How to Use the Dashboard

When the dashboard opens, look at the screen:

1. **Sidebar Dropdown (Left side)**:
   - Click it to switch between:
     - `Línea 1 - Costura Principal (Oso Teddy Clásico)`
     - `Línea 2 - Relleno y Acabados (Perrito Husky)`
     - `Línea 3 - Bordados Ojos/Nariz (Panda Gigante)`
   - Every time you pick a different line, the SQL database runs a new query instantly!

2. **The "⚡ Simular pulso SCADA" Button**:
   - Imagine a plush toy just rolled off the conveyor belt right now!
   - Click this button. It sends an `INSERT` command into SQLite and recalculates all the graphs live!

3. **The 4 KPI Cards (Top)**:
   - **Total Good Units**: Total number of finished toys.
   - **Scrap / Defects**: Shows the percentage of bad toys. If it goes over 5%, a warning appears!
   - **Avg Temperature**: Average machine head temperature.
   - **Line Status**: Says `Óptimo` (green) or `⚠️ Revisión Requerida` (orange) if defects are too high.

4. **The Graphs**:
   - **Green line**: Good toys produced each hour.
   - **Red dashed line**: Defective toys. Notice what happened at 12:00 in Line 1!
   - **Orange gradient chart**: Temperature of the machine over time.

---

## 5. Other Cool Utilities in This Repo

### Generating an Image Report
Need to send an image to your boss on WhatsApp or email? Run:
```bash
python dashboard_peluches.py
```
This script queries `peluches.db`, uses Matplotlib to draw the lines, and saves `dashboard_peluches.png`.

### Generating an Excel Spreadsheet
Need numbers for accountants? Run:
```bash
python generar_csv.py
```
This produces `scada_peluches.csv` which can be opened directly in Microsoft Excel, LibreOffice Calc, or Google Drive.

### Opening the Static HTML Page
Double-click `dashboard_web.html` in your file browser (or open with Chrome/Brave/Firefox). It uses Chart.js directly in the browser with zero Python required!

---

## 6. Common Questions & Troubleshooting (FAQ)

### Q: "I got `ModuleNotFoundError: No module named 'streamlit'`!"
**A:** You forgot to activate your virtual environment or install the dependencies. Run:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Q: "How do I stop Streamlit?"
**A:** In the terminal window where Streamlit is running, press `Ctrl + C`.

### Q: "Can I inspect the SQLite database directly?"
**A:** Yes! You can use the `sqlite3` CLI tool:
```bash
sqlite3 fabrica_peluches.db "SELECT * FROM lineas;"
```
Or download a free GUI tool like **DB Browser for SQLite** to click and browse the tables visually.

---

## 7. Golden Rules for Junior Engineers

1. **Always read the error message from bottom to top**: Python gives you the exact file and line number where something went wrong.
2. **Never change production databases without a backup**: Always test SQL queries on a local copy first.
3. **Commit often with clear messages**: Future you will be very grateful!
