import pandas as pd

sales_data = {
    "Order_ID": [101,102,103,104,105,106,107,108,109,110,111,112],
    "Salesperson": [
        "Ali", "Hassan", "Ali", "Ahmed",
        "Hassan", "Ali", "Bilal", "Ahmed",
        "Bilal", "Hassan", "Ali", "Ahmed"
    ],
    "City": [
        "Lahore", "Karachi", "Lahore", "Islamabad",
        "Karachi", "Lahore", "Islamabad", "Lahore",
        "Karachi", "Islamabad", "Karachi", "Lahore"
    ],
    "Product": [
        "Laptop", "Mobile", "Tablet", "Laptop",
        "Laptop", "Mobile", "Tablet", "Mobile",
        "Laptop", "Tablet", "Laptop", "Mobile"
    ],
    "Quantity": [2, 5, 3, 1, 4, 2, 6, 3, 2, 5, 1, 4],
    "Price": [120000, 50000, 70000, 120000, 120000, 50000, 70000, 50000, 120000, 70000, 120000, 50000]
}

df = pd.DataFrame(sales_data)

# Total Sale Amount
df["Total_Sale"] = df["Quantity"] * df["Price"]

print(df)

# group by city

grouped_data_city = df.groupby("City").count()
print(grouped_data_city)