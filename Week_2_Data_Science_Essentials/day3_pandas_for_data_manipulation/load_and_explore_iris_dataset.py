
import pandas as pd

df = pd.read_csv("Week_2_Data_Science_Essentials\day3_pandas_for_data_manipulation\iris.csv")
print("_________________________________________________________________")
print("First five rows : ")
print(df.head())
print("_________________________________________________________________")
print("Last five rows : ")
print(df.tail())
print("_________________________________________________________________")
print("Information : ")
print(df.info())
print("_________________________________________________________________")
print("Description/Statistics : ")
print(df.describe())