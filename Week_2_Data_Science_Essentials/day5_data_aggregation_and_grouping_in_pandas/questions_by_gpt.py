# Find the average salary of each department.
# Find the highest salary in each department.
# Find the lowest salary in each department.
# Count employees in each department.
# Find the average experience of each department.
# Use .agg() to show:
# Mean Salary
# Max Salary
# Min Salary
# Employee Count

import pandas as pd

employees = {
    "Name": ["Ali", "Ahmed", "Hassan", "Bilal", "Umer", "Saad", "Usman", "Hamza"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 70000, 60000, 48000, 65000, 72000, 52000],
    "Experience": [2, 1, 5, 4, 2, 6, 5, 3]
}

df = pd.DataFrame(employees)

