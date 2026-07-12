import pandas as pd
import matplotlib.pyplot as plt

gym = {
    "Member_ID":[101,102,103,104,105,106,107,108,109,110,111,112],

    "Month":[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "New_Members":[
        45,52,60,70,85,90,
        88,95,80,75,68,72
    ],

    "Trainer":[
        "Ali","Ahmed","Ali","Hassan","Ahmed","Ali",
        "Hassan","Ali","Ahmed","Ali","Hassan","Ahmed"
    ],

    "Workout_Hours":[
        5,7,8,6,9,10,
        8,11,7,6,9,10
    ],

    "Calories_Burned":[
        1200,1700,2000,1500,2400,2600,
        2100,2800,1800,1600,2350,2550
    ],

    "Age":[
        18,20,22,25,24,27,
        30,28,26,21,23,29
    ],

    "City":[
        "Lahore","Karachi","Islamabad","Lahore",
        "Karachi","Islamabad","Lahore",
        "Karachi","Islamabad","Lahore",
        "Karachi","Islamabad"
    ]
}

df = pd.DataFrame(gym)
print(df.to_string(index=False))


# which month has more members

plt.plot(df["Month"], df["New_Members"], marker="o")
plt.title("Month vs Members")
plt.xlabel("Month")
plt.ylabel("New Members")
plt.grid(True)
plt.show()
