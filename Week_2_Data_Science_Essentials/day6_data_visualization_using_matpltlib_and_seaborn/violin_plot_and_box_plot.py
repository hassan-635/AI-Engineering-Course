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

sns.set_style("whitegrid")
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=df,
            x="Trainer",
            y="Calories_Burned",
            palette="Set2",
            showmeans=True)
plt.xlabel("Trainer")
plt.ylabel("Calories Burned")
plt.title("Box Plot")

plt.subplot(1, 2, 2)
sns.violinplot(data=df,
               x="Trainer",
               y="Calories_Burned",
               palette="Set2")
plt.xlabel("Trainer")
plt.ylabel("Calories Burned")
plt.title("Violin Plot")

plt.show()