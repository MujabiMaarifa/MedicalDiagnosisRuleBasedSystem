🩺 Medical Diagnosis Expert System (Forward & Backward Chaining)

Overview
This project implements a rule-based expert system in Python that simulates a simplified medical diagnosis process. It demonstrates how forward chaining and backward chaining can be used to reason about symptoms, derive possible diagnoses, and recommend treatments.
The system is designed as a learning tool for understanding knowledge representation, inference engines, and AI reasoning strategies.


Features
- Fact Management
- Add and store known symptoms or conditions as facts.
- Rule Management
- Define medical rules as logical implications (conditions → conclusion).
- Forward Chaining
- Starts with known symptoms and applies rules iteratively to derive all possible diagnoses and treatments.
- Backward Chaining
- Starts with a goal (e.g., “prescribe_rest”) and works backward through rules to check if it can be proven from existing facts.
- Loop Prevention
- Uses a visited set in backward chaining to avoid infinite recursion when rules reference each other.


Example Use Case
Rules
- fever AND cough → suspect_flu
- suspect_flu AND body_ache → diagnose_flu
- diagnose_flu → prescribe_rest

📖 Learning Objectives
- Understand the difference between forward chaining (data-driven) and backward chaining (goal-driven) reasoning.
- Explore how expert systems can be built using simple rule-based logic.
- Gain hands-on experience with knowledge representation in Python.
- Apply AI reasoning concepts to a practical domain (medical diagnosis).

Clone the repository:
git clone https://github.com/MujabiMaarifa/MedicalDiagnosisRuleBasedSystem
cd MedicalDiagnosisRuleBasedSystem

Run the python script:
python MedicalDiagnosis.py

🔧 Future Enhancements
- Add conflict resolution strategies (e.g., prioritizing certain rules).
- Support probabilistic reasoning (e.g., likelihood of flu given symptoms).
- Extend to more complex domains (e.g., multiple diseases, overlapping symptoms).
- Build a simple user interface for entering symptoms interactively.


