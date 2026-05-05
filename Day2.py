marks = [78, 85, 90, 67, 85, 92, 78]

def analyzing_scores(marks):
    total_marks = sum(marks)
    total_students = len(marks)
    average = total_marks / total_students
    highest = max(marks)
    lowest = min(marks)
    
    above_average_students = 0
    grades = {"A": 0, "B": 0, "C": 0, "Fail": 0}

    for score in marks:
        if score > average:
            above_average_students += 1
        
        
        if score >= 90:
            grades["A"] += 1
        elif score >= 80:
            grades["B"] += 1
        elif score >= 70:
            grades["C"] += 1
        else:
            grades["Fail"] += 1

    
    print("Average Score:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Above Average Students:", above_average_students)
    print("Grades Distribution:", grades)
analyzing_scores(marks)