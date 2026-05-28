import pandas as pd
import matplotlib.pyplot as plt


data = {
    "DATE": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05",
        "2024-01-06",
        "2024-01-07"
    ],

    "STOCK_PRICE": [
        100,
        105,
        102,
        110,
        115,
        108,
        120
    ]
}

df = pd.DataFrame(data)


df["DATE"] = pd.to_datetime(df["DATE"])

print("Stock Dataset:\n")
print(df)



df["MOVING_AVG"] = df["STOCK_PRICE"].rolling(
    window=3
).mean()



highest_price = df["STOCK_PRICE"].max()
lowest_price = df["STOCK_PRICE"].min()

highest_day = df.loc[
    df["STOCK_PRICE"].idxmax(),
    "DATE"
]

lowest_day = df.loc[
    df["STOCK_PRICE"].idxmin(),
    "DATE"
]


volatility = df["STOCK_PRICE"].std()



plt.figure(figsize=(10, 5))


plt.plot(
    df["DATE"],
    df["STOCK_PRICE"],
    marker='o',
    label="Stock Price"
)

plt.plot(
    df["DATE"],
    df["MOVING_AVG"],
    linestyle='--',
    label="3-Day Moving Average"
)


plt.title("Stock Price Trend Analysis")
plt.xlabel("Date")
plt.ylabel("Price")


plt.legend()


plt.grid(True)


plt.show()


print("\n------ ANALYSIS ------")

print("\nHighest Price:", highest_price)
print("Highest Price Day:", highest_day.date())

print("\nLowest Price:", lowest_price)
print("Lowest Price Day:", lowest_day.date())

print("\nVolatility (Standard Deviation):")
print(round(volatility, 2))

print("\nDataset with Moving Average:\n")
print(df)