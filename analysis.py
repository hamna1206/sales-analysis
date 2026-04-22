import pandas as pd

# 1. load csv file and read sales data using pandas
df = pd.read_csv("sales.csv")

# 2. calculate total sales for each product
df["TotalSales"] = df["Quantity"] * df["Price"]

# 3. group by product and calculate total sales for each of product
category_sales = df.groupby("Category")["TotalSales"].sum()
top_product = df.groupby("Product")["TotalSales"].sum().idxmax()
region_sales = df.groupby("Region")["TotalSales"].sum()

df_filtered = df[df["TotalSales"] > 200]

print(category_sales)
print(top_product)
print(region_sales)
print(df_filtered)
print(df_filtered.columns)
print(df.head())
