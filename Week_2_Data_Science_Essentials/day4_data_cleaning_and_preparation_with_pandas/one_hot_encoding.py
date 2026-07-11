import pandas as pd
student_data = {
    "Name": [
        "Hassan", "Ali", "Muneeb", "Bilal", "Umer",
        "Ahsan", "Uzair", "Hamza", "Saad", "Zain"
    ],
    "Department": [
        "AI", "CS", "SE", "AI", "CS",
        "IT", "SE", "AI", "IT", "CS"
    ],
    "Gender": [
        "Male", "Male", "Male", "Male", "Male",
        "Female", "Female", "Male", "Male", "Male"
    ],
    "City": [
        "Rawalpindi", "Lahore", "Islamabad", "Karachi", "Peshawar",
        "Rawalpindi", "Lahore", "Karachi", "Islamabad", "Peshawar"
    ],
    "CGPA": [
        3.45, 3.80, 3.20, 3.60, 3.90,
        3.75, 3.50, 3.10, 3.65, 3.85
    ]
}
df = pd.DataFrame(student_data)

df = pd.get_dummies(df, columns=["Department"], dtype=int)

print(df.to_string(index=False))
print(df.corr(numeric_only=True))