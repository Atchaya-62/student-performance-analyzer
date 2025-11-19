import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("student_analyzer.pkl")

st.set_page_config(page_title="Student Performance Analyzer")

st.title("🎓 Student Performance Analyzer")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])
internet = st.selectbox("Internet Access", ["Yes", "No"])
motivation = st.slider("Motivation Level (1-10)", 1, 10)
study_hours = st.number_input("Study Hours / Day", 0, 10)
attendance = st.number_input("Attendance %", 0, 100)

# Create input DF exactly like training set
input_df = pd.DataFrame({
    "Gender": [gender],
    "Family_Income": [family_income],
    "Internet_Access": [internet],
    "Motivation_Level": [motivation],
    "Study_Hours": [study_hours],
    "Attendance": [attendance]
})

# Predict
if st.button("Predict Performance"):
    pred = pipeline.predict(input_df)[0]
    st.success(f"📊 Predicted Score: {pred:.2f}")
