import streamlit as st
import joblib
import pandas as pd

# Load models and features
covers_model = joblib.load("covers_model.pkl")
avg_model = joblib.load("avg_check_model.pkl")
features = joblib.load("features.pkl")

st.title("🍽️ Restaurant Demand Prediction")
st.markdown("Predict daily covers and average check")

# --- USER INPUT ---
st.header("Enter Inputs")

input_dict = {}

for feature in features:
    if feature == 'day_of_week':
        input_dict[feature] = st.selectbox("Day of Week (0=Mon)", list(range(7)))
    elif feature == 'is_weekend':
        input_dict[feature] = st.selectbox("Weekend?", [0, 1])
    else:
        input_dict[feature] = st.number_input(f"{feature}", value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# --- Prediction ---
if st.button("Predict"):
    covers_pred = covers_model.predict(input_df)[0]
    avg_pred = avg_model.predict(input_df)[0]

    st.success(f"👥 Predicted Covers: {covers_pred:.2f}")
    st.success(f"💰 Predicted Avg Check: ${avg_pred:.2f}")
