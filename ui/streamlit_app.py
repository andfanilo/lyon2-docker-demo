import requests
import streamlit as st

st.title("Iris Dataset Prediction")

with st.form("prediction"):
    sepal_length=st.slider("Sepal Length", 0.0, 8.0)
    sepal_width=st.slider("Sepal Width", 0.0, 8.0)
    petal_length=st.slider("Petal Length", 0.0, 8.0)
    petal_width=st.slider("Petal Width", 0.0, 8.0)

    if st.form_submit_button("Submit data"):
        with st.spinner("Predicting..."):
            response = requests.post("http://localhost:8000/predict", json={
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
            })
            json_response = response.json()
        st.info(f"Prediction was **{json_response['prediction']}**")