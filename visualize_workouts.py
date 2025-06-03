import os
import json
import pandas as pd
import matplotlib.pyplot as plt

print("Current JSON files in workouts/ folder:")
for f in os.listdir("workouts"):
    print(" -", f)

WORKOUT_DIR = "workouts"

def load_existing_workouts():
    records = []
    files = sorted([f for f in os.listdir(WORKOUT_DIR) if f.endswith(".json")])
    for file in files:
        with open(os.path.join(WORKOUT_DIR, file)) as f:
            data = json.load(f)
            date = data["date"]
            workout_type = data["workout_type"]
            for ex in data["exercises"]:
                ex_name = ex["exercise_name"]
                for s in ex["sets"]:
                    records.append({
                        "date": date,
                        "workout_type": workout_type,
                        "exercise_name": ex_name,
                        "set_number": s["set_number"],
                        "weight_kg": s["weight_kg"],
                        "reps": s["reps"],
                        "successful": s["successful"]
                    })
    return pd.DataFrame(records)

def plot_weight_progression(df):
    plt.figure(figsize=(10,6))
    for ex_name in df["exercise_name"].unique():
        ex_data = df[df["exercise_name"] == ex_name]
        # Group by date and take the average weight for that day
        avg_weight = ex_data.groupby("date")["weight_kg"].mean()
        plt.plot(avg_weight.index, avg_weight.values, marker='o', label=ex_name)
    plt.xlabel("Date")
    plt.ylabel("Weight (kg)")
    plt.title("Weight Progression Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_success_rate(df):
    plt.figure(figsize=(10,6))
    df["success_numeric"] = df["successful"].apply(lambda x: 1 if x else 0)
    success_rate = df.groupby("date")["success_numeric"].mean() * 100
    plt.plot(success_rate.index, success_rate.values, marker='o', color='green')
    plt.xlabel("Date")
    plt.ylabel("Success Rate (%)")
    plt.title("Workout Success Rate Over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_existing_workouts()
    if df.empty:
        print("No workout data available.")
    else:
        df = df.sort_values("date")  # Ensure chronological order
        print("Loaded data preview:")
        print(df.head())
        plot_weight_progression(df)
        plot_success_rate(df)
