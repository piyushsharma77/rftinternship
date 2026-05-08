
file = open("students.csv", "r")

lines = file.readlines()


headers = lines[0].strip().split(",")

data = []


for line in lines[1:]:
    values = line.strip().split(",")

    student = {
        "NAME": values[0],
        "AGE": int(values[1]),
        "MARKS": int(values[2])
    }

    data.append(student)

file.close()


print(data)


total = 0

for student in data:
    total += student["MARKS"]

average = total / len(data)

print("Average Marks:", average)