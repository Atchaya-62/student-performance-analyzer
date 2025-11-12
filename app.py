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
        parental_edu = st.selectbox("👨‍🏫 Parental Education Level", ["Low", "Medium", "High"])
        internet_access = st.selectbox("🌐 Internet Access", ["No", "Yes"])
        tutoring = st.selectbox("📘 Attends Tutoring Classes?", ["No", "Yes"])
        sports = st.selectbox("⚽ Sports Activity", ["No", "Yes"])

    with col2:
        extracurricular = st.selectbox("🎭 Extracurricular Activities", ["No", "Yes"])
        school_type = st.selectbox("🏫 School Type", ["Public", "Private"])
        sleep_hours = st.slider("💤 Average Sleep Hours", 3, 10, 7)
        travel_time = st.slider("🚌 Travel Time to School (mins)", 0, 120, 30)
        test_anxiety = st.slider("😰 Test Anxiety Level (1-10)", 1, 10, 5)
        motivation = st.slider("🔥 Motivation Level (1-10)", 1, 10, 7)
        library_usage = st.slider("📖 Library Usage per Week (hours)", 0, 20, 5)

    submitted = st.form_submit_button("🔍 Predict Performance")

# Prediction Logic
if submitted:
    # Convert categorical fields to numeric for the model
    parental_edu_map = {"Low": 0, "Medium": 1, "High": 2}
    yes_no_map = {"No": 0, "Yes": 1}
    school_type_map = {"Public": 0, "Private": 1}

    input_data = {
        "Study_Hours_per_Week": study_hours,
        "Attendance_Percentage": attendance,
        "Previous_Sem_Score": prev_score,
        "Parental_Education": parental_edu_map[parental_edu],
        "Internet_Access": yes_no_map[internet_access],
        "Tutoring_Classes": yes_no_map[tutoring],
        "Sports_Activity": yes_no_map[sports],
        "Extra_Curricular": yes_no_map[extracurricular],
        "School_Type": school_type_map[school_type],
        "Sleep_Hours": sleep_hours,
        "Travel_Time": travel_time,
        "Test_Anxiety_Level": test_anxiety,
        "Motivation_Level": motivation,
        "Library_Usage_per_Week": library_usage
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=scaler.feature_names_in_, fill_value=0)

    # Preprocessing
    scaled_input = scaler.transform(input_df)
    selected_input = selector.transform(scaled_input)

    # Predict
    prediction = model.predict(selected_input)[0]

    st.success(f"📈 Predicted Final Score: **{prediction:.2f}**")

    if prediction >= 85:
        st.balloons()
        st.info("🌟 Excellent Performance Expected!")
    elif prediction >= 60:
        st.warning("⚡ Moderate Performance – Can Improve!")
    else:
        st.error("📉 Low Performance – Needs Attention!")

st.markdown("---")
st.caption("Developed by Atchaya • AI&DS Student Analyzer 💡")
