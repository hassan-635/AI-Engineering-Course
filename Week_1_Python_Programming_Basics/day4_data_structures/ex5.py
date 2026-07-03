

# program to store student grades in dictionary and calculates average grade

grades = {
    "chemistry": "A",
    "urdu": "C",
    "physics" : "D",
    "islamiat": "A",
    "pak_study": "B"
}

numbers = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60
}

total_marks = 0

for subject in grades:
    grade = grades[subject]
    total_marks+= numbers[grade]

average = total_marks/5
print(average)
    
print(total_marks)