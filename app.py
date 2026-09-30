import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("heart_disease_model.pkl")

# Title
st.title("❤️ Heart Disease Prediction")

st.write("Enter patient details below:")

# Inputs
age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Blood Pressure", 50, 250, 120)
chol = st.number_input("Cholesterol", 50, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate", 50, 250, 150)
exang = st.selectbox("Exercise Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Major Vessels", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Prediction
if st.button("🔍 Predict"):

    data = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]], columns=[
        "age", "sex", "cp", "trestbps", "chol",
        "fbs", "restecg", "thalach", "exang",
        "oldpeak", "slope", "ca", "thal"
    ])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("⚠️ Heart Disease Predicted")
    else:
        st.success("✅ No Heart Disease Predicted")