import os
import json
import random
from datetime import datetime, timedelta
##I found that I needed to generate data for the visualization, this script is what I used. 

# Constants
WORKOUT_DIR = "workouts"
EXERCISES_A = ["Squat", "Bench Press", "Barbell Row"]
EXERCISES_B = ["Squat", "Overhead Press", "Deadlift"]
INCREMENT_LOWER = 5.0  # kg
INCREMENT_UPPER = 2.5  # kg

# Cap values
CAP_WEIGHTS = {
    "Squat": 150,
    "Deadlift": 189,
    "Bench Press": 110,  # typically ~75% of max squat
    "Barbell Row": 100,  # typically ~66% of max squat
    "Overhead Press": 75  # typically ~50% of max squat
}

# Create a set with success logic
def create_set(set_number, weight_kg, reps, successful=True):
    return {
        "set_number": set_number,
        "weight_kg": weight_kg,
        "reps": reps,
        "successful": successful
    }

# Create exercise data for one exercise
def create_exercise(exercise_name, weight_kg, sets_count=5, notes=""):
    sets = []
    for i in range(sets_count):
        # 85% chance of success
        successful = random.choices([True, False], [0.85, 0.15])[0]
        sets.append(create_set(i+1, weight_kg, 5, successful))
    return {
        "exercise_name": exercise_name,
        "sets": sets,
        "notes": notes
    }

# Main generator function
def generate_workouts():
    os.makedirs(WORKOUT_DIR, exist_ok=True)
    start_date = datetime.now() - timedelta(weeks=26)  # 6 months ago

    # Starting weights
    current_weights = {
        "Squat": 50,
        "Bench Press": 40,
        "Barbell Row": 40,
        "Overhead Press": 30,
        "Deadlift": 60
    }

    workout_count = 0
    for week in range(26):  # 26 weeks
        for day_offset in [0, 2, 4]:  # 3 workouts/week
            workout_date = start_date + timedelta(days=week*7 + day_offset)
            workout_type = "A" if workout_count % 2 == 0 else "B"
            exercises = EXERCISES_A if workout_type == "A" else EXERCISES_B

            exercises_data = []
            for ex in exercises:
                sets_count = 1 if ex == "Deadlift" else 5
                ex_data = create_exercise(ex, current_weights[ex], sets_count=sets_count)
                exercises_data.append(ex_data)

                # If all sets successful, add weight (capped)
                if all(s["successful"] for s in ex_data["sets"]):
                    increment = INCREMENT_LOWER if ex in ["Squat", "Deadlift"] else INCREMENT_UPPER
                    next_weight = current_weights[ex] + increment
                    current_weights[ex] = min(next_weight, CAP_WEIGHTS[ex])

            # Workout metadata
            workout_json = {
                "workout_id": f"{workout_date.date()}-{workout_type}",
                "date": str(workout_date.date()),
                "program": "StrongLifts 5x5",
                "workout_type": workout_type,
                "exercises": exercises_data,
                "metadata": {
                    "duration_min": random.randint(40, 60),
                    "user_feeling": random.choice(["strong", "average", "tired"]),
                    "location": "Home Gym"
                }
            }

            # Save to JSON
            filename = os.path.join(WORKOUT_DIR, f"workout_{workout_date.date()}_{workout_type}.json")
            with open(filename, "w") as f:
                json.dump(workout_json, f, indent=4)

            workout_count += 1

    print(f"Generated {workout_count} workouts with capped weights in '{WORKOUT_DIR}'.")

if __name__ == "__main__":
    generate_workouts()
