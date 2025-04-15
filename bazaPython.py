import pyodbc
import pandas as pd



orders_merged = pd.read_csv(r"C:\Users\bojana.boskovic\Downloads\orders_merged_with_status.csv")
users = pd.read_csv(r"C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\final\users.csv")

# konekcija sa MSSQL serverom preko Windows Auth


conn = pyodbc.connect(
    r'DRIVER={SQL Server};SERVER=DELTA-PC-147;DATABASE=NewDb;Trusted_Connection=yes;'
)
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE Users (
        User_ID INT PRIMARY KEY,
        Region NVARCHAR(255),
        Manager NVARCHAR(255)
    )
""")

conn.commit()
for index, row in users.iterrows():
    cursor.execute("""
        INSERT INTO Users (User_ID, Region, Manager) VALUES (?, ?, ?)
    """, row['User ID'], row['Region'], row['Manager'])

conn.commit()
