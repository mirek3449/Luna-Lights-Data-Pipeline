# 🌙 Luna Lights Data Pipeline
A complete end-to-end data engineering project showing the flow from raw CSVs to Power BI dashboards using Azure SQL Database.

## 🚀 Overview
ETL process built for a fictional e-commerce brand *Luna Lights*.
Data is transformed with Python, loaded to Azure SQL, and visualized in Power BI.

## 🧩 Tech Stack
- **Python (pandas, pyodbc)** — ETL pipeline
- **Azure SQL Database** — cloud warehouse
- **Power BI** — dashboards
- **GitHub** — version control

## ⚙️ Run Locally
\`\`\`bash
git clone git@github.com:mirek3449/Luna-Lights-Data-Pipeline.git
cd Luna-Lights-Data-Pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/transform_sales.py
python scripts/upload_to_azure.py
\`\`\`

## 📊 Power BI Dashboard
Includes:
- Total revenue & average order value
- Monthly & daily trends
- Top 10 products
- Customer segmentation
- Clean Luna Lights theme (#FFF9F2, #F6E6C3, #B59E7B)

## 🧱 Architecture
Raw CSVs → Python ETL → Azure SQL DB → Power BI

## 🧾 Author
**Myroslav Soima (Mirek)**
Data Engineer | BI Developer
GitHub: https://github.com/mirek3449
