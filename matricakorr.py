import pandas as pd

# 1. Učitavanje već pripremljenog orders_merged CSV
orders = pd.read_csv(r"C:\Users\bojana.boskovic\Downloads\orders_merged_with_status.csv", parse_dates=['Order Date', 'Ship Date'])

# 5. Korelacija (isključujemo određene kolone)
columns_to_exclude = ['Row ID', 'Customer ID', 'Order ID']
corr_df = orders.drop(columns=columns_to_exclude).corr(numeric_only=True)

# Pronalazak top 3 i bottom 3 parova
corr_unstacked = corr_df.where(~(corr_df == 1)).unstack().dropna()
corr_unstacked = corr_unstacked[~corr_unstacked.duplicated()]

top_3 = corr_unstacked.sort_values(ascending=False).head(3)
bottom_3 = corr_unstacked.sort_values().head(3)

print("\nTop 3 korelacije:\n", top_3)
print("\nNajslabije 3 korelacije:\n", bottom_3)

# Export u CSV
corr_summary = pd.concat([top_3, bottom_3]).reset_index()
corr_summary.columns = ['Feature 1', 'Feature 2', 'Correlation']
corr_summary.to_csv('correlation_summary.csv', index=False)

import seaborn as sns
import matplotlib.pyplot as plt

# Vizuelni prikaz matrice korelacije
plt.figure(figsize=(12, 10))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", square=True, linewidths=0.5, cbar_kws={'label': 'Correlation'})
plt.title('Matrica korelacije između numeričkih atributa (bez Row ID, Customer ID, Order ID)')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# Čuvanje kao PNG (opciono)
plt.savefig('correlation_matrix.png')

# Prikaz grafa
plt.show()
