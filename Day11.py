import matplotlib.pyplot as plt


days = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]


max_sale = max(sales)
min_sale = min(sales)

max_day = days[sales.index(max_sale)]
min_day = days[sales.index(min_sale)]


plt.plot(days, sales, marker='o', linewidth=2)


plt.scatter(max_day, max_sale, label=f"Highest: {max_day} ({max_sale})")
plt.scatter(min_day, min_sale, label=f"Lowest: {min_day} ({min_sale})")


plt.title("Sales Trend Analysis")
plt.xlabel("Days")
plt.ylabel("Sales")

# Show values on points
for i in range(len(days)):
    plt.text(days[i], sales[i] + 5, str(sales[i]))

# Legend and grid
plt.legend()
plt.grid(True)

# Display chart
plt.show()