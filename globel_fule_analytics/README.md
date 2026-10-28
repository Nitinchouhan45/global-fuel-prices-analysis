# Global Fuel Prices and Taxation Trends: A Comprehensive Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask%203.x-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Tableau](https://img.shields.io/badge/Visualization-Tableau%20Public-E97627?logo=tableau)](https://public.tableau.com/)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-purple?logo=bootstrap)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-Academic%20Evaluation-teal)]()

An interactive, responsive full-stack web application built with **Python Flask** and **Tableau Public** to analyze global retail fuel prices, international crude oil price transmission elasticity, government subsidy levels, and cross-national taxation structures.

Developed for Data Analytics portfolio evaluation and submission to **SkillWallet**.

---

## 📌 Project Overview

Energy prices are a critical barometer of global macroeconomic stability and household cost-of-living. While crude oil is priced in standardized international markets (e.g., Brent Crude), the prices that consumers pay at retail fuel stations for **Petrol**, **Diesel**, and **LPG** vary vastly across countries.

This web application integrates **Tableau Public Interactive Dashboards** and **Tableau Stories** into a modern, responsive web portal powered by Flask. It allows researchers, analysts, and recruiters to explore:
1. **Price Transmission Elasticity:** How fluctuations in international Brent Crude USD transmit to domestic retail pump prices.
2. **Fiscal Policy Disparities:** The divergence between sovereign jurisdictions that tax fuel heavily (excise/VAT) versus those that subsidize domestic consumption.
3. **Socioeconomic Vulnerability:** Fuel price burdens mapped across World Bank income classifications (`High`, `Upper-Middle`, `Lower-Middle`, `Low`).
4. **Cross-Fuel Spreads:** Pricing parity and gaps between Petrol, Diesel, and LPG.

---

## 📂 Project Folder Structure

```text
globel_fule_analytics/
│
├── app.py                     # Flask application entry point and URL configuration
├── requirements.txt           # Python dependency requirements
├── README.md                  # Comprehensive documentation and setup guide
├── .gitignore                 # Git ignore rules for Python and local environments
│
├── templates/                 # Jinja2 HTML templates
│   ├── base.html              # Base layout with navbar, footer, and CDN links
│   ├── index.html             # Home page with hero, summary cards, and objectives
│   ├── dashboard.html         # Interactive Tableau Public Dashboard embedding
│   ├── story.html             # Guided Tableau Story narrative & findings placeholders
│   ├── about.html             # Data dictionary (10 fields), methodology, & limitations
│   ├── contact.html           # Contact form, analyst portfolio card, & FAQ
│   └── 404.html               # Custom branded 404 error page
│
└── static/                    # Static assets
    ├── css/
    │   └── style.css          # Custom responsive CSS theme (Navy, Teal, Orange)
    ├── js/
    │   └── main.js            # Embed handler, fullscreen toggle, fallback script
    └── images/
        └── favicon.svg        # Fuel analytics browser icon
```

---

## 📊 Dataset Schema (10 Standardized Fields)

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| **`Country`** | Categorical | Sovereign nation or territory name. |
| **`Date`** | Temporal | Observation recording period / timestamp. |
| **`Income Level`** | Categorical / Ordinal | World Bank classification (High, Upper-Middle, Lower-Middle, Low). |
| **`Region`** | Categorical | Geographical continent or regional economic bloc. |
| **`Subsidy Level`** | Categorical / Ordinal | Intensity tier of government retail price subsidy (High, Med, Low, None). |
| **`Brent Crude USD`** | Numerical (Continuous) | Benchmark international crude oil spot price (USD per barrel). |
| **`Diesel USD Liter`** | Numerical (Continuous) | Retail automotive diesel pump price (USD per liter). |
| **`LPG USD Liter`** | Numerical (Continuous) | Retail liquefied petroleum gas price (USD per liter equivalent). |
| **`Petrol USD Liter`** | Numerical (Continuous) | Retail motor gasoline / petrol price (USD per liter). |
| **`Tax Percentage`** | Numerical (Percentage) | Total fiscal tax/excise burden as a percentage of retail price. |

---

## 🚀 Quick Start: Running the Project Locally

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13 installed on your machine.
- Git installed.
- Terminal (PowerShell, Command Prompt, or Bash).

### 2. Open Terminal in the Project Directory
```powershell
cd "c:\Users\nitin\Desktop\project file\globel_fule_analytics"
```

### 3. Create and Activate a Virtual Environment (Recommended)
**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(If PowerShell blocks script execution, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Start the Flask Server
```bash
python app.py
```

### 6. View the Application
Open your web browser and navigate to:
```text
http://127.0.0.1:5000
```

---

## 🔗 How to Connect Your Tableau Dashboard & Story

You do **not** need complex code edits to plug in your own Tableau visualizations.

### Step 1: Publish to Tableau Public
1. Open your workbook in Tableau Desktop.
2. Go to **Server** &rarr; **Tableau Public** &rarr; **Save to Tableau Public As...**
3. Once published on your Tableau Public profile, open the dashboard in your browser.
4. Click the **Share** button (at the top-right or bottom-right of the Tableau toolbar).
5. Copy the **Link** (e.g., `https://public.tableau.com/views/YourWorkbook/YourDashboard`).

### Step 2: Configured URLs in `app.py`
The active dashboard URL is connected in `app.py`:
```python
# Active Dashboard & Story URLs:
DEFAULT_TABLEAU_DASHBOARD_URL = os.environ.get(
    'TABLEAU_DASHBOARD_URL',
    'https://public.tableau.com/views/Globelfulepriseandtaxationtrends/GlobalFuelPriceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)

DEFAULT_TABLEAU_STORY_URL = os.environ.get(
    'TABLEAU_STORY_URL',
    'https://public.tableau.com/views/Globelfulepriseandtaxationtrends/GlobalFuelPriceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)
```
Save the file and refresh your browser. The embedded dashboard and story will render immediately with interactive filters, tooltips, and responsive layout.

---

## 🖥️ Application Features & Pages

- **Home Page (`/`)**: High-impact energy analytics hero, project goals, analytical scope, dimension summary cards for Petrol, Diesel, LPG, and Taxation.
- **Interactive Dashboard (`/dashboard`)**: Full-screen capable Tableau Public embed with loading spinner, reload button, direct Tableau link, and responsive fallback notice.
- **Tableau Story Page (`/story`)**: Guided sequential narrative chapters, analytical findings placeholders, and policy recommendations.
- **About Project (`/about`)**: Complete 10-field data dictionary, data cleaning methodology, visualization architecture, and analytical limitations.
- **Contact & Portfolio (`/contact`)**: Portfolio details for recruiters/evaluators, interactive inquiry form with flash notifications, and quick FAQ.
- **Custom 404 (`/404`)**: Error page keeping users inside the app.

---

## 🌐 Deploying to the Cloud for Free (Render / PythonAnywhere)

To share your live web app with evaluators and recruiters on SkillWallet, deploy it on a free hosting platform like **Render.com**:

### Deploying on Render (Free):
1. Push your code to GitHub (see GitHub commands below).
2. Go to [https://render.com](https://render.com) and sign up for a free account.
3. Click **New +** &rarr; **Web Service**.
4. Connect your GitHub repository: `global-fuel-analytics`.
5. Fill in the service settings:
   - **Name:** `global-fuel-analytics`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app.py:app`
   - **Instance Type:** `Free`
6. Click **Deploy Web Service**. Within 2 minutes, Render will provide a live URL (e.g. `https://global-fuel-analytics.onrender.com`).

---

## 🐙 Step-by-Step GitHub Commands

To initialize git and push your code to GitHub:

```bash
# 1. Initialize Git in the project directory
git init

# 2. Stage all files
git add .

# 3. Create your initial commit
git commit -m "Initial commit: Global Fuel Analytics Flask & Tableau Web App"

# 4. Rename default branch to main
git branch -M main

# 5. Link your GitHub remote repository (replace with your repo URL)
git remote add origin https://github.com/<your-username>/global-fuel-analytics.git

# 6. Push code to GitHub
git push -u origin main
```

---

## 💼 Submitting to SkillWallet

When submitting your project to **SkillWallet**:
1. **Project Title:** `Global Fuel Prices and Taxation Trends: A Comprehensive Analysis`
2. **GitHub Repository URL:** `https://github.com/<your-username>/global-fuel-analytics`
3. **Live Deployed URL:** `https://<your-app-name>.onrender.com` (or your chosen host)
4. **Tableau Public Dashboard URL:** `https://public.tableau.com/views/Globelfulepriseandtaxationtrends/GlobalFuelPriceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link`
5. **Key Skills Highlighted:** Tableau Public, Python Flask, Jinja2, Data Visualization, Bootstrap 5, Exploratory Data Analysis (EDA), Git & GitHub.

---

## 🛠️ Common Errors & Quick Troubleshooting

1. **Error: `ModuleNotFoundError: No module named 'flask'`**
   - **Solution:** Activate your virtual environment and run `pip install -r requirements.txt`.
2. **Error: `Address already in use` or Port 5000 is busy**
   - **Solution:** In `app.py`, change `port=5000` to `port=5050` or run: `python app.py` with environment variable `PORT=5050`.
3. **Tableau Dashboard shows a gray box or says 'Refused to display'**
   - **Solution:** Ensure your Tableau viz is set to **Public** on Tableau Public. Make sure the URL ends with `?:showVizHome=no&:embed=true`. Use the "Open on Tableau Public" button if local browser adblockers block third-party cookies.
4. **PowerShell execution policy error on `venv\Scripts\Activate.ps1`**
   - **Solution:** Open PowerShell as Administrator or run:
     `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

---

## 👨‍💻 Author & Acknowledgments

- **Author:** Data Analytics Specialist & Full-Stack Developer
- **Target:** Tableau Data Analytics Portfolio Submission & SkillWallet Evaluation
- **Tools:** Python, Flask, Tableau Public, Bootstrap 5, Git

