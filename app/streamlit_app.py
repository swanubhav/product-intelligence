import streamlit as st
import pandas as pd
import joblib

st.title("Product Intelligence AI")

slow_model = joblib.load("src/models/slow_death_model.pkl")
return_model = joblib.load("src/models/return_risk_model.pkl")

st.header("Slow-Death Product Prediction")

price = st.number_input("Price")
rating = st.slider("Rating", 1.0, 5.0, 4.0)
sales = st.number_input("Sales Count")
return_rate = st.slider("Return Rate", 0.0, 1.0, 0.2)
age = st.number_input("Product Age (days)")

if st.button("Predict Product Health"):
    pred = slow_model.predict([[price, rating, sales, return_rate, age]])
    st.success("Dying Product" if pred[0] == 1 else "Healthy Product")

st.header("Return Risk Before Shipping")

qty = st.number_input("Quantity", 1, 5)

if st.button("Predict Return Risk"):
    prob = return_model.predict_proba([[qty]])[0][1]
    st.warning(f"Return Probability: {round(prob,2)}")
