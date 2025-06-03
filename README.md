# IMT-542---Final

Group Project Presentation and Deliverables

StrongLifts 5x5 Tracker & Visualizer

A modular, Python-powered system for tracking and analyzing weightlifting workouts, with a focus on the StrongLifts 5x5 program.

---

## 🚀 Project Goals

✅ Enable **clear data recording** for workouts (including set-level success/failure)  
✅ Create a **structured JSON dataset** for portability and future integration  
✅ Provide **visual insights** with progression graphs and success rates  
✅ Ensure **sustainable tracking** across platforms, no lock-in to proprietary systems

---

## 🧱 Features

### 🔥 Workout Data Recording
- Interactive script `generate_workout.py` to **prompt you** for each set’s success/failure.
- **Accurate JSON logs** for each workout, stored in the `workouts/` folder.

### 📈 Visualization & Analysis
- `visualize_workouts.py` script:
  - Plots **weight progression** over time for each exercise.
  - Plots **success rates** (percent of sets completed) for quality tracking.
- **Portable, open data** —no vendor lock-in!

### ⚙️ Weight Progression Logic
- Increases weight **gradually** (e.g., +2.5kg or +1.25kg) only if all sets of an exercise are successful.
- **Caps** for each exercise to reflect realistic progression goals:
  - Squat: 150 kg
  - Deadlift: 189 kg
  - Bench Press: 120 kg
  - Barbell Row: 110 kg
  - Overhead Press: 85 kg
- If sets are not successful, the next workout **holds** at the same weight (future deload logic can be added!).

---

## 📂 Project Structure
project/
├── workouts/ # JSON logs for each workout
├── Other Files/ # Files that helped along the Way, Strong Lifts 5X5, Garmin
├── visualize_workouts.py # Data visualization script
├── generate_workout.py # Interactive logger for recording workout data
└── README.md # Project documentation (this file!)


---

## 📦 Installation


Install required Python packages:

'pip install pandas matplotlib'

🚀 Usage
Record a Workout
bash
Copy
Edit
'python generate_workout.py'
✅ Prompts you to log actual set success/failure for the current workout.

Visualize Data
bash
Copy
Edit
'python visualize_workouts.py'
✅ Generates clear plots of:

Weight progression for each lift

Success rate for your lifting consistency

Data Flow
Input: User logs workout in record_workout.py
Output: Structured JSON file saved in workouts/
Analysis: visualize_workouts.py loads these JSON files, parses them into a pandas DataFrame, and creates visual plots.

*Generated with the Assistance of ChatGPT, edited for consistency, content and cohesion.
