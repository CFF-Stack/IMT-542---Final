Test Plan for StrongLifts 5x5 Portable Information System

1. Purpose
This test plan outlines the desired quality and performance standards for the StrongLifts 5x5 portable information system. It defines the testing framework for ensuring that the data model, data collection workflows, and visualization scripts work correctly and consistently, and that the system maintains high data integrity, accessibility, and portability throughout its lifecycle.

2. Scope
This plan covers:

Functional tests: Validation of data structure, workflows, and user interactions.
Performance tests: Assessment of data handling, script execution times, and file access performance.
Alarms and actions: Procedures to identify, alert, and correct any failures in data quality or system operation.

It applies to all scripts (record_workout.py, visualize_workouts.py), JSON data files in the workouts/ folder, and supporting documentation.

3. Test Objectives

Verify that all user inputs are correctly captured in the JSON data structure.
Ensure that data remains consistent, complete, and free of errors across workflows.
Confirm that file-based access (reading, writing, parsing JSON) is reliable and performant.
Validate that plots and data summaries generated from the JSON data are accurate.
Provide early detection of any data or performance issues.

## 4. Functional Testing

| Test Case                       | Method                                              | Expected Result                                                   | Frequency        |
|---------------------------------|-----------------------------------------------------|-------------------------------------------------------------------|------------------|
| Data entry validation           | Run `record_workout.py`, enter sample data          | JSON file created with all required fields and correct data types | Every new release; random spot checks. |
| Set-level tracking              | Confirm `"successful": true/false` is recorded      | Accurate success/failure per set                                  | Ongoing.         |
| File naming and integrity       | Check JSON file naming convention and structure     | Files are named `workout_YYYY-MM-DD_A.json` or `_B.json`, parseable JSON | Every file.      |
| Field consistency               | Review field names (`exercise_name`, `sets`, etc.)  | No unexpected or missing fields                                   | Bi-weekly.       |
| Visualization output            | Run `visualize_workouts.py`                         | Plots display correct weight progression and success rates        | After data entry updates. |

---

## 5. Performance Testing

| Test Case                       | Method                                                  | Expected Result                           | Frequency        |
|---------------------------------|---------------------------------------------------------|-------------------------------------------|------------------|
| Script execution time           | Time execution of `record_workout.py` and `visualize_workouts.py`. | Scripts run within acceptable time (under 3 seconds for typical datasets). | Quarterly.       |
| Large dataset handling          | Test with 6 months of data (e.g., 70+ workouts).        | Scripts process data without significant lag or crashes. | Quarterly.       |
| File read/write integrity       | Verify file reads/writes under typical usage scenarios. | No data corruption or parse errors.       | Quarterly.       |

---

## 6. Alarms and Actions

| Alarm/Trigger                        | Action                                                    | 
|--------------------------------------|-----------------------------------------------------------|
| JSON parse error                     | Investigate the file, restore from last known-good file.  | 
| Unexpected field or data type        | Update scripts to handle new data type or fix input issue.| 
| Visualization error                  | Check data consistency, confirm no corruption.            |
| Slow performance (>3 seconds)        | Profile scripts, identify bottlenecks, optimize parsing.  |

7. Ongoing Quality Assurance
Version control: All script and data structure changes will be version-controlled in GitLab.

Peer review: Significant updates to scripts or the JSON schema will be peer-reviewed before deployment.

Spot checks: Every 2-4 weeks, randomly review JSON files for completeness and adherence to schema.

Data backups: Periodically back up the workouts/ folder to prevent data loss.

User feedback: Users are encouraged to report issues or inconsistencies. These will be logged and resolved with each minor release.

8. Living Document Approach
This test plan is intended to be updated continuously as:

New features are added (e.g., deload logic, cloud sharing).

Data structures evolve (e.g., new fields or metadata types).

External integrations are added (e.g., APIs, health data standards).

The document will be reviewed at least every six months to ensure ongoing relevance and alignment with user needs.
