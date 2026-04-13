import streamlit as st
from src.inference import RVModel

# Load model
model = RVModel(
    model_path="models/final_pipeline.pkl",
    config_path="config/config.yaml"
)

st.set_page_config(page_title="Exoplanet RV Predictor")

st.title(" Exoplanet Detection Predictor")
st.markdown("Predict likelihood of Radial Velocity detection")

# Inputs
pl_bmasse = st.number_input("Planet Mass (Earth Masses)", 0.1, 10000.0)
pl_orbper = st.number_input("Orbital Period (days)", 0.1, 10000.0)
pl_orbsmax = st.number_input("Semi-Major Axis (AU)", 0.01, 100.0)
st_mass = st.number_input("Stellar Mass (Solar Mass)", 0.1, 10.0)
sy_vmag = st.number_input("Visual Magnitude", 0.0, 20.0)
sy_dist = st.number_input("Distance (parsec)", 0.1, 10000.0)

if st.button("Predict"):
    input_data = {
        "pl_bmasse": pl_bmasse,
        "pl_orbper": pl_orbper,
        "pl_orbsmax": pl_orbsmax,
        "st_mass": st_mass,
        "sy_vmag": sy_vmag,
        "sy_dist": sy_dist
    }

    result = model.predict(input_data)

    st.subheader("Prediction")
    st.write(f"RV Detectable: {result['prediction']}")
    st.write(f"Probability: {result['probability']:.3f}")
