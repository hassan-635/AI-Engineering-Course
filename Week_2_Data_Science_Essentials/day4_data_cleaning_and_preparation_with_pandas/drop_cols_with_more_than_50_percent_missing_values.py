import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Id" : [1, 2, 3, 4, 5, 6, 7, 8],
    "Name" : ["Alice", "Bob", "Charlie", np.nan, "Elon", "Faizan", np.nan, "Haider"],
    "Marks" : [45, 50, 56, np.nan, np.nan, np.nan, np.nan, np.nan], 
    "Score" : [10, 20, np.nan, np.nan, np.nan, np.nan, np.nan, 10]
})

print("\n_____________________________________________________________\nOriginal Dataset : \n")
print(df.to_string(index=False))
print("\n_____________________________________________________________\nDropped Miising Values Dataset : \n")
