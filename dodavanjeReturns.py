import pandas as pd

# Lista putanja do CSV fajlova
orders_files = [
    r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\pivot tabele\csv\Orders_Central.csv",
    r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\pivot tabele\csv\Orders_East.csv",
    r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\pivot tabele\csv\Orders_South.csv",
    r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\pivot tabele\csv\Orders_West.csv"
]

# Učitaj sve fajlove uz preskakanje loših redova (npr. sa pogrešnim brojem kolona)
dataframes = []
for file in orders_files:
    df = pd.read_csv(file, on_bad_lines='skip', encoding='utf-8', sep='|')  # Možeš probati i sep=';' ako zarezi ne rade
    dataframes.append(df)

# Spajanje svih u jedan DataFrame
orders_merged = pd.concat(dataframes, ignore_index=True)

orders_merged.columns = orders_merged.columns.str.strip()
# 2. Dodaj status iz Returns.csv na osnovu Order ID
returns = pd.read_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\pivot tabele\csv\Returns.csv", sep="|")
returns.columns = returns.columns.str.strip()


orders_merged = orders_merged.merge(returns, how='left', on='Order ID')
orders_merged['Status'] = orders_merged['Status'].fillna('Not Returned')


# (opcionalno) sačuvaj update-ovan orders_merged
orders_merged.to_csv(r"C:\Users\bojana.boskovic\Downloads\orders_merged_with_status.csv", index=False)
print("✅ Dodata Status kolona iz Returns.")


