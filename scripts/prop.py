import pandas as pd

products = pd.read_csv('data/raw/products.csv')
sales = pd.read_csv('data/raw/sales.csv')

print("Products columns:", products.columns.tolist())
print("Sales columns:", sales.columns.tolist())
