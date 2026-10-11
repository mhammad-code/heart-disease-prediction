
import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Load the trained model and label encoder
BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "heart_disease_svc_model.pkl", "rb") as file:
    model = pickle.load(file)

with open(BASE_DIR / "heart_disease_le_cp.pkl", "rb") as file:
    le_cp = pickle.load(file)

# App interface
st.title("❤️ Heart Disease Prediction")
st.write(
    "Enter the following information to get a prediction "
    "from the trained machine learning model."
)

st.info("This tool is for educational purposes, not medical diagnosis.")

# Input fields
age = st.number_input(
    "Age", min_value=1, max_value=120, value=45
)

thalach = st.number_input(
    "Maximum Heart Rate (thalach)",
    min_value=1, max_value=300, value=150
)

chol = st.number_input(
    "Cholesterol (chol)",
    min_value=1, max_value=1000, value=220
)

cp = st.selectbox(
    "Chest Pain Type (cp)",
    options=list(le_cp.classes_)
)

# Make prediction
if st.button("Predict Heart Disease", type="primary"):
    try:
        encoded_cp = le_cp.transform([cp])[0]

        # Keep the same feature order used during training
        input_data = pd.DataFrame(
            [[age, thalach, chol, encoded_cp]],
            columns=["age", "thalach", "chol", "cp"]
        )

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.warning(
                "The model predicts the positive heart disease class."
            )
        else:
            st.success(
                "The model predicts the negative heart disease class."
            )

        st.caption(
            "This prediction is not a diagnosis. "
            "Consult a qualified healthcare professional for medical advice."
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")
