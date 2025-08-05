import streamlit as st
import pandas as pd
import joblib

# Load saved models
lr_model = joblib.load('lr_model.pkl')
rf_model = joblib.load('rf_model.pkl')

# Sidebar - Select model
model_choice = st.sidebar.selectbox("Choose ML Model", ["Linear Regression", "Random Forest"])

st.title("📊 Math Score Predictor")

st.markdown("Enter the student's details to predict their **Math Score** based on reading & writing scores.")

# Input form
gender = st.selectbox("Gender", ["male", "female"])
race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent_edu = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college",
    "associate's degree", "bachelor's degree", "master's degree"])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.slider("📖 Reading Score", 0, 100, 50)
writing_score = st.slider("✍️ Writing Score", 0, 100, 50)

# Encode lunch manually (same as training time)
lunch_standard = 1 if lunch == "standard" else 0

# Create input DataFrame (must match training features)
input_df = pd.DataFrame({
    'reading_score': [reading_score],
    'writing_score': [writing_score],
    'lunch_standard': [lunch_standard]
})

# Predict
if st.button("🔮 Predict Math Score"):
    if model_choice == "Linear Regression":
        prediction = lr_model.predict(input_df)[0]
    else:
        prediction = rf_model.predict(input_df)[0]

    st.success(f"🧮 Predicted Math Score: {prediction:.2f}")

# Pass/Fail logic
    scores = [reading_score, writing_score, prediction]
    st.subheader("📋 Pass/Fail Status")
    avg_score = sum(scores)/len(scores)
    if all(score >= 40 for score in scores):
        result = "✅ Pass with average score: {:.2f}".format(avg_score)
    else:
        result = "❌ Fail with average score: {:.2f}".format(avg_score)

    # Grade assignment function
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 40:
            return "E"
        else:
            return "F"

    st.info(f"Result: {result}")
    st.write(f"Grades:")
    st.write(f"- Reading: {get_grade(reading_score)}")
    st.write(f"- Writing: {get_grade(writing_score)}")
    st.write(f"- Predicted Math: {get_grade(prediction)}")
    st.write(f"- Average Score: {get_grade(avg_score)}")

    # Bar chart to compare
    st.subheader("📊 Comparison Chart")
    st.bar_chart({
        'Scores': {
            'Reading': reading_score,
            'Writing': writing_score,
            'Predicted Math': prediction
        }
    })
