import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Trainer": ["Ali"]*5 + ["Hassan"]*5 + ["Ahmed"]*5,
    "Calories_Burned": [
        1400,1500,1600,1700,2500,
        1500,1520,1530,1540,1550,
        1200,1500,1800,2100,2400
    ]
}

df = pd.DataFrame(data)
print(df)