import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model, scaler, and feature selector
model = joblib.load('Student_Analyzer_t3.pkl')
scaler = joblib.load('scaler.pkl')
selector = joblib.load('feature_selector.pkl')

st.set_page_config(page_title="🎓 Student Performance Analyzer", page_icon="🎯", layout="centered")

st.title("🎓 Student Performance Analyzer")
st.markdown("Enter student details to predict the **Final Score** or **Performance Level**")

# Input form
with st.form("student_form"):
    col1, col2 = st.columns(2)

    with col1:
        study_hours = st.slider("📚 Study Hours per Week", 0, 60, 20)
        attendance = st.slider("🎯 Attendance Percentage", 0, 100, 85)
        prev_score = st.slider("📊 Previous Semester Score", 0, 100, 70)
        

    with col2:
      
        
        test_anxiety = st.slider("😰 Test Anxiety Level (1-10)", 1, 10, 5)
        teacher_feedback=st.slider("  Teacher Feedback (1-10)",1,10)
        library_usage = st.slider("📖 Library Usage per Week (hours)", 0, 20, 5)

    submitted = st.form_submit_button("🔍 Predict Performance")

# Prediction Logic
if submitted:
    # Convert categorical fields to numeric for the model
    

    input_data = {
        "Study_Hours_per_Week": study_hours,
        "Attendance_Percentage": attendance,
        "Previous_Sem_Score": prev_score,
        
        "Test_Anxiety_Level": test_anxiety,
        "Teacher_Feedback":teacher_feedback,
        "Library_Usage_per_Week": library_usage
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=scaler.feature_names_in_, fill_value=0)

    # Preprocessing
    scaled_input = scaler.transform(input_df)
    selected_input = selector.transform(scaled_input)

    # Predict
    prediction = model.predict(selected_input)[0]

    print("Input Features:")
    for col, val in input_df.iloc[0].items():
        print(f"{col:<30} : {val}")

    print(f"\nPredicted Final Score: {prediction:.2f}")

    st.success(f"📈 Predicted Final Score: **{prediction:.2f}**")

    if prediction >= 85:
        st.balloons()
        st.info("🌟 Excellent Performance Expected!")
    elif prediction >= 60:
        st.warning("⚡ Moderate Performance – Can Improve!")
    else:
        st.error("📉 Low Performance – Needs Attention!")

st.markdown("---")
st.caption("Developed by Atchaya •  Student Analyzer 💡")
