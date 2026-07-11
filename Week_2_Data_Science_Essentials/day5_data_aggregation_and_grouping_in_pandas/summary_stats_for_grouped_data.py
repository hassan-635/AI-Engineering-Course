import pandas as pd

import pandas as pd

employees = {
    "Name": ["Ali", "Ahmed", "Hassan", "Bilal", "Umer", "Saad", "Usman", "Hamza"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 70000, 60000, 48000, 65000, 72000, 52000],
    "Experience": [2, 1, 5, 4, 2, 6, 5, 3]
}

df = pd.DataFrame(employees)
print("Original Data : ")
print(df.to_string(index=False))

grouped_data = df.groupby("Department")["Salary"].mean()
print("Mean Of Salaries in Grouped Data : ")
print(grouped_data)

