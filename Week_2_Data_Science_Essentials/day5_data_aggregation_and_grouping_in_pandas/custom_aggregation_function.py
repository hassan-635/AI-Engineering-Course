import pandas as pd
import numpy as np

employees = {
    "Name": ["Ali", "Ahmed", "Hassan", "Bilal", "Umer", "Saad", "Usman", "Hamza"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 70000, 60000, 48000, 65000, 72000, 52000],
    "Experience": [2, 1, 5, 4, 2, 6, 5, 3]
}

df = pd.DataFrame(employees)
print(df.to_string(index=False))

def variance(series):
    mean = np.mean(series)
    return np.sum((series - mean) ** 2)/(len(series)-1)
    
mean_and_variance = df.groupby("Department").agg(
    {
        "Salary" : ["mean", variance]
    }
)

print(mean_and_variance)