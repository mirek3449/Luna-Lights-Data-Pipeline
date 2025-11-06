import pandas as pd
import os

# path
raw_path = 'data/raw'
processed_path = 'data/processed'

# Creates folder
os.makedirs(processed_path, exist_ok=True)

# Read
sales = pd.read_csv(f'{raw_path}/sales.csv')
customers = pd.read_csv(f'{raw_path}/customers.csv')
products = pd.read_csv(f'{raw_path}/products.csv')

# Clears
sales.columns = sales.columns.str.strip()
customers.columns = customers.columns.str.strip()
products.columns = products.columns.str.strip()

sales = sales.drop(columns=['unit_price', 'total_price'], errors='ignore')

# Merge tables
df = sales.merge(customers, on='customer_id', how='left') \
          .merge(products, on='product_id', how='left')

# Deletes duplicates
df = df.drop_duplicates()

# Filling empty spaces
df = df.fillna({'first_name': 'Unknown', 'last_name': 'Unknown', 'product_name': 'Unknown'})

# Adds total price
df['total_price'] = df['quantity'] * df['unit_price']

# Saves all
df.to_csv(f'{processed_path}/sales_clean.csv', index=False)

print("✅ ETL is done. file firection: 'data/processed/sales_clean.csv'")
