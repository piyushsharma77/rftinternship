import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = {
    "DATE": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05",
        "2024-01-06"
    ],

    "PRODUCT": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Laptop",
        "Mouse",
        "Keyboard"
    ],

    "REGION": [
        "North",
        "South",
        "East",
        "West",
        "North",
        "East"
    ],

    "SALES": [
        50000,
        3000,
        7000,
        55000,
        None,
        9000
    ]
}


df = pd.DataFrame(data)



print("Original Dataset:\n")
print(df)


df["SALES"] = df["SALES"].fillna(
    df["SALES"].mean()
)


df["DATE"] = pd.to_datetime(df["DATE"])

print("\nCleaned Dataset:\n")
print(df)

product_sales = df.groupby(
    "PRODUCT"
)["SALES"].sum()


region_sales = df.groupby(
    "REGION"
)["SALES"].sum()


daily_sales = df.groupby(
    "DATE"
)["SALES"].sum()


best_product = product_sales.idxmax()


best_region = region_sales.idxmax()



plt.figure(figsize=(15, 5))



plt.subplot(1, 3, 1)

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker='o'
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)


plt.subplot(1, 3, 2)

product_sales.plot(kind='bar')

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Revenue")


plt.subplot(1, 3, 3)

plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct='%1.1f%%'
)

plt.title("Region-wise Contribution")

plt.tight_layout()


plt.show()



print("\n------ KEY INSIGHTS ------")

print("\n1. Best Selling Product:")
print(best_product)

print("\n2. Best Performing Region:")
print(best_region)

print("\n3. Product-wise Revenue:")
print(product_sales)

print("\n4. Region-wise Revenue:")
print(region_sales)

print("\n5. Average Sales:")
print(round(df["SALES"].mean(), 2))