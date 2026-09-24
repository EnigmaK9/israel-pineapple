# 🤝 Contribution Guidelines - SWE Intern & Developer Guide

Welcome to the **israel-pineapple** contributor guide! Whether you are a full-time software engineer, a junior developer, or a SWE intern, this document will help you understand our development lifecycle, Git practices, coding standards, and testing procedures.

---

## 🧭 Code of Conduct & Philosophy

- **Ask Questions Early**: No question is silly. If something is unclear in the code, open a discussion or ask your mentor.
- **Write Clear, Readable Code**: Code is read 10 times more often than it is written. Variable names like `good_pieces` are preferred over `gp`.
- **Leave Code Cleaner Than You Found It**: If you see an unhandled error or a missing docstring, improve it.

---

## 🛠️ Local Development Setup

### 1. Fork & Clone
Clone the repository to your local machine:
```bash
git clone https://github.com/EnigmaK9/israel-pineapple.git
cd israel-pineapple
```

### 2. Configure Virtual Environment
Always isolate your dependencies using `venv`:
```bash
# Create environment
python3 -m venv .venv

# Activate environment (Linux/macOS)
source .venv/bin/activate

# Activate environment (Windows PowerShell)
# .venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🌿 Git Branching Strategy

We follow the standard **Feature Branch Workflow**:

1. Never commit directly to `main`.
2. Create a branch from `main` using descriptive naming:
   - Features: `feat/add-mqtt-listener`
   - Bugfixes: `fix/divide-by-zero-scrap`
   - Documentation: `docs/improve-architecture-diagram`
   - Refactor: `refactor/modularize-sqlite-queries`

```bash
git checkout main
git pull origin main
git checkout -b feat/my-new-feature
```

---

## 📜 Commit Message Conventions

We adhere to **Conventional Commits**:

| Type | When to use | Example |
|---|---|---|
| `feat:` | A brand-new user-facing feature or script | `feat: add live audio alert on temperature threshold breach` |
| `fix:` | A bugfix in existing logic | `fix: handle empty SQLite query when line has no records` |
| `docs:` | Documentation changes only | `docs: add troubleshooting steps for Streamlit port conflicts` |
| `style:` | Formatting, whitespace, missing semicolons (no code change) | `style: format Python files according to PEP 8` |
| `refactor:` | Code restructuring without changing behavior | `refactor: extract database connection logic into db_helper.py` |
| `test:` | Adding or modifying tests | `test: add unit test for scrap percentage formula` |

Example commit:
```bash
git add app_dashboard.py
git commit -m "feat: add sound notification when scrap exceeds 5%"
```

---

## 🐍 Python Coding Standards

### PEP 8 Compliance
- Indentation: **4 spaces** (never tabs).
- Maximum line length: **88 - 100 characters**.
- Function & variable names: `snake_case` (e.g., `calculate_scrap_rate`).
- Classes: `PascalCase` (e.g., `ProductionMonitor`).
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_SAFE_TEMPERATURE = 80.0`).

### Safe SQL Queries
**Never** format raw strings into SQL queries:
```python
# ❌ DANGEROUS: Susceptible to SQL Injection
cur.execute(f"SELECT * FROM produccion_scada WHERE id_linea = {user_input}")

# ✅ CORRECT: Parameterized query with tuple placeholders
cur.execute("SELECT * FROM produccion_scada WHERE id_linea = ?", (user_input,))
```

### Type Annotations
Whenever possible, add type hints to new helper functions:
```python
def calculate_scrap_percentage(good_units: int, defective_units: int) -> float:
    total = good_units + defective_units
    if total == 0:
        return 0.0
    return round((defective_units / total) * 100.0, 2)
```

---

## 🧪 Testing Your Changes Locally

Before opening a Pull Request, ensure that every pipeline component runs without crashing:

```bash
# 1. Reset and reseed the database
python db_setup.py

# 2. Verify static reporting
python dashboard_peluches.py
# Check that 'dashboard_peluches.png' is updated and valid

# 3. Verify CSV generator
python generar_csv.py
# Check that 'scada_peluches.csv' is generated

# 4. Run the Streamlit interactive dashboard
streamlit run app_dashboard.py
# Navigate through all 3 lines in the dropdown and click the 'Simulate SCADA pulse' button
```

---

## 🚀 Submitting a Pull Request (PR)

1. Push your branch to GitHub:
   ```bash
   git push origin feat/my-new-feature
   ```
2. Open a Pull Request against `main`.
3. Provide a clear description:
   - **What does this PR do?**
   - **How did you test it?**
   - **Screenshots** (if modifying the Streamlit UI or Matplotlib charts).
4. Request a review from the repository maintainer.
