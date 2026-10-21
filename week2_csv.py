import pandas as pd

df = pd.read_csv(
    r"C:\Users\rashid\OneDrive\Desktop\Sales. csv"
)

df["Revenue"] = df["Quantity"] * df["Unit_Price"]

print("SALES DATA")
print(df)

print("\n1. Total Revenue:")
print(df["Revenue"].sum())

print("\n2. Total Quantity Sold:")
print(df["Quantity"].sum())

print("\n3. Average Sale Revenue:")
print(df["Revenue"].mean())

print("\n4. Revenue by Product:")
print(df.groupby("Product")["Revenue"].sum())

print("\nHighest Revenue Sale:")
print(df.loc[df["Revenue"].idxmax()])

print("\nLowest Revenue Sale:")
print(df.loc[df["Revenue"].idxmin()])

print("\nSales Summary:")
print(df.describe())

# Create a product-wise sales report

summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum")
)

summary = summary.sort_values(
    by="Total_Revenue", ascending=False
)

print("\nPRODUCT-WISE SALES REPORT")
print(summary)

# Save the report as a CSV file
summary.to_csv("sales_report.csv")

print("\nReport saved successfully!")

import matplotlib.pyplot as plt

product_revenue = df.groupby("Product")["Revenue"].sum()
product_revenue = product_revenue.sort_values(ascending=False)

product_revenue.plot(
    kind="bar",
    title="Total Revenue by Product",
    figsize=(8, 5)
)

plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

print("Chart saved successfully!")
