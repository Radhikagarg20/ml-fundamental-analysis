
# 📊 FinIntel AI  
### Machine Learning Generated Fundamental Analysis Platform

---

## 🌐 Live Production Links

🔹 **Frontend (Investor Dashboard)**  
https://finintel-ai.netlify.app/

🔹 **Backend API (ML Engine)**  
https://ml-fundamental-analysis.onrender.com/

---

# 🚀 Project Overview

**FinIntel AI** is a full-stack, production-deployed financial intelligence platform that evaluates stock market listed companies using machine learning-based scoring logic.

The system:

- Fetches company financial data
- Builds financial performance metrics
- Calculates ML-based financial score
- Classifies companies into risk categories
- Generates strengths & weaknesses
- Displays investor-grade dashboard UI

---

# 🧠 Problem Statement

Retail investors often:

- ❌ Struggle to interpret financial statements
- ❌ Cannot quickly evaluate company fundamentals
- ❌ Lack structured financial scoring tools
- ❌ Depend on scattered financial data sources

There is a need for:

> A simplified AI-powered system that converts raw financial data into actionable investment insights.

---

# 💡 Solution

FinIntel AI solves this by:

1. Fetching company financial data via API
2. Extracting meaningful financial metrics
3. Applying ML-based scoring logic
4. Generating automated insights
5. Classifying companies as:
   - 🟢 Strong
   - 🟡 Stable
   - 🔴 Risky
6. Displaying results in a production-grade dashboard

---

# 🏗 System Architecture


            ┌───────────────────────┐
            │      Frontend         │
            │   (Netlify - Static)  │
            └──────────┬────────────┘
                       │
                       │ HTTPS API Call
                       ▼
            ┌───────────────────────┐
            │      Backend API      │
            │   (Render - Flask)    │
            └──────────┬────────────┘
                       │
                       ▼
            ┌───────────────────────┐
            │   Financial Metrics   │
            │     Builder Layer     │
            └──────────┬────────────┘
                       ▼
            ┌───────────────────────┐
            │   ML Scoring Engine   │
            └──────────┬────────────┘
                       ▼
            ┌───────────────────────┐
            │  Insight Generator    │
            └───────────────────────┘

---

# 🔄 Application Flow


User enters Company (e.g. TCS)
↓
Frontend sends request:
GET /analyze?id=TCS
↓
Backend fetches raw financial data
↓
Metrics Builder processes data
↓
ML Scoring Engine calculates score
↓
Insight Generator creates pros/cons
↓
JSON response returned
↓
Frontend dashboard renders:
• Score
• Category
• Metrics
• Chart
• Pros & Cons


---

# 📁 Project Folder Structure


ml_fundamental_analysis/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── src/
│ │ ├── api/
│ │ │ └── fetch_data.py
│ │ ├── processing/
│ │ │ └── metrics_builder.py
│ │ ├── ml_engine/
│ │ │ ├── scoring.py
│ │ │ └── insight_generator.py
│
├── frontend/
│ ├── index.html
│ ├── analyze.html
│ ├── assets/
│ │ ├── css/style.css
│ │ └── js/
│ │ ├── api.js
│ │ ├── main.js
│ │ ├── charts.js
│ │ └── animations.js
│
├── render.yaml
├── README.md
└── .gitignore


---

# ⚙ Tech Stack

## 🔹 Backend
- Python
- Flask
- Flask-CORS
- Custom ML Scoring Logic
- Financial Metrics Engine
- Render Deployment

## 🔹 Frontend
- HTML5
- Tailwind CSS
- JavaScript (Vanilla)
- Chart.js
- Netlify Deployment

---

# 🔬 Core Functionalities

### 1️⃣ Financial Metrics Builder

Extracted metrics include:

- ROCE
- Sales Growth
- Profit Growth
- Debt to Equity Ratio
- Dividend Payout

---

### 2️⃣ ML Financial Scoring Engine

Custom weighted scoring algorithm:


Classification Logic:

- **Strong** → Score > 30
- **Stable** → Score > 15
- **Risky** → Score ≤ 15

---

### 3️⃣ Insight Generator

Automatically generates:

- ✔ Pros (Strengths)
- ✖ Cons (Risks)

---

### 4️⃣ Investor Dashboard Features

- Real-time API data rendering
- Dynamic category badge
- Financial metric cards
- Interactive chart visualization
- Responsive design
- Production-ready UI

---

# 🖥 Running Locally

## 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

```
Backend runs at:
http://127.0.0.1:5000
------


## 🔹 Frontend Setup

```bash
cd frontend
index.html
```

Frontend runs at (Live Server example):
http://127.0.0.1:5500
------


# 🌍 Production Deployment

## 🔹 Backend

**Hosted on:** Render  

- GitHub repository connected  
- Automatic deployment enabled  
- Public REST API endpoint exposed  

**Live API:**  
https://ml-fundamental-analysis.onrender.com/

---

## 🔹 Frontend

**Hosted on:** Netlify  

- Static site deployment  
- GitHub repository connected  
- Auto-redeploy on every push  

**Live Dashboard:**  
https://finintel-ai.netlify.app/

---

# 📈 Scalability Roadmap

Future improvements planned:

- PostgreSQL database integration  
- User authentication system  
- Portfolio tracking module  
- Real-time market API integration  
- Cloud caching layer (Redis)  
- Advanced ML model enhancement  
- AI-generated financial reports  
- Multi-company comparison engine  

---

# 🏆 Achievements

- ✔ Built a complete full-stack ML financial platform  
- ✔ Designed investor-grade responsive UI  
- ✔ Implemented custom financial scoring engine  
- ✔ Successfully deployed backend & frontend in production  
- ✔ Resolved CORS and cross-origin deployment challenges  
- ✔ Structured scalable modular architecture  

---

# 📊 Result

FinIntel AI transforms complex financial data into:

> A simplified, AI-powered financial intelligence system ready for production-level scaling.
