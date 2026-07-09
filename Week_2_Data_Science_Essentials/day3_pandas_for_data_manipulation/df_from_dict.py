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

student_data = df.to_dict()
df.to_excel("Week_2_Data_Science_Essentials/day3_pandas_for_data_manipulation/data.xlsx", index=False)
df.to_csv("Week_2_Data_Science_Essentials/day3_pandas_for_data_manipulation/data.csv", index=False)
