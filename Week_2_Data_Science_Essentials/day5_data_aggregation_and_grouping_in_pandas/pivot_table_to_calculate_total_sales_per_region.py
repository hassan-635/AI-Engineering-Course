import pandas as pd

sales_data = {
    "Order_ID": [101,102,103,104,105,106,107,108,109,110,111,112],
    "Region": [
        "North", "South", "East", "West",
        "North", "South", "East", "West",
        "North", "South", "East", "West"
    ],
    "Year": [
        2023, 2023, 2023, 2023,
        2024, 2024, 2024, 2024,
        2025, 2025, 2025, 2025
    ],
    "Product": [
        "Laptop", "Mobile", "Tablet", "Laptop",
        "Mobile", "Laptop", "Tablet", "Mobile",
        "Laptop", "Tablet", "Mobile", "Laptop"
    ],
    "Quantity": [
        2, 5, 3, 1,
        4, 2, 6, 3,
        5, 2, 4, 3
    ],
    "Price": [
        120000, 50000, 70000, 120000,
        50000, 120000, 70000, 50000,
        120000, 70000, 50000, 120000
    ]
}

df = pd.DataFrame(sales_data)

# Create Total Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

print(df)

pivot = pd.pivot_table(
    data=df,
    values="Total_Sales",
    index="Region",
    columns="Year",
    aggfunc="sum",
    margins=True,
    margins_name="Grand Total"
)

print("________________________________________________")
print(pivot)