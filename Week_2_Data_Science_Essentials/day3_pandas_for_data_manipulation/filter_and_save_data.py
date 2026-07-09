import pandas as pd

df = pd.read_excel("Week_2_Data_Science_Essentials/day3_pandas_for_data_manipulation/data.xlsx")
print("Original Data : ")
print(df)

filtered_data = df[df["CGPA"] > 3.5]
print("Filtered Data : ")
print(filtered_data)

filtered_data.to_csv("Week_2_Data_Science_Essentials/day3_pandas_for_data_manipulation/filtered_data.csv")