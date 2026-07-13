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

trainer_df = df.groupby("Trainer")["New_Members"].sum()
print(trainer_df.to_string(index=False))
print(df.to_string(index=False))



plt.figure(figsize=(12, 10))
plt.subplots_adjust(wspace=0.8, hspace=0.8)

# which month has more members
plt.subplot(4, 2, 1)
plt.plot(df["Month"], df["New_Members"],label="line", marker="o")
plt.title("Month vs Members")
plt.xlabel("Month")
plt.ylabel("New Members")
plt.grid(True)

# total new members trained each year
plt.subplot(4, 2, 2)
plt.bar(trainer_df.index, trainer_df.values, label="bar")
for i, value in enumerate(trainer_df.values):
    plt.text(i, value+1, str(value))
plt.grid(True)

# relation between workout hours and calories burned
plt.subplot(4, 2, 3)
plt.scatter(x=df["Workout_Hours"], y=df["Calories_Burned"], marker="o")
plt.xlabel("Workout Hours")
plt.ylabel("Calories burnt")
plt.title("Workout Hours vs. Calories Burnt")
plt.grid(True)

# age disatribution
plt.subplot(4, 2, 4)
plt.hist(df["Age"], bins=4),
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)

# city vs new members
plt.subplot(4, 2, 5)
plt.bar(df["City"], df["New_Members"])
plt.title("City vs. New Members")
plt.xlabel("City")
plt.ylabel("New Members")
plt.grid(True)

# city members average burnt calories
avg_burnt_cals = df.groupby("City")["Calories_Burned"].mean()
plt.subplot(4, 2, 6)
plt.bar(avg_burnt_cals.index, avg_burnt_cals.values)
plt.title("Average Burned Calories with respect to city")
plt.xlabel("City")
plt.ylabel("Calories Burned")
plt.grid(True)

# AVERAGE WORKOUT HOURS OF EVERY trainer

avg_workout_hours = df.groupby("Trainer")["Workout_Hours"].mean()
plt.subplot(4, 2, 7)
plt.bar(avg_workout_hours.index, avg_workout_hours.values)
plt.title("Average Workout Hours of Every Member")
plt.xlabel("Trainer")
plt.ylabel("Average Workout Hours")
plt.grid(True)

plt.tight_layout()
plt.show()