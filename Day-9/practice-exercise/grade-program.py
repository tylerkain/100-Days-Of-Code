grades = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62, }

student_grades = {}

for student in grades:
    score = grades[student]
    if score > 90:
        student_grades[student] = ["Outstanding", score]
    elif score > 80:
        student_grades[student] = ["Exceeds Expectation", score]
    elif score > 70:
        student_grades[student] = ["Acceptable", score]
    else:
        student_grades[student] = ["Fail", score]

print(student_grades)
