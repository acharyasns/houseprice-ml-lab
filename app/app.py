import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")

with st.form("predict"):
    locality = st.selectbox(
    "Choose a locality:",["BTM Layout", "Attibele", "K R Puram ", "Marathahalli",'Indiranagar'])
    area = st.number_input("Area", value=15000)
    rent = st.number_input("rent", value=1000)
    facing = st.selectbox(
    "Choose a facing:",["North-West","North-East",'North-West', "East", "North", "West",'South'])
    bhk = st.selectbox(
    "Choose a bhk:",[1,2,3,4])
    bathrooms = st.number_input("bathrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.selectbox("Choose a parking:",["Bike","Car",'Bike and Car'])
    submitted = st.form_submit_button("Predict")


if submitted:
    X = pd.DataFrame([{
        "locality": locality,
        "area": area,
        'rent':rent,
        "facing": facing,
        "BHK": bhk,
        "bathrooms": bathrooms,
        "parking": parking 
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
