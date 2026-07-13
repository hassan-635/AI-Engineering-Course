# gym meber analysis

import pandas as pd
import matplotlib.pyplot as plt

gym = {
    "Member_ID": [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],

    "Trainer": [
        "Ali","Ali","Ali","Ali","Ali",
        "Ahmed","Ahmed","Ahmed","Ahmed","Ahmed",
        "Hassan","Hassan","Hassan","Hassan","Hassan"
    ],

    "Workout_Hours": [
        5,6,7,8,9,
        7,8,9,10,11,
        4,5,6,7,8
    ],

    "Calories_Burned": [
        1500,1700,1900,2100,2300,
        1800,2000,2200,2500,2700,
        1200,1400,1600,1800,2000
    ],

    "Age": [
        20,21,22,23,24,
        25,26,27,28,29,
        19,20,21,22,23
    ]
}

df = pd.DataFrame(gym)

plt.hist(x=df[df["Trainer"] == "Ali"]["Calories_Burned"], bins = 4, color="green", label="Ali", alpha = 0.8)
plt.hist(x=df[df["Trainer"] == "Ahmed"]["Calories_Burned"], bins = 4, color="blue", label="Ahmed", alpha = 0.3)
plt.hist(x=df[df["Trainer"] == "Hassan"]["Calories_Burned"], bins = 4, color="red", label= "Hassan", alpha = 0.3)
plt.grid(True)
plt.legend()
plt.xlabel("Calories Burned")
plt.title("Distribution of Calories Burned")
plt.show()