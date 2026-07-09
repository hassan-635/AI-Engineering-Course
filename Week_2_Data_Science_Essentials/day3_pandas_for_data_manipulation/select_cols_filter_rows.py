import pandas as pd
df = pd.read_csv("Week_2_Data_Science_Essentials\day3_pandas_for_data_manipulation\iris.csv")

sel_cols = df[["species", "sepal_length"]]
print(sel_cols)

filtered_rows = df[(df["species"] == "setosa") & (df["sepal_length"] > 5.0)]
print(filtered_rows)