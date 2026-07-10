import numpy as np
import pandas as pd

data = {
    "Name": ["Hassan", "Ali", np.nan, "Uzair", "Ahmed", np.nan],
    "Age" : [22, np.nan, 23, 21, np.nan, 50],
    "Score" : [90, 50, np.nan, np.nan, 10, np.nan]
}

df = pd.DataFrame(data)
print(df)
print("\n__________________________________________________________________")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()
df = df.dropna()
df = df.rename(columns={"Name": "Student_Name", "Score": "Marks"})
print("\n")
print(df)
print("\n__________________________________________________________________")



