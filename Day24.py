import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Read Weather Data
# -----------------------------------

df = pd.read_csv("weather_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\n===== WEATHER DATA =====")
print(df)

# -----------------------------------
# 2. Average Temperature by City
# -----------------------------------

avg_temp = df.groupby("City")["Temperature"].mean().sort_values(ascending=False)

print("\n===== AVERAGE TEMPERATURE BY CITY =====")
print(avg_temp)

# -----------------------------------
# 3. Hottest and Coldest City
# -----------------------------------

hottest_city = avg_temp.idxmax()
hottest_temp = avg_temp.max()

coldest_city = avg_temp.idxmin()
coldest_temp = avg_temp.min()

print("\n===== HOTTEST CITY =====")
print(f"{hottest_city} : {hottest_temp:.2f} °C")

print("\n===== COLDEST CITY =====")
print(f"{coldest_city} : {coldest_temp:.2f} °C")

# -----------------------------------
# 4. Rainy and Sunny Days
# -----------------------------------

rainy_days = (df["Weather"].str.lower() == "rainy").sum()
sunny_days = (df["Weather"].str.lower() == "sunny").sum()

print("\n===== WEATHER SUMMARY =====")
print("Rainy Days :", rainy_days)
print("Sunny Days :", sunny_days)

# -----------------------------------
# 5. Temperature Trend
# -----------------------------------

daily_temp = df.groupby("Date")["Temperature"].mean()

plt.figure(figsize=(10, 5))
plt.plot(
    daily_temp.index,
    daily_temp.values,
    marker="o"
)

plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_trend.png")
plt.show()

# -----------------------------------
# 6. Weather Distribution
# -----------------------------------

weather_count = df["Weather"].value_counts()

plt.figure(figsize=(7, 5))
weather_count.plot(kind="bar")

plt.title("Weather Distribution")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Days")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("weather_distribution.png")
plt.show()

# -----------------------------------
# 7. Average Temperature Per City
# -----------------------------------

plt.figure(figsize=(8, 5))
avg_temp.plot(kind="bar")

plt.title("Average Temperature per City")
plt.xlabel("City")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_temperature_city.png")
plt.show()

# -----------------------------------
# 8. Moving Average Prediction
# -----------------------------------

overall_daily_temp = df.groupby("Date")["Temperature"].mean()

window = 3

if len(overall_daily_temp) >= window:
    predicted_temp = overall_daily_temp.rolling(window).mean().iloc[-1]

    print("\n===== TOMORROW'S TEMPERATURE PREDICTION =====")
    print(f"Predicted Temperature: {predicted_temp:.2f} °C")
else:
    predicted_temp = None
    print("\nNot enough data for moving average prediction.")

# -----------------------------------
# 9. Create Final Report
# -----------------------------------

report = pd.DataFrame({
    "City": avg_temp.index,
    "Average Temperature": avg_temp.values
})

report["Hottest City"] = hottest_city
report["Hottest Temperature"] = hottest_temp
report["Coldest City"] = coldest_city
report["Coldest Temperature"] = coldest_temp
report["Rainy Days"] = rainy_days
report["Sunny Days"] = sunny_days

if predicted_temp is not None:
    report["Predicted Tomorrow Temperature"] = predicted_temp

# Export report
report.to_csv("weather_final_report.csv", index=False)

print("\n===== REPORT EXPORTED =====")
print("weather_final_report.csv created successfully!")