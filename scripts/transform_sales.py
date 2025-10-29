import pandas as pd
import os

# pth
raw_path = 'data/raw'
processed_path = 'data/processed'

# Створити папку processed, якщо її нема
os.makedirs(processed_path, exist_ok=True)

# read
sales = pd.read_csv(f'{raw_path}/sales.csv')
customers = pd.read_csv(f'{raw_path}/customers.csv')
products = pd.read_csv(f'{raw_path}/products.csv')

# clrr
sales.columns = sales.columns.str.strip()
customers.columns = customers.columns.str.strip()
products.columns = products.columns.str.strip()

sales = sales.drop(columns=['unit_price', 'total_price'], errors='ignore')

# ---------- Об'єднання таблиць ----------
df = sales.merge(customers, on='customer_id', how='left') \
          .merge(products, on='product_id', how='left')

# Видаляємо дублікати
df = df.drop_duplicates()

# Заповнення пропусків
df = df.fillna({'first_name': 'Unknown', 'last_name': 'Unknown', 'product_name': 'Unknown'})

# ---------- Додавання total_price ----------
df['total_price'] = df['quantity'] * df['unit_price']

# ---------- Збереження обробленого CSV ----------
df.to_csv(f'{processed_path}/sales_clean.csv', index=False)

print("✅ ETL is done. file firection: 'data/processed/sales_clean.csv'")
