import pandas as pd

student_data = {
    "Name": ["Hassan", "Ali", "Ahmad", "Umer", "Bilal"],
    "Age": [21, 22, 20, 23, 21],
    "Department": ["CS", "AI", "SE", "CS", "AI"],
    "CGPA": [3.45, 3.80, 3.20, 3.60, 3.90]
}

df = pd.DataFrame(student_data)
print(df)

df["Country"] = ["Pakistan", "Iran", "Iraq", "Pakistan", "Iran"]
print(df)

dict = df.to_dict()
print(dict)
