import matplotlib.pyplot as plt

categories = ["FOOD", "TRAVEL", "SHOPPING"]
expenses = [500, 300, 200]

colors = ["gold", "skyblue", "lightgreen"]

plt.figure(figsize=(7, 7))

plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    shadow=True
)

plt.title("Monthly Expense Distribution")

plt.show()