import streamlit as st
import joblib
import numpy as np

# ===============================
# LOAD MODEL
# ===============================
model = joblib.load("rf_model.pkl")

# ===============================
# UI
# ===============================
st.set_page_config(page_title="Sensor Alert System", layout="centered")

st.title("🔥 Sensor Alert Prediction System")
st.write("Enter sensor values to predict alert")

# ===============================
# INPUTS
# ===============================
time_sec = st.number_input("⏱️ Time (seconds)", min_value=0.0, step=0.1)
node_id = st.number_input("🖥️ Node ID", min_value=0, step=1)
temperature = st.number_input("🌡️ Temperature", step=1.0)

# ===============================
# THRESHOLD
# ===============================
threshold = st.slider("⚙️ Alert Threshold", 0.0, 1.0, 0.5)

# ===============================
# PREDICTION
# ===============================
if st.button("🔮 Predict"):
    data = np.array([[time_sec, node_id, temperature]])

    pred = model.predict(data)[0]
    proba = model.predict_proba(data)[0][1]

    st.write(f"📊 Confidence Score: {proba:.2f}")

    if proba > threshold:
        st.error("🚨 ALERT DETECTED!")
    else:
        st.success("✅ Normal Condition")

# ===============================
# EXTRA INFO
# ===============================
st.markdown("---")
st.subheader("📌 About Model")

st.write("""
- Model Used: Random Forest  
- Input Features: Time, Node ID, Temperature  
- Output: Alert (0 = Normal, 1 = Alert)  
""")