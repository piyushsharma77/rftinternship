import pandas as pd
data = {
    "Name" : ["Aman","Riya","Rahul","Sneha","Karan"],
    "Age" : [25,32,28,24,35],
    "Salary" : [60000,45000,70000,52000,40000]
}
df = pd.DataFrame(data)

print("original dataset:\n",df)

filtered_data = df[(df["Salary"] > 50000) & (df["Age"] < 30)]

print("\n filtered data (Salary > 50000 and Age < 30) :\n",filtered_data)

filtered_data.to_csv("filtered_data.csv",index = False)

print("\n failed data saved to 'filtered_data.csv' ")