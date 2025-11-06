import pandas as pd
import pyodbc

# CSV 
df = pd.read_csv("data/processed/sales_clean.csv")
df = df[['sale_id', 'date', 'customer_id', 'product_id', 'quantity', 'unit_price', 'total_price']]

# Connection data
server = 'lunalights-sql-server.database.windows.net' 
database = 'lunalights-db'
username = 'adminmirek'  
password = 'VBHJCBR@12'
driver = '{ODBC Driver 18 for SQL Server}'

# Connection
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Creates table
cursor.execute("""
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='sales' AND xtype='U')
CREATE TABLE sales (
    sale_id INT,
    date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    unit_price FLOAT,
    total_price FLOAT
)
""")
conn.commit()

# Upploads data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (sale_id, date, customer_id, product_id, quantity, unit_price, total_price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, tuple(row))
conn.commit()

cursor.close()
conn.close()
print("✅ Data is uploaded in Azure SQL!")
