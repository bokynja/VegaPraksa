import pandas as pd

# Učitavanje fajla
orders_merged = pd.read_csv(r"C:\Users\bojana.boskovic\Downloads\orders_merged_with_status.csv")
users = pd.read_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\pivot tabele\csv\Users.csv")
users['User ID'] = range(1, len(users) + 1)

print(orders_merged.columns)

# ---------- CATEGORIES ----------
categories = orders_merged[['Product Category']].drop_duplicates().reset_index(drop=True)
categories.insert(0, 'Category ID', range(1, len(categories) + 1))

# ---------- SUBCATEGORIES ----------
subcategories = orders_merged[['Product Sub-Category', 'Product Category']].drop_duplicates().reset_index(drop=True)
subcategories.insert(0, 'Sub-Category ID', range(1, len(subcategories) + 1))

# ---------- PRODUCTS ----------
products = orders_merged[['Product Name', 'Product Sub-Category', 'Product Category', 'Product Base Margin']].drop_duplicates().reset_index(drop=True)
products.insert(0, 'Product ID', range(1, len(products) + 1))

# ---------- CUSTOMERS ----------
customers = orders_merged[['Customer ID', 'Customer Name', 'Customer Segment', 'Country',
                           'State or Province', 'City', 'Postal Code', 'Region']].drop_duplicates().reset_index(drop=True)

# ---------- Čuvanje CSV fajlova ----------
users.to_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\final\users.csv", index=False)
categories.to_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\final\categories.csv", index=False)
subcategories.to_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\final\subcategories.csv", index=False)
products.to_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\final\products.csv", index=False)
customers.to_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\final\customers.csv", index=False)

print("✅ Gotove tabele sa svim kolonama: users, categories, subcategories, products, customers.")
