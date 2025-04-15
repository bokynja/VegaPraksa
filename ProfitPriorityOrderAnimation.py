import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

products = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\products.csv", encoding="ISO-8859-1")
customers = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\customers.csv", encoding="ISO-8859-1")
orderdetails = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\orderdetails.csv", encoding="ISO-8859-1")
orders = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\orders.csv", encoding="ISO-8859-1")

orderdetails["Order_Date"] = pd.to_datetime(orderdetails["Order_Date"])
orderdetails["Week_Number"] = orderdetails["Order_Date"].dt.to_period("W").dt.to_timestamp()

merged = orderdetails.merge(orders, on="Row_ID", how="left")
merged = merged.merge(customers, on="Customer_ID", how="left")
merged = merged.merge(products, on="Product_ID", how="left")

profits_data = merged.groupby(["Week_Number", "Order_Priority"])["Profit"].sum().reset_index()

profits_data["Cumulative_Profit"] = profits_data.groupby("Order_Priority")["Profit"].cumsum()

weeks = profits_data["Week_Number"].sort_values().unique()


sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (15, 7)

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    current_week = weeks[frame]
    subset = profits_data[profits_data["Week_Number"] <= current_week]
    
    latest = subset.groupby("Order_Priority")["Cumulative_Profit"].max().reset_index()    
    top10 = latest.sort_values("Cumulative_Profit", ascending=False).head(10)

    sns.barplot(
        x="Cumulative_Profit",
        y="Order_Priority",
        data=top10,
        palette="mako",
        ax=ax
    )

    ax.set_title(f"Top Order Priorities by Cumulative Profit\nWeek: {current_week.strftime('%Y-%m-%d')}", fontsize=16)
    ax.set_xlabel("Cumulative Profit")
    ax.set_ylabel("Order Priority")

    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f')

anim = FuncAnimation(fig, update, frames=len(weeks), repeat=False, interval=500)

plt.tight_layout()
plt.show()

