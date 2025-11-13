STUDENT PERFORMANCE ANALYZER
A web-based application that predicts student academic performance using machine-learning.
Builds on a dataset of student attributes and outputs a predicted performance score or level.

FEATURES

Input student features (e.g., study time, past scores, attendance) and receive a predicted outcome.

Web interface built with Python and Streamlit (via app.py).

Includes model artefacts: scaler, feature selector and trained model (.pkl files).

Dataset (students_performance_dataset.xlsx) included for training / reference.

Ready to deploy or extend for custom datasets and further features.

PREREQUISITIES

Python 3.7+

pip (or equivalent)

Recommended: virtual environment for isolation

INSTALLATION & SETUP

1.Clone the repository

git clone https://github.com/Atchaya-62/student-performance-analyzer.git
cd student-performance-analyzer

2.Install dependencies

pip install -r requirements.txt

RUNNING THE APP
streamlit run app.py

Then open your browser at http://localhost:8501 to access the interface.

WORKFLOW

User inputs student feature values via the UI.

These inputs are scaled using scaler.pkl.

Feature selection via feature_selector.pkl.

Prediction performed by the trained model (Student_Analyzer_t3.pkl).

Predicted performance score or class displayed to the user with optional insights.

FILE STRUCTURE

student-performance-analyzer/
├── app.py                        
├── Student_Analyzer_t3.ipynb     
├── Student_Analyzer_t3.pkl      
├── scaler.pkl                      
├── feature_selector.pkl          
├── students_performance_dataset.xlsx   
├── requirements.txt              
└── README.md  

USING THE APP- GUIDE
Step 1: Input student information
<img width="1014" height="599" alt="image" src="https://github.com/user-attachments/assets/64ad6aca-60a1-47ed-9e89-06715bd66ee2" />

Step 2: Click “Predict”
<img width="945" height="409" alt="image" src="https://github.com/user-attachments/assets/7a1188bd-410f-49ba-b3f6-93c05aa2769b" />

Step 3: View predicted performance
<img width="1003" height="303" alt="image" src="https://github.com/user-attachments/assets/1dc6be6f-2132-48a9-8810-576c728fb90b" />
