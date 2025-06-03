# IMT-542---Final

Group Project Presentation and Deliverables

Github repository should contain a Readme.md file that describes your project, including any code used to download and convert the structure and any code or processes for exposing the data as a website or API
A presentation file as a PDF stored in Github that you will present in class. Focus on a summary of your project that touches on the main points described above for:
Info story or who is the user and why is it important to them
Existing structure and FAIR assessment,
How you decided to improve the structure,
What your new structure is, and
How would quality be identified and addressed
For each of the 4 project grading elements above (and found rubric below) you should have documentation from prior class assignments that you can update and upload to Github using easy to understand file naming. These artifacts are what we will use for grading.


# 🏋️‍♂️ StrongLifts 5x5 Tracker & Visualizer

A **modular, Python-powered system** for tracking and analyzing weightlifting workouts, with a focus on the StrongLifts 5x5 program.

---

## 🚀 Project Goals

✅ Enable **clear data recording** for workouts (including set-level success/failure)  
✅ Create a **structured JSON dataset** for portability and future integration  
✅ Provide **visual insights** with progression graphs and success rates  
✅ Ensure **sustainable tracking** across platforms, no lock-in to proprietary systems

---

## 🧱 Features

### 🔥 Workout Data Recording
- Interactive script `record_workout.py` to **prompt you** for each set’s success/failure.
- **Accurate JSON logs** for each workout, stored in the `workouts/` folder.

### 📈 Visualization & Analysis
- `visualize_workouts.py` script:
  - Plots **weight progression** over time for each exercise.
  - Plots **success rates** (percent of sets completed) for quality tracking.
- **Portable, open** data—no vendor lock-in!

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


