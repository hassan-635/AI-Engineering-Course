import pandas as pd

students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Hassan", "Ali", "Ahmad", "Bilal", "Umer"]
}

marks = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Math": [90, 75, 80, 65, 95],
    "Physics": [88, 70, 82, 60, 98]
}

attendance = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Attendance": [95, 80, 90, 70, 98]
}

df1 = pd.DataFrame(students)
df2 = pd.DataFrame(marks)
df3 = pd.DataFrame(attendance)

df4 = pd.merge(df1, df2, on="Student_ID", how="outer")
df = pd.merge(df4, df3, on="Student_ID", how="outer")
print(df.to_string(index=False))

print(df.corr(numeric_only=True))