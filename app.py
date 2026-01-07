import streamlit as st
import pandas as pd
import pickle
from monitor import get_live_vitals
from chatbot import chatbot_response

with open("models/heart_model.pkl", "rb") as f:
    model, scaler, feature_names = pickle.load(f)

st.set_page_config(page_title="Smart AI Healthcare", layout="wide")
st.title("🏥 Smart AI Healthcare Monitoring & Assistant System")

menu = st.sidebar.radio(
    "Select Module",
    ["Live Health Monitoring", "Heart Disease Prediction", "Healthcare Chatbot"]
)

if menu == "Live Health Monitoring":
    st.subheader("📊 Live Health Monitoring (Simulated)")

    vitals = get_live_vitals()

    col1, col2 = st.columns(2)
    col1.metric("❤️ Heart Rate", vitals["Heart Rate"])
    col2.metric("🌡 Body Temperature", vitals["Body Temperature"])

    col3, col4 = st.columns(2)
    col3.metric("🫁 Oxygen Level", vitals["Oxygen Level"])
    col4.metric("🩸 Blood Pressure", vitals["Blood Pressure"])

elif menu == "Heart Disease Prediction":
    st.subheader("🧠 Heart Disease Prediction (Kaggle Dataset)")

    age = st.number_input("Age", 20, 100)
    sex = st.selectbox("Sex (1=Male, 0=Female)", [0, 1])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Cholesterol")
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
    restecg = st.selectbox("Rest ECG", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate")
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression")
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.selectbox("Major Vessels", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

    if st.button("Predict"):
        input_data = pd.DataFrame(
            [[age, sex, cp, trestbps, chol, fbs, restecg,
              thalach, exang, oldpeak, slope, ca, thal]],
            columns=feature_names
        )

        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")

else:
    st.subheader("🤖 AI Healthcare Chatbot")
    user_input = st.text_input("Ask a health-related question")

    if st.button("Ask"):
        st.info(chatbot_response(user_input))
