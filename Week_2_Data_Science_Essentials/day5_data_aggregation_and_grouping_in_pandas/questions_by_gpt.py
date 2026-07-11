import pandas as pd

employees = {
    "Name": ["Ali", "Ahmed", "Hassan", "Bilal", "Umer", "Saad", "Usman", "Hamza"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 70000, 60000, 48000, 65000, 72000, 52000],
    "Experience": [2, 1, 5, 4, 2, 6, 5, 3]
}

df = pd.DataFrame(employees)
print(df.to_string(index=False))

# Find the average salary of each department.

avg_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary of Every Department : ")
print(avg_salary)

# Find the highest salary in each department.
highest_salary = df.groupby("Department")["Salary"].max()
print("Highest Salary of Every Department : ")
print(highest_salary)

# Find the lowest salary in each department.
lowest_salary = df.groupby("Department")["Salary"].min()
print("Lowest Salary of Every Department : ")
print(lowest_salary)

# Count employees in each department.
emp = df.groupby("Department")["Name"].count()
print("Total Employees in each department : ")
print(emp)

# Find the average experience of each department.
exp = df.groupby("Department")["Experience"].mean()
print("Average Experience of each Department : ")
print(exp)

# Use .agg() to show:
# Mean Salary
# Max Salary
# Min Salary
# Employee Count

stats = df.groupby("Department").agg({
    "Salary" : ["mean", "max", "min"],
    "Name" : ["count"]
})

print("Statistical Summary : ")
print(stats)