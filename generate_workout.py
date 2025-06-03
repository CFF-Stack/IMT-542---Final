import os
import json
from datetime import datetime
#
WORKOUT_DIR = "workouts"
BASE_WEIGHTS = {
    "Squat": 50.0,
    "Bench Press": 40.0,
    "Barbell Row": 40.0,
    "Overhead Press": 30.0,
    "Deadlift": 60.0
}

INCREMENT_LOWER = 2.5
INCREMENT_UPPER = 1.25
CAP_WEIGHTS = {
    "Squat": 150.0,
    "Deadlift": 189.0,
    "Bench Press": 120.0,
    "Barbell Row": 110.0,
    "Overhead Press": 85.0
}

def load_last_workout(workout_type):
    if not os.path.exists(WORKOUT_DIR):
        return None
    files = sorted(f for f in os.listdir(WORKOUT_DIR) if f.endswith(".json"))
    for f_name in reversed(files):
        with open(os.path.join(WORKOUT_DIR, f_name)) as f:
            data = json.load(f)
            if data.get("workout_type") == workout_type:
                return data
    return None

def prompt_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please type 'y' or 'n'.")

def make_exercise_entry(ex_name, weight_kg, sets_count, reps=5):
    sets = []
    for i in range(sets_count):
        prompt = f"Was set {i+1} of {ex_name} at {weight_kg} kg successful? (y/n): "
        successful = prompt_yes_no(prompt)
        sets.append({
            "set_number": i + 1,
            "weight_kg": weight_kg,
            "reps": reps,
            "successful": successful
        })
    return {
        "exercise_name": ex_name,
        "sets": sets,
        "notes": ""
    }

def record_workout():
    w_type = ""
    while w_type not in ("A", "B"):
        w_type = input("Enter workout type to record (A or B): ").strip().upper()

    # Load last workout to get weight progression
    last = load_last_workout(w_type)
    weights = BASE_WEIGHTS.copy()

    if last:
        for ex in last["exercises"]:
            name = ex["exercise_name"]
            last_weight = ex["sets"][0]["weight_kg"]
            # Determine if last workout for this exercise was successful overall
            last_success = all(s["successful"] for s in ex["sets"])
            if last_success:
                inc = INCREMENT_LOWER if name in ("Squat", "Deadlift") else INCREMENT_UPPER
                weights[name] = min(last_weight + inc, CAP_WEIGHTS[name])
            else:
                weights[name] = last_weight

    # Determine which exercises and set counts to use
    if w_type == "A":
        exercises = ["Squat", "Bench Press", "Barbell Row"]
        set_counts = {"Squat": 5, "Bench Press": 5, "Barbell Row": 5}
    else:
        exercises = ["Squat", "Overhead Press", "Deadlift"]
        set_counts = {"Squat": 5, "Overhead Press": 5, "Deadlift": 1}

    # Create detailed exercise data with success per set
    workout_exercises = []
    for ex in exercises:
        ex_data = make_exercise_entry(ex, weights[ex], set_counts[ex])
        workout_exercises.append(ex_data)

    # Build final workout record
    today = str(datetime.now().date())
    workout_id = f"{today}-{w_type}"
    workout_data = {
        "workout_id": workout_id,
        "date": today,
        "program": "StrongLifts 5x5",
        "workout_type": w_type,
        "exercises": workout_exercises,
        "metadata": {
            "duration_min": None,
            "user_feeling": input("How did you feel? (e.g., strong, tired): "),
            "location": input("Where did you train? (e.g., Home Gym): ")
        }
    }

    # Save to JSON
    os.makedirs(WORKOUT_DIR, exist_ok=True)
    fname = os.path.join(WORKOUT_DIR, f"workout_{today}_{w_type}.json")
    with open(fname, "w") as f:
        json.dump(workout_data, f, indent=4)

    # Final summary
    print(f"\nWorkout {workout_id} summary:")
    for ex in workout_exercises:
        successes = [s["successful"] for s in ex["sets"]]
        print(f" • {ex['exercise_name']}: {sum(successes)}/{len(successes)} sets successful")
    print(f"\nWorkout record saved to: {fname}\n")

if __name__ == "__main__":
    record_workout()
