import requests
import streamlit as st

st.title("Iris Dataset Prediction")

with st.form("prediction"):
    sepal_length = st.slider("Sepal Length")
    sepal_width = st.slider("Sepal Width")
    petal_length = st.slider("Petal Length")
    petal_width = st.slider("Petal Width")
    
    submit_button = st.form_submit_button("Predict flower") 

if submit_button:
    r = requests.post(
        "http://server:8000/predict", 
        json = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )
    st.write(r.json())