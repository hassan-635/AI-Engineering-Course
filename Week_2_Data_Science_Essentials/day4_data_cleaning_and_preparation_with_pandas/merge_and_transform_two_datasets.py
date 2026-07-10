import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "Name" : ["Hassan", "Ali", "Abrar"],
    "Age" : [19, 15, 18]
})

df2 = pd.DataFrame({
    "id" : [2, 3, 4],
    "Country" : ["Pakistan", "Iran", "Iraq"]
})

df = pd.merge(df1, df2, how="inner",on="id")

print(df)