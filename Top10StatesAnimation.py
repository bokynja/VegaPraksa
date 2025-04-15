import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

products = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\products.csv", encoding="ISO-8859-1")
customers = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\customers.csv", encoding="ISO-8859-1")
orderdetails = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\orderdetails.csv", encoding="ISO-8859-1")
orders = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\orders.csv", encoding="ISO-8859-1")

orderdetails["Order_Date"] = pd.to_datetime(orderdetails["Order_Date"])
orderdetails["Order_Date"] = orderdetails["Order_Date"].dt.to_period("M").dt.to_timestamp()

merged = orderdetails.merge(orders, on="Row_ID", how="left")
merged = merged.merge(customers, on="Customer_ID", how="left")
merged = merged.merge(products, on="Product_ID", how="left")

sales_data = merged.groupby(["Order_Date", "State_or_Province"])["Sales"].sum().reset_index()

sales_data["Cumulative_Sales"] = sales_data.groupby("State_or_Province")["Sales"].cumsum()

dates = sales_data["Order_Date"].sort_values().unique()

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    current_date = dates[frame]
    subset = sales_data[sales_data["Order_Date"] <= current_date]
    
    latest = subset[subset["Order_Date"] == current_date]
    top10 = latest.sort_values("Cumulative_Sales", ascending=False).head(10)
    
    sns.barplot(
        x="Cumulative_Sales", 
        y="State_or_Province", 
        data=top10, 
        palette="viridis", 
        ax=ax
    )
    
    ax.set_title(f"Top 10 States by Cumulative Sales\nDate: {current_date.strftime('%Y-%m')}", fontsize=16)
    ax.set_xlabel("Cumulative Sales")
    ax.set_ylabel("State or Province")

anim = FuncAnimation(fig, update, frames=len(dates), repeat=False, interval=700)

plt.tight_layout()
plt.show()