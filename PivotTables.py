import pandas as pd

products = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\products.csv", encoding="ISO-8859-1")
customers = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\customers.csv", encoding="ISO-8859-1")
orderdetails = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\orderdetails.csv", encoding="ISO-8859-1")
orders = pd.read_csv(r"C:\Users\bojana.boskovic\Desktop\orders.csv", encoding="ISO-8859-1")

orderdetails["Order_Date"] = pd.to_datetime(orderdetails["Order_Date"])
orderdetails["Ship_Date"] = pd.to_datetime(orderdetails["Ship_Date"])

orderdetails["Days_Between_Order_And_Ship"] = (
    orderdetails["Ship_Date"] - orderdetails["Order_Date"]
).dt.days

merged = orderdetails.merge(orders, on="Row_ID", how="left")
merged = merged.merge(customers, on="Customer_ID", how="left")
merged = merged.merge(products, on="Product_ID", how="left")

agg_dict = {
    "Discount": "mean",
    "Shipping_Cost": "mean",
    "Days_Between_Order_And_Ship": "mean",
    "Profit": "sum",
    "Sales": "sum"
}

def create_pivot(df, index_col, filename):
    pivot = df.pivot_table(index=index_col, values=agg_dict.keys(), aggfunc=agg_dict)
    pivot.columns = [
        "Average Discount",
        "Average Shipping Cost",
        "Average Days Between Order and Ship Date",
        "Total Profit",
        "Total Sales"
    ]
    pivot = pivot.round(2)
    pivot.to_csv(f"{filename}.csv")

create_pivot(merged, "Order_Priority", "pivot_order_priority")
create_pivot(merged, "Customer_Segment", "pivot_customer_segment")
create_pivot(merged, "Product_Category", "pivot_product_category")
create_pivot(merged, "Product_Sub_Category", "pivot_product_sub_category")
create_pivot(merged, "State_or_Province", "pivot_state_or_province")
