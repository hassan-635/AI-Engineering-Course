import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

students = {
    "Student": [
        "Ali","Ahmed","Hassan","Bilal","Umer",
        "Saad","Usman","Hamza","Ahsan","Zain"
    ],

    "Math": [90,75,85,60,95,70,88,65,80,92],

    "Physics": [88,70,82,58,96,68,90,62,78,94],

    "Chemistry": [85,72,80,65,90,70,84,68,76,89],

    "English": [70,80,75,85,68,90,72,88,84,71],

    "Computer": [95,78,90,70,98,75,94,72,86,97]
}

df = pd.DataFrame(students)
print(df.to_string(index=False))
del df["Student"]
correlation = df.corr()
print(correlation)

sns.heatmap(data=correlation,
            cmap="coolwarm",
            annot=True)
plt.title("Correlation between subjects")
plt.show()